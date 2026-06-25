# === Stage 54: Add colorized output through optional ANSI codes ===
# Project: TravelKit
def colorize(text, style=""):
    codes = {"reset": "\033[0m", "bold": "\033[1m", "red": "\033[91m", "green": "\033[92m", "yellow": "\033[93m", "blue": "\033[94m"}
    if not style: return text
    prefix = codes.get(style, "") + codes["bold"]
    suffix = codes["reset"]
    return f"{prefix}{text}{suffix}"

def print_section(title):
    print(colorize(f"\n=== {title} ===", "blue"))

def print_success(msg):
    print(colorize(f"  [OK] {msg}", "green"))

def print_error(msg):
    print(colorize(f"  [ERR] {msg}", "red"))

def print_warning(msg):
    print(colorize(f"  [WARN] {msg}", "yellow"))
