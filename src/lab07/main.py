# src/lab07/main.py
import sys
from pathlib import Path

# Добавляем корень проекта в sys.path для корректных импортов
project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from src.lab07.app import StudentApp
from src.lab07.cli import CLI

def main():
    """Точка входа в программу."""
    # Приложение автоматически загрузит данные из файла при запуске
    app = StudentApp("students_data.json")
    
    # Инициализация и запуск CLI
    cli = CLI(app)
    cli.run()

if __name__ == "__main__":
    main()