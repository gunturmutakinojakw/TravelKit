# === Stage 42: Add CSV export without external dependencies ===
# Project: TravelKit
def export_to_csv(trip_data, filename="trip_export.csv"):
    import csv
    if not trip_data: return False
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=sorted(trip_data[0].keys()))
        writer.writeheader()
        for item in trip_data:
            writer.writerow(item)
    return True
