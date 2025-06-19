# update.py

import json
from datetime import datetime

# Шлях до шаблону
TEMPLATE_PATH = "template/index_template.html"
OUTPUT_PATH = "index.html"
DATA_PATH = "data/report.json"

def load_template():
    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        return f.read()

def load_data():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def generate_html(template: str, data: dict) -> str:
    return template\
        .replace("{{date}}", data["date"])\
        .replace("{{vix}}", str(data["vix"]))\
        .replace("{{sp500_change}}", str(data["sp500_change"]))\
        .replace("{{btc_usd}}", str(data["btc_usd"]))\
        .replace("{{market_summary}}", data["market_summary"])

def save_output(html: str):
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(html)

if name == "main":
    template = load_template()
    data = load_data()
    html = generate_html(template, data)
    save_output(html)
    print("✅ index.html згенеровано успішно")
