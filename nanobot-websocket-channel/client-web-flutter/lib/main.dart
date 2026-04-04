import 'package:flutter/material.dart';
import 'package:web/web.dart' as web;
import 'chat_screen.dart';
import 'llm_service.dart';
import 'login_screen.dart';

void main() {
  runApp(const ChatbotApp());
}

class ChatbotApp extends StatefulWidget {
  const ChatbotApp({super.key});

  @override
  State<ChatbotApp> createState() => _ChatbotAppState();
}

class _ChatbotAppState extends State<ChatbotApp> {
  String _token = '';

  @override
  void initState() {
    super.initState();
    _token = web.window.localStorage.getItem('access_key') ?? '';
  }

  Future<String?> _handleLogin(String token) async {
    try {
      await LlmService.validateAccessKey(token);
    } catch (_) {
      web.window.localStorage.removeItem('access_key');
      return 'Access key rejected. Please try again.';
    }

    web.window.localStorage.setItem('access_key', token);
    setState(() => _token = token);
    return null;
  }

  void _handleDisconnect() {
    web.window.localStorage.removeItem('access_key');
    setState(() => _token = '');
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Nanobot',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.indigo),
        useMaterial3: true,
        textSelectionTheme: const TextSelectionThemeData(
          selectionColor: Color(0x66FFD54F),
          selectionHandleColor: Color(0xFF1A237E),
          cursorColor: Color(0xFF1A237E),
        ),
      ),
      home: _token.isEmpty
          ? LoginScreen(onLogin: _handleLogin)
          : ChatScreen(
              accessKey: _token,
              onDisconnect: _handleDisconnect,
            ),
    );
  }
}
