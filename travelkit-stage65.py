# === Stage 65: Add import merging behavior that avoids obvious duplicates ===
# Project: TravelKit
import sys, os, re
from pathlib import Path
def merge_imports(src_path: str) -> None:
    if not src_path.endswith('.py'): return
    with open(src_path, 'r', encoding='utf-8') as f: lines = f.readlines()
    imports = []
    for i, line in enumerate(lines):
        m = re.match(r'^\s*import\s+(\S+)(?:\s+(.+))?', line) or \
            re.match(r'^\s*from\s+(\S+)\s+import\s+(.+)', line)
        if not m: continue
        mod, names = (m.group(1), m.group(2).split() + ['']) if m else ('', [])
        for name in [n.strip() for n in names if n.strip()]:
            key = f"{mod}.{name}" if mod and name else name
            if not any(i[0] == key or i[1].startswith(key) for i in imports):
                imports.append((key, line))
    new_lines = []
    skip_next = 0
    for i, line in enumerate(lines):
        if skip_next > 0:
            skip_next -= 1
            continue
        m = re.match(r'^\s*import\s+(\S+)(?:\s+(.+))?', line) or \
            re.match(r'^\s*from\s+(\S+)\s+import\s+(.+)', line)
        if not m: new_lines.append(line); continue
        mod, names = (m.group(1), m.group(2).split() + ['']) if m else ('', [])
        skip_block = False
        for name in [n.strip() for n in names if n.strip()]:
            key = f"{mod}.{name}" if mod and name else name
            existing = next((i for i in imports if i[0] == key), None)
            if existing:
                skip_block = True
                break
        if not skip_block: new_lines.append(line); continue
        # Merge duplicates into first occurrence line
        orig_line = lines[i].rstrip()
        used_names = set()
        for name in [n.strip() for n in names if n.strip()]:
            key = f"{mod}.{name}" if mod and name else name
            existing = next((i for i in imports if i[0] == key), None)
            if existing: used_names.add(name)
        new_import_line = orig_line.replace(f" {names}", " ".join(sorted(used_names)))
        # Remove duplicates from subsequent lines by skipping them
        skip_next = 1
    with open(src_path, 'w', encoding='utf-8') as f: f.writelines(new_lines)
