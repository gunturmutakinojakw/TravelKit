# === Stage 32: Add pagination helpers for long console output ===
# Project: TravelKit
def paginate_output(items, max_lines=15):
    if len(items) <= max_lines:
        print('\n'.join(str(i) for i in items))
        return
    total = len(items)
    page_size = (total + max_lines - 1) // max_lines
    start = 0
    while start < total:
        end = min(start + max_lines, total)
        print(f"--- Page {start//max_lines + 1} of {(total-1)//max_lines + 1} ---")
        for i in range(start, end):
            print(str(items[i]))
        start += page_size
