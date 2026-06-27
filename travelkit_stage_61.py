# === Stage 61: Add performance timing for core list and search operations ===
# Project: TravelKit
import time
from datetime import datetime, timedelta

def benchmark_operation(func, *args, iterations=5):
    """Measure execution time for a function."""
    start = time.perf_counter()
    for _ in range(iterations):
        func(*args)
    end = time.perf_counter()
    avg_time_ms = (end - start) / iterations * 1000
    return {
        "function": func.__name__,
        "avg_time_ms": round(avg_time_ms, 3),
        "timestamp": datetime.now().isoformat()
    }

def profile_list_operations(travel_data):
    """Benchmark core list operations."""
    results = []
    
    # Benchmark adding an item to packing list
    def add_item():
        travel_data["packing"].append({"item": "Socks", "category": "Clothing"})
    
    results.append(benchmark_operation(add_item))
    
    # Benchmark searching for a category in places
    def search_places(category):
        return [p for p in travel_data.get("places", []) if p.get("tags") and any(cat in tag.lower() for cat in category)]
    
    results.append(benchmark_operation(lambda: search_places(["beach"]), "Beach"))
    
    # Benchmark calculating total expenses
    def calculate_expenses():
        return sum(item["amount"] for item in travel_data.get("expenses", []))
    
    results.append(benchmark_operation(calculate_expenses))
    
    return results

if __name__ == "__main__":
    sample_data = {
        "packing": [{"item": "Passport"}],
        "places": [
            {"name": "Beach Resort", "tags": ["beach", "relaxation"]},
            {"name": "Mountain View", "tags": ["hiking", "nature"]}
        ],
        "expenses": [{"amount": 10.5}, {"amount": 20.0}]
    }
    
    print(profile_list_operations(sample_data))
