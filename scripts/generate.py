from datetime import datetime

# Формування заголовку
now = datetime.utcnow()
date_str = now.strftime("%d.%m.%Y")
start_time = now.strftime("%H:%M UTC")
end_time = (now.replace(second=0, microsecond=0)).strftime("%H:%M UTC")

html = f"""<!DOCTYPE html>
<html lang="uk">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Щоденний ринковий аналіз</title>
  <style>
    body {{
      background-color: #f9f9f9;
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      margin: 2rem;
      color: #333;
    }}
    .block {{
      background-color: #f0f0f0;
      padding: 1.5rem;
      border-radius: 8px;
      margin-bottom: 1.5rem;
    }}
    .italic {{
      font-style: italic;
      color: #666;
    }}
  </style>
</head>
<body>
  <div class="block">
    <h1>🔎 Щоденний аналіз ринку</h1>
    <p><strong>Дата аналізу:</strong> {date_str}</p>
    <p><strong>Час початку збору даних:</strong> {start_time}</p>
    <p><strong>Час завершення аналізу:</strong> {end_time}</p>
    <p class="italic">Цей аналіз сформовано автоматично.</p>
  </div>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
