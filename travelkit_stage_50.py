# === Stage 50: Add unit tests for import and export behavior ===
# Project: TravelKit
import json, os, tempfile, shutil
from pathlib import Path
from typing import Dict, List, Optional

def test_import_export():
    temp_dir = tempfile.mkdtemp()
    try:
        # Setup sample data for testing
        sample_data = {
            "trip_name": "Paris Adventure",
            "days": [
                {"day": 1, "places": ["Eiffel Tower"], "expenses": [{"desc": "Metro", "amount": 2.0}]}
            ],
            "packing_list": ["Passport", "Toothbrush"]
        }

        # Test Export to JSON
        export_path = Path(temp_dir) / "trip.json"
        TravelKit.export_trip(sample_data, str(export_path))
        
        assert export_path.exists(), "Export file was not created"
        with open(export_path) as f:
            exported_content = json.load(f)
        assert exported_content["trip_name"] == sample_data["trip_name"], "Trip name mismatch after export"

        # Test Import from JSON
        import_path = Path(temp_dir) / "imported_trip.json"
        with open(import_path, 'w') as f:
            json.dump(sample_data, f)
        
        imported_data = TravelKit.import_trip(str(import_path))
        assert imported_data["trip_name"] == sample_data["trip_name"], "Import failed to restore data correctly"

        # Test Export to CSV (Packing List only)
        csv_path = Path(temp_dir) / "packing.csv"
        TravelKit.export_packing_list(sample_data, str(csv_path))
        
        assert csv_path.exists(), "CSV export file was not created"
        with open(csv_path) as f:
            lines = f.readlines()
        assert len(lines) > 1, "CSV should contain header and at least one item"

    finally:
        shutil.rmtree(temp_dir)
