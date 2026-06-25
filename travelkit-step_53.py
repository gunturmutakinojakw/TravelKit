# === Stage 53: Add command help text and usage examples ===
# Project: TravelKit
def print_help():
    """Prints usage instructions and examples for TravelKit CLI."""
    help_text = (
        "TravelKit - Trip Organizer\n"
        "Usage: python travelkit.py <command> [options]\n\n"
        "Commands:\n"
        "  add-place     Add a new destination to the trip.\n"
        "  list-places   Display all saved places with details.\n"
        "  add-expense   Record an expense for a specific place or day.\n"
        "  show-budget   View total expenses and remaining budget.\n"
        "  plan-day      Create or view the itinerary for a specific day.\n"
        "  pack-list     Generate a packing checklist based on destinations.\n"
        "  save          Persist all changes to the local data file.\n\n"
        "Examples:\n"
        '  python travelkit.py add-place --name="Paris" --days=5\n'
        '  python travelkit.py list-places\n'
        '  python travelkit.py add-expense --place="Paris" --amount=120.50 --category="Food"\n'
        "  python travelkit.py show-budget\n"
        "  python travelkit.py plan-day --day=3\n"
        "  python travelkit.py pack-list --output=packing.txt\n\n"
        "Options:\n"
        "  --help        Show this help message and exit.\n"
    )
    print(help_text)
