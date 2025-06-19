# generate.py
# Скрипт формує index.html для GitHub Pages на основі актуальних даних

def generate_html():
    # Тут формуємо просту сторінку з контентом
    html_content = """<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8" />
    <title>Аналіз Ринку</title>
</head>
<body>
    <h1>Щоденний Аналіз Ринку</h1>
    <p>Це автоматично згенерована сторінка.</p>
</body>
</html>"""
    return html_content

def main():
    html = generate_html()
    # Записуємо у файл index.html в корені репозиторію
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("index.html успішно згенеровано.")

if name == "main":
    main()
