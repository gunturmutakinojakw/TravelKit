# === Stage 31: Add compact table rendering for long lists ===
# Project: TravelKit
from rich.table import Table, Column
def render_compact_table(data: list[dict], columns: list[str]) -> str:
    if not data: return "No data"
    table = Table(show_header=True, header_style="bold magenta", expand=False)
    for col in columns: table.add_column(col, style="dim")
    for row in data:
        cells = [str(row.get(c, ""))[:15] for c in columns]
        table.add_row(*cells)
    return "\n".join(table._render_text())
