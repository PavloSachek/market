# generate.py

import json
from datetime import datetime

def collect_market_data():
    # Тимчасові (заглушки) аналітичні дані — заміниш потім на API-збір
    return {
        "date": datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC"),
        "vix": 13.5,
        "sp500_change": -0.8,
        "btc_usd": 66100,
        "market_summary": "Ринок відкрився негативно через очікування рішення ФРС. VIX на низькому рівні.",
    }

def save_report(data):
    with open("data/report.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if name == "main":
    report = collect_market_data()
    save_report(report)
    print("✅ Данні зібрано і збережено в data/report.json")
