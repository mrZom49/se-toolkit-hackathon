import 'dart:async';
import 'package:flutter/material.dart';

import 'llm_service.dart';
import 'protocol.dart';

class ChatMessage {
  final String text;
  final bool isUser;
  final DateTime timestamp;
  final OutboundMessage? structured;

  ChatMessage({required this.text, required this.isUser, this.structured})
      : timestamp = DateTime.now();

  factory ChatMessage.fromBotResponse(OutboundMessage response) {
    return ChatMessage(
      text: response.displayText,
      isUser: false,
      structured: response,
    );
  }
}

class ChatScreen extends StatefulWidget {
  final String accessKey;
  final VoidCallback? onDisconnect;

  const ChatScreen({super.key, required this.accessKey, this.onDisconnect});

  @override
  State<ChatScreen> createState() => _ChatScreenState();
}

class _ChatScreenState extends State<ChatScreen> {
  final List<ChatMessage> _messages = [];
  final TextEditingController _controller = TextEditingController();
  final ScrollController _scrollController = ScrollController();
  late final LlmService _llm = LlmService();
  StreamSubscription<OutboundMessage>? _sub;
  StreamSubscription<bool>? _connSub;
  bool _isLoading = false;
  bool _isConnected = true;
  Timer? _slowResponseTimer;
  Timer? _hardResponseTimer;
  final Stopwatch _elapsed = Stopwatch();
  Timer? _elapsedTicker;

  static const _slowResponseDuration = Duration(seconds: 20);
  static const _hardResponseDuration = Duration(seconds: 120);

  @override
  void initState() {
    super.initState();
    _llm.connect(accessKey: widget.accessKey);
    _sub = _llm.responses.listen(
      (response) {
        _cancelResponseTimers();
        setState(() {
          _messages.add(ChatMessage.fromBotResponse(response));
          _isLoading = false;
        });
        _scrollToBottom();
      },
    );
    _connSub = _llm.connectionState.listen((connected) {
      if (!mounted) return;
      if (connected && !_isConnected) {
        _addBotMessage('Reconnected.');
      } else if (!connected && _isConnected) {
        _cancelResponseTimers();
        setState(() => _isLoading = false);
        _addBotMessage('Connection lost. Reconnecting...');
      }
      setState(() => _isConnected = connected);
    });
    _addBotMessage(
      'Connected to Nanobot!\n\n'
      'Start by asking:\n'
      '• What can you do in this system?\n'
      '• What tools do you have right now?\n'
      '• Ask one question about the LMS or the system state.\n\n'
      'I am more than a chat UI only when the agent has tools, skills, and memory. '
      'Try discovering those capabilities from the conversation itself.',
    );
  }

  void _cancelResponseTimers() {
    _slowResponseTimer?.cancel();
    _hardResponseTimer?.cancel();
    _stopElapsed();
  }

  void _stopElapsed() {
    _elapsedTicker?.cancel();
    _elapsed.stop();
  }

  void _stopWaiting() {
    _llm.send('/stop');
    _cancelResponseTimers();
    setState(() => _isLoading = false);
  }

  void _startResponseTimeouts() {
    _slowResponseTimer?.cancel();
    _hardResponseTimer?.cancel();
    _slowResponseTimer = Timer(_slowResponseDuration, () {
      if (!mounted) return;
      _addBotMessage(
        'The assistant is still working on this request. '
        'Slow responses can happen when the model is busy.',
      );
    });
    _hardResponseTimer = Timer(_hardResponseDuration, () {
      if (!mounted) return;
      _addBotMessage(
        'This request is taking unusually long. '
        'Press the stop button to cancel and try again.',
      );
    });
  }

  void _addBotMessage(String text) {
    setState(() {
      _messages.add(ChatMessage(text: text, isUser: false));
    });
    _scrollToBottom();
  }

  void _scrollToBottom() {
    WidgetsBinding.instance.addPostFrameCallback((_) {
      if (_scrollController.hasClients) {
        _scrollController.animateTo(
          _scrollController.position.maxScrollExtent,
          duration: const Duration(milliseconds: 300),
          curve: Curves.easeOut,
        );
      }
    });
  }

