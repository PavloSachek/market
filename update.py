# update.py
import os
import subprocess

# Додаємо файли до коміту
subprocess.run(["git", "config", "--global", "user.email", "actions@github.com"])
subprocess.run(["git", "config", "--global", "user.name", "GitHub Actions"])

subprocess.run(["git", "add", "index.html"])
subprocess.run(["git", "commit", "-m", "🔄 Автоматичне оновлення index.html"])
subprocess.run(["git", "push", "origin", "main"])
