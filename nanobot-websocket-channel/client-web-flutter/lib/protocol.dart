import 'dart:convert';

sealed class OutboundMessage {
  const OutboundMessage();

  factory OutboundMessage.fromWire(String raw) {
    try {
      final decoded = jsonDecode(raw);
      if (decoded is Map<String, dynamic>) {
        return OutboundMessage.fromJson(decoded);
      }
    } catch (_) {
      // Fall back to treating the payload as plain text.
    }
    return TextMessage(content: raw);
  }

  factory OutboundMessage.fromJson(Map<String, dynamic> json) {
    final type = json['type'] as String? ?? 'text';
    switch (type) {
      case 'choice':
        return ChoiceMessage.fromJson(json);
      case 'confirm':
        return ConfirmMessage.fromJson(json);
      case 'composite':
        return CompositeMessage.fromJson(json);
      default:
        return TextMessage.fromJson(json);
    }
  }

  String get displayText;
}

final class TextMessage extends OutboundMessage {
  const TextMessage({required this.content, this.format = 'markdown'});

  factory TextMessage.fromJson(Map<String, dynamic> json) {
    return TextMessage(
      content: json['content'] as String? ?? '',
      format: json['format'] as String? ?? 'markdown',
    );
  }

  final String content;
  final String format;

  @override
  String get displayText => content;
}

final class ChoiceOption {
  const ChoiceOption({required this.label, required this.value});

  factory ChoiceOption.fromJson(Map<String, dynamic> json) {
    final label = json['label'] as String? ?? '';
    return ChoiceOption(label: label, value: json['value'] as String? ?? label);
  }

  final String label;
  final String value;
}

final class ChoiceMessage extends OutboundMessage {
  const ChoiceMessage({required this.options, this.content = ''});

  factory ChoiceMessage.fromJson(Map<String, dynamic> json) {
    final optionsJson = json['options'];
    final options = optionsJson is List
        ? optionsJson
              .whereType<Map<String, dynamic>>()
              .map(ChoiceOption.fromJson)
              .toList()
        : <ChoiceOption>[];
    return ChoiceMessage(
      content: json['content'] as String? ?? '',
      options: options,
    );
  }

  final String content;
  final List<ChoiceOption> options;

  @override
  String get displayText => content;
}

final class ConfirmMessage extends OutboundMessage {
  const ConfirmMessage({this.content = ''});

  factory ConfirmMessage.fromJson(Map<String, dynamic> json) {
    return ConfirmMessage(content: json['content'] as String? ?? '');
  }

  final String content;

  @override
  String get displayText => content;
}

final class CompositeMessage extends OutboundMessage {
  const CompositeMessage({required this.parts});

  factory CompositeMessage.fromJson(Map<String, dynamic> json) {
    final partsJson = json['parts'];
    final parts = partsJson is List
        ? partsJson
              .whereType<Map<String, dynamic>>()
              .map(OutboundMessage.fromJson)
              .toList()
        : <OutboundMessage>[];
    return CompositeMessage(parts: parts);
  }

  final List<OutboundMessage> parts;

  @override
  String get displayText => parts.isEmpty ? '' : parts.first.displayText;
}
