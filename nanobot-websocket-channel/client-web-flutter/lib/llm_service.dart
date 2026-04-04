import 'dart:async';
import 'dart:convert';
import 'package:web_socket_channel/web_socket_channel.dart';

import 'protocol.dart';

/// Nanobot webchat client over WebSocket.
///
/// Connects to the nanobot webchat channel and sends/receives messages.
/// All incoming messages are emitted on [responses]; the UI decides how to
/// display them (progress vs final answer are both chat bubbles).
class LlmService {
  WebSocketChannel? _channel;
  final StreamController<OutboundMessage> _responses =
      StreamController<OutboundMessage>.broadcast();

  /// WebSocket URL path (appended to the page origin).
  final String wsUrl;

  LlmService({this.wsUrl = '/ws/chat'});

  /// Probe the WebSocket endpoint before entering the chat UI.
  ///
  /// The webchat server rejects invalid access keys by closing the socket
  /// immediately, so a short grace period is enough to distinguish a bad key
  /// from a healthy connection.
  static Future<void> validateAccessKey(
    String accessKey, {
    String wsUrl = '/ws/chat',
    Duration gracePeriod = const Duration(milliseconds: 1500),
  }) async {
    final origin = Uri.base;
    final scheme = origin.scheme == 'https' ? 'wss' : 'ws';
    final query = '?access_key=${Uri.encodeComponent(accessKey)}';
    final uri = Uri.parse('$scheme://${origin.host}:${origin.port}$wsUrl$query');
    final channel = WebSocketChannel.connect(uri);
    final completer = Completer<void>();
    var settled = false;
    Timer? timer;

    void succeed() {
      if (settled) return;
      settled = true;
      timer?.cancel();
      channel.sink.close();
      completer.complete();
    }

    void fail([Object? _]) {
      if (settled) return;
      settled = true;
      timer?.cancel();
      channel.sink.close();
      completer.completeError(
        Exception('Invalid access key or WebSocket connection failed'),
      );
    }

    channel.stream.listen(
      (_) {},
      onError: fail,
      onDone: fail,
      cancelOnError: true,
    );

    timer = Timer(gracePeriod, succeed);
    return completer.future;
  }

  String? _accessKey;
  bool _disposed = false;
  int _reconnectAttempts = 0;
  Timer? _reconnectTimer;

  static const _maxReconnectDelay = Duration(seconds: 30);

  /// Stream that emits `true` on connect and `false` on disconnect.
  final StreamController<bool> _connectionState =
      StreamController<bool>.broadcast();
  Stream<bool> get connectionState => _connectionState.stream;

  /// Connect to the nanobot webchat WebSocket.
  /// Derives the WS URL from the page origin (works when served by Caddy).
  /// When [accessKey] is provided it is sent as a query parameter so the
  /// channel can validate access to the deployment.
  void connect({String? accessKey}) {
    _accessKey = accessKey;
    _connectInternal();
  }

  void _connectInternal() {
    if (_disposed) return;
    _channel?.sink.close();
    final origin = Uri.base;
    final scheme = origin.scheme == 'https' ? 'wss' : 'ws';
    final query = _accessKey != null
        ? '?access_key=${Uri.encodeComponent(_accessKey!)}'
        : '';
    final uri = Uri.parse('$scheme://${origin.host}:${origin.port}$wsUrl$query');
    _channel = WebSocketChannel.connect(uri);
    _reconnectAttempts = 0;
    _connectionState.add(true);
    _channel!.stream.listen(
      (data) {
        try {
          final response = OutboundMessage.fromWire(data as String);
          if (response is TextMessage && response.content.isEmpty) {
            return;
          }
          _responses.add(response);
        } catch (_) {}
      },
      onError: (_) => _scheduleReconnect(),
      onDone: () => _scheduleReconnect(),
    );
  }

  void _scheduleReconnect() {
    if (_disposed) return;
    _channel = null;
    _connectionState.add(false);
    final delay = Duration(
      seconds: (1 << _reconnectAttempts).clamp(1, _maxReconnectDelay.inSeconds),
    );
    _reconnectAttempts++;
    _reconnectTimer?.cancel();
    _reconnectTimer = Timer(delay, _connectInternal);
  }

  /// Send a message to nanobot.
  void send(String message) {
    if (_channel == null) return;
    _channel!.sink.add(jsonEncode({'content': message}));
  }

  /// Stream of all incoming response messages from nanobot.
  Stream<OutboundMessage> get responses => _responses.stream;

  bool get isConnected => _channel != null;

  void disconnect() {
    _reconnectTimer?.cancel();
    _channel?.sink.close();
    _channel = null;
  }

  void dispose() {
    _disposed = true;
    disconnect();
    _responses.close();
    _connectionState.close();
  }
}
