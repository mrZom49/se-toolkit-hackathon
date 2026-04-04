import 'package:flutter/material.dart';

class LoginScreen extends StatefulWidget {
  final Future<String?> Function(String token) onLogin;

  const LoginScreen({super.key, required this.onLogin});

  @override
  State<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  final _controller = TextEditingController();
  String? _error;
  bool _isLoading = false;

  Future<void> _handleConnect() async {
    final key = _controller.text.trim();
    if (key.isEmpty) {
      setState(() => _error = 'Please enter your access key');
      return;
    }

    setState(() {
      _error = null;
      _isLoading = true;
    });

    final error = await widget.onLogin(key);
    if (!mounted) return;

    setState(() {
      _isLoading = false;
      _error = error;
    });
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: ConstrainedBox(
          constraints: const BoxConstraints(maxWidth: 360),
          child: Card(
            elevation: 4,
            shape:
                RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
            child: Padding(
              padding: const EdgeInsets.all(32),
              child: Column(
                mainAxisSize: MainAxisSize.min,
                children: [
                  Icon(Icons.smart_toy_outlined,
                      size: 48,
                      color: Theme.of(context).colorScheme.primary),
                  const SizedBox(height: 16),
                  Text('Nanobot',
                      style: Theme.of(context).textTheme.headlineSmall),
                  const SizedBox(height: 8),
                  const Text('Enter your access key to connect.'),
                  const SizedBox(height: 24),
                  TextField(
                    controller: _controller,
                    enabled: !_isLoading,
                    obscureText: true,
                    decoration: const InputDecoration(
                      labelText: 'Access Key',
                      border: OutlineInputBorder(),
                    ),
                    onSubmitted: (_) => _handleConnect(),
                  ),
                  if (_error != null) ...[
                    const SizedBox(height: 12),
                    Text(_error!, style: const TextStyle(color: Colors.red)),
                  ],
                  const SizedBox(height: 24),
                  SizedBox(
                    width: double.infinity,
                    child: FilledButton(
                      onPressed: _isLoading ? null : _handleConnect,
                      child: Text(_isLoading ? 'Connecting...' : 'Connect'),
                    ),
                  ),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }
}
