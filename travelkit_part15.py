# === Stage 15: Add a simple command dispatcher for text commands ===
# Project: TravelKit
class CommandDispatcher:
    def __init__(self, handlers):
        self.handlers = {cmd.lower(): handler for cmd, handler in handlers.items()}

    def dispatch(self, text):
        clean_text = text.strip().lower()
        if not clean_text or clean_text.startswith('#'): return None
        for keyword, handler in sorted(self.handlers.items()):
            if clean_text.startswith(keyword) and len(clean_text) > len(keyword):
                args = clean_text[len(keyword):].strip()
                try:
                    return handler(args)
                except Exception as e:
                    print(f"Error executing command '{keyword}': {e}")
                    return None
        if clean_text in self.handlers:
            return self.handlers[clean_text]()
        return f"Unknown command. Available: {', '.join(sorted(self.handlers.keys()))}"

    def register(self, keyword, handler):
        self.handlers[keyword.lower()] = handler
