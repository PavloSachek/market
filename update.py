import yfinance as yf
import pandas as pd
from datetime import datetime

# приклад: беремо S&P500 (SPY), Nasdaq (QQQ), Bitcoin (BTC-USD)
tickers = ["SPY", "QQQ", "BTC-USD"]

data = {}
for t in tickers:
    ticker = yf.Ticker(t)
    hist = ticker.history(period="2d")  # останні 2 дні
    if len(hist) >= 2:
        change = (hist["Close"][-1] - hist["Close"][-2]) / hist["Close"][-2] * 100
        data[t] = f"{change:.2f}%"
    else:
        data[t] = "немає даних"

# формуємо звіт
today = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

with open("report.txt", "w", encoding="utf-8") as f:
    f.write(f"Звіт за {today}\n\n")
    for t, ch in data.items():
        f.write(f"{t}: {ch}\n")

print("✅ report.txt створено")
