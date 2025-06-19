from datetime import datetime

# Дані, які ти хочеш вивести (можна буде підключити інші джерела)
now = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

html = f"""<!DOCTYPE html>
<html lang="uk">
<head>
  <meta charset="UTF-8">
  <title>Оновлення ринку</title>
  <style>
    body {{
      font-family: sans-serif;
      background: #f2f2f2;
      padding: 2rem;
    }}
    .box {{
      background: #fff;
      padding: 1.5rem;
      border-radius: 10px;
      box-shadow: 0 2px 10px rgba(0,0,0,0.1);
      max-width: 800px;
      margin: auto;
    }}
    h1 {{
      color: #333;
    }}
  </style>
</head>
<body>
  <div class="box">
    <h1>Автоматичне оновлення ринку</h1>
    <p>Дані оновлено: <strong>{now}</strong></p>
    <p>Тут буде ваша аналітика та показники ринку.</p>
  </div>
</body>
</html>
"""

# Зберігаємо файл в корені репозиторію
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