  void _sendMessage(String text) {
    final trimmed = text.trim();
    if (trimmed.isEmpty || _isLoading) return;

    _controller.clear();
    setState(() {
      _messages.add(ChatMessage(text: trimmed, isUser: true));
      _isLoading = true;
    });
    _scrollToBottom();

    _llm.send(trimmed);
    _elapsed.reset();
    _elapsed.start();
    _elapsedTicker = Timer.periodic(
      const Duration(seconds: 1),
      (_) => setState(() {}),
    );
    _startResponseTimeouts();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Nanobot'),
        backgroundColor: Theme.of(context).colorScheme.primary,
        foregroundColor: Colors.white,
        actions: [
          if (widget.onDisconnect != null)
            IconButton(
              icon: const Icon(Icons.logout),
              tooltip: 'Disconnect',
              onPressed: widget.onDisconnect,
            ),
        ],
      ),
      body: Column(
        children: [
          Expanded(
            child: SelectionArea(
              child: ListView.builder(
                controller: _scrollController,
                padding: const EdgeInsets.all(16),
                itemCount: _messages.length + (_isLoading ? 1 : 0),
                itemBuilder: (context, index) {
                  if (index == _messages.length) {
                    return _buildLoadingBubble();
                  }
                  return _buildMessageBubble(_messages[index]);
                },
              ),
            ),
          ),
          _buildInputArea(),
        ],
      ),
    );
  }

  Widget _buildMessageBubble(ChatMessage message) {
    final isUser = message.isUser;
    if (!isUser && message.structured != null) {
      return _buildStructuredMessage(message.structured!);
    }
    return Align(
      alignment: isUser ? Alignment.centerRight : Alignment.centerLeft,
      child: Container(
        constraints: BoxConstraints(
          maxWidth: MediaQuery.of(context).size.width * 0.75,
        ),
        margin: const EdgeInsets.symmetric(vertical: 4),
        padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 10),
        decoration: BoxDecoration(
          color: isUser
              ? Theme.of(context).colorScheme.primary
              : Colors.grey[200],
          borderRadius: BorderRadius.only(
            topLeft: const Radius.circular(16),
            topRight: const Radius.circular(16),
            bottomLeft: Radius.circular(isUser ? 16 : 4),
            bottomRight: Radius.circular(isUser ? 4 : 16),
          ),
        ),
        child: SelectableText(
          message.text,
          textAlign: TextAlign.left,
          style: TextStyle(
            color: isUser ? Colors.white : Colors.black87,
            fontSize: 15,
          ),
        ),
      ),
    );
  }

  Widget _buildBotBubble(String text) {
    return Align(
      alignment: Alignment.centerLeft,
      child: Container(
        constraints: BoxConstraints(
          maxWidth: MediaQuery.of(context).size.width * 0.75,
        ),
        margin: const EdgeInsets.symmetric(vertical: 4),
        padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 10),
        decoration: BoxDecoration(
          color: Colors.grey[200],
          borderRadius: const BorderRadius.only(
            topLeft: Radius.circular(16),
            topRight: Radius.circular(16),
            bottomLeft: Radius.circular(4),
            bottomRight: Radius.circular(16),
          ),
        ),
        child: SelectableText(
          text,
          textAlign: TextAlign.left,
          style: const TextStyle(color: Colors.black87, fontSize: 15),
        ),
      ),
    );
  }

  Widget _buildStructuredMessage(OutboundMessage data) {
    if (data is ChoiceMessage) {
      return _buildChoiceMessage(data);
    }
    if (data is ConfirmMessage) {
      return _buildConfirmMessage(data);
    }
    if (data is CompositeMessage) {
      return _buildCompositeMessage(data);
    }
    return _buildBotBubble(data.displayText);
  }

  Widget _buildChoiceMessage(ChoiceMessage data) {
    final content = data.content;
    final options = data.options;
    return Align(
      alignment: Alignment.centerLeft,
      child: Container(
        constraints: BoxConstraints(
          maxWidth: MediaQuery.of(context).size.width * 0.75,
        ),
        margin: const EdgeInsets.symmetric(vertical: 4),
        padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 10),
        decoration: BoxDecoration(
          color: Colors.grey[200],
          borderRadius: const BorderRadius.only(
            topLeft: Radius.circular(16),
            topRight: Radius.circular(16),
            bottomLeft: Radius.circular(4),
            bottomRight: Radius.circular(16),
          ),
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            if (content.isNotEmpty)
              Padding(
                padding: const EdgeInsets.only(bottom: 8),
                child: SelectableText(
                  content,
                  textAlign: TextAlign.left,
                  style: const TextStyle(color: Colors.black87, fontSize: 15),
                ),
              ),
            Wrap(
              spacing: 6,
              runSpacing: 6,
              children: options.map<Widget>((opt) {
                return ActionChip(
                  label: Text(opt.label),
                  onPressed: _isLoading ? null : () => _sendMessage(opt.value),
                  backgroundColor: Colors.white,
                  side: BorderSide(
                    color: Theme.of(context).colorScheme.primary,
                  ),
                  labelStyle: TextStyle(
                    color: Theme.of(context).colorScheme.primary,
                  ),
                );
              }).toList(),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildConfirmMessage(ConfirmMessage data) {
    final content = data.content;
    return Align(
      alignment: Alignment.centerLeft,
      child: Container(
        constraints: BoxConstraints(
          maxWidth: MediaQuery.of(context).size.width * 0.75,
        ),
        margin: const EdgeInsets.symmetric(vertical: 4),
        padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 10),
        decoration: BoxDecoration(
          color: Colors.grey[200],
          borderRadius: const BorderRadius.only(
            topLeft: Radius.circular(16),
            topRight: Radius.circular(16),
            bottomLeft: Radius.circular(4),
            bottomRight: Radius.circular(16),
          ),
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            if (content.isNotEmpty)
              Padding(
                padding: const EdgeInsets.only(bottom: 8),
                child: SelectableText(
                  content,
                  textAlign: TextAlign.left,
                  style: const TextStyle(color: Colors.black87, fontSize: 15),
                ),
              ),
            Row(
              mainAxisSize: MainAxisSize.min,
              children: [
                ActionChip(
                  label: const Text('Yes'),
                  onPressed: _isLoading ? null : () => _sendMessage('yes'),
                  backgroundColor: Theme.of(context).colorScheme.primary,
                  side: BorderSide.none,
                  labelStyle: const TextStyle(color: Colors.white),
                ),
                const SizedBox(width: 8),
                ActionChip(
                  label: const Text('No'),
                  onPressed: _isLoading ? null : () => _sendMessage('no'),
                  backgroundColor: Colors.white,
                  side: BorderSide(color: Colors.grey[400]!),
                  labelStyle: const TextStyle(color: Colors.black87),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildCompositeMessage(CompositeMessage data) {
    final parts = data.parts;
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: parts.map<Widget>((part) {
        if (part is ChoiceMessage) return _buildChoiceMessage(part);
        if (part is ConfirmMessage) return _buildConfirmMessage(part);
        if (part is CompositeMessage) return _buildCompositeMessage(part);
        return _buildBotBubble(part.displayText);
      }).toList(),
    );
  }

  Widget _buildLoadingBubble() {
    final seconds = _elapsed.elapsed.inSeconds;
    return Align(
      alignment: Alignment.centerLeft,
      child: Container(
        margin: const EdgeInsets.symmetric(vertical: 4),
        padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 10),
        decoration: BoxDecoration(
          color: Colors.grey[200],
          borderRadius: const BorderRadius.only(
            topLeft: Radius.circular(16),
            topRight: Radius.circular(16),
            bottomLeft: Radius.circular(4),
            bottomRight: Radius.circular(16),
          ),
        ),
        child: Row(
          mainAxisSize: MainAxisSize.min,
          children: [
            const SizedBox(
              width: 20,
              height: 20,
              child: CircularProgressIndicator(strokeWidth: 2),
            ),
            const SizedBox(width: 10),
            Text(
              seconds > 0 ? 'Thinking... ${seconds}s' : 'Thinking...',
              style: TextStyle(color: Colors.grey[600], fontSize: 13),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildInputArea() {
    return Container(
      padding: const EdgeInsets.all(8),
      decoration: BoxDecoration(
        color: Colors.white,
        border: Border(top: BorderSide(color: Colors.grey[300]!)),
      ),
      child: Row(
        children: [
          Expanded(
            child: TextField(
              controller: _controller,
              decoration: const InputDecoration(
                hintText: 'Ask Nanobot about the system...',
                border: OutlineInputBorder(
                  borderRadius: BorderRadius.all(Radius.circular(24)),
                ),
                contentPadding:
                    EdgeInsets.symmetric(horizontal: 16, vertical: 10),
              ),
              onSubmitted: _isLoading ? null : _sendMessage,
            ),
          ),
          const SizedBox(width: 8),
          if (_isLoading)
            IconButton.filled(
              onPressed: _stopWaiting,
              icon: const Icon(Icons.stop),
              tooltip: 'Stop waiting',
              style: IconButton.styleFrom(
                backgroundColor: Colors.red[400],
              ),
            )
          else
            IconButton.filled(
              onPressed: () => _sendMessage(_controller.text),
              icon: const Icon(Icons.send),
            ),
        ],
      ),
    );
  }

  @override
  void dispose() {
    _cancelResponseTimers();
    _sub?.cancel();
    _connSub?.cancel();
    _controller.dispose();
    _scrollController.dispose();
    _llm.dispose();
    super.dispose();
  }
}
