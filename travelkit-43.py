# === Stage 43: Add CSV import for the primary record type ===
# Project: TravelKit
import csv
from pathlib import Path

def load_csv_records(file_path: str, record_type: str) -> list[dict]:
    records = []
    with open(Path(file_path), 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get('type') == record_type or not row.get('type'):
                records.append(row)
    return records

def save_records_to_csv(records: list[dict], file_path: str, column_names: list[str]) -> None:
    with open(Path(file_path), 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=column_names)
        writer.writeheader()
        for record in records:
            filtered_record = {col: record.get(col, '') for col in column_names}
            writer.writerow(filtered_record)
