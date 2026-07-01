# === Stage 73: Add a lightweight HTML report export ===
# Project: TravelKit
from jinja2 import Template
import os, json, datetime

def export_report(trip_data):
    template = Template("""
<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>{{ trip_name }}</title>
<style>body{font-family:system-ui,sans-serif;margin:2rem;max-width:800px}h1{color:#333}.section{margin-top:2rem;border-bottom:1px solid #eee;padding-bottom:.5rem}</style></head><body>
<h1>{{ trip_name }}</h1>
<div class="section"><h2>Packing List</h2><ul>{% for item in packing %}<li>{{ item }}</li>{% endfor %}</ul></div>
<div class="section"><h2>Daily Plan</h2>{% for day,plan in days.items() %}<p><strong>{{ day }}:</strong> {{ plan|join(', ') }}</p>{% endfor %}</div>
<div class="section"><h2>Expenses</h2><ul>{% for exp in expenses %}<li>{{ exp }}</li>{% endfor %}</ul></div>
<div class="section"><h2>Places</h2><ul>{% for place in places %}<li>{{ place }}</li>{% endfor %}</ul></div>
<p style="margin-top:3rem;font-size:.8em">Generated on {{ now }}</p>
</body></html>""")

    with open(os.path.join(trip_data['output_dir'], f"{trip_data['name']}_report.html"), 'w', encoding='utf-8') as f:
        f.write(template.render(**{**trip_data, **{'now': datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}}, days=trip_data.get('days', {}), packing=trip_data.get('packing', []), expenses=trip_data.get('expenses', []), places=trip_data.get('places', [])))
