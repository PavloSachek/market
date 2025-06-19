# update.py
# Цей файл виконує аналіз і формує HTML-блок, який буде вставлено в index.html

from datetime import datetime

def run_analysis():
    # Тут ти можеш підключити аналіз даних (наприклад, із API або файлу)
    # Але для демонстрації вставляємо просто статичний текст і поточний час

    now = datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')

    html_block = f"""
    <h2>Звіт оновлено: {now}</h2>
    <p>Дані зібрано автоматично за допомогою GitHub Actions.</p>
    <p>Це демонстраційний блок, який ти можеш замінити на реальну аналітику.</p>
    """

    return html_block
