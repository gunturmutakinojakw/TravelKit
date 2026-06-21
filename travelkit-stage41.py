# === Stage 41: Add plain text import for a simple line-based format ===
# Project: TravelKit
import csv

def load_plain_text(filename):
    items = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                parts = line.split(maxsplit=1)
                if len(parts) == 2:
                    items.append({'name': parts[0], 'category': parts[1]})
    return items

def save_plain_text(items, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for item in items:
            f.write(f"{item['name']} {item['category']}\n")
