# generate.py
from datetime import datetime

html_template = f"""
<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <title>Щоденний ринковий аналіз</title>
    <style>
        body {{
            background-color: #f9f9f9;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            margin: 40px;
        }}
        .block {{
            background-color: #ececec;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 30px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }}
        em {{
            color: #666;
        }}
    </style>
</head>
<body>
    <div class="block">
        <h1>📅 Щоденний ринковий аналіз</h1>
        <p><strong>Дата:</strong> {datetime.utcnow().strftime('%Y-%m-%d')}</p>
        <p><strong>Початок збору:</strong> {datetime.utcnow().strftime('%H:%M UTC')}</p>
        <p><strong>Завершення аналізу:</strong> {datetime.utcnow().strftime('%H:%M UTC')}</p>
        <p><em>Автоматично згенеровано за допомогою GitHub Actions</em></p>
    </div>
</body>
</html>
"""

with open("index.html", "w") as f:
    f.write(html_template)
