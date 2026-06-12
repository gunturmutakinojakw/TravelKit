# === Stage 12: Add JSON import with friendly error handling for malformed data ===
# Project: TravelKit
import json, os

def load_data(path: str) -> dict | None:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return {}
    except json.JSONDecodeError as e:
        error_msg = f"Error: Malformed JSON in '{path}'. Details: {e}"
        print(error_msg)
        # Attempt to salvage data by reading raw lines if possible, or just fail gracefully
        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            print("Raw file content for debugging:")
            print(content[:500])  # Print first 500 chars to help user identify issue
        except Exception:
            pass
        return {}

# Usage example within your main script logic
# data = load_data("data.json")
# if not isinstance(data, dict):
#     sys.exit(1)
