# === Stage 44: Add backup creation for the data file ===
# Project: TravelKit
import json, os, datetime
def backup_data(file_path: str) -> None:
    if not os.path.exists(file_path): return
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    dir_name = "backups"
    os.makedirs(dir_name, exist_ok=True)
    dest_path = os.path.join(dir_name, f"{os.path.basename(file_path)}.{timestamp}")
    with open(file_path, 'r', encoding='utf-8') as src: data = json.load(src)
    with open(dest_path, 'w', encoding='utf-8') as dst: json.dump(data, dst, indent=2, ensure_ascii=False)
