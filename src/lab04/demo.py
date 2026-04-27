"""
Демонстрация ЛР-4: интерфейсы и коллекция.
Показывает:
  1. Единый список объектов разных типов.
  2. Вызов интерфейсных методов (полиморфизм).
  3. Фильтрация коллекции по интерфейсам.
  4. Сортировку через Comparable.
  5. Универсальную функцию, работающую через интерфейс.
  6. Проверку isinstance.
"""
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from src.lab04.models import (
    Student,
    BakalavrStudent,
    MagaStudent,
    ExtendedStudentCollection,
)
from src.lab04.interfaces import Printable, Comparable


def print_all(items: list[Printable]) -> None:
    """Универсальная функция: работает с любыми Printable объектами."""
    print("\n=== Все объекты (Printable) ===")
    for item in items:
        print(item.to_string())


def show_comparable_info(items: list[Comparable]) -> None:
    """Демонстрация сортировки через интерфейс Comparable."""
    from functools import cmp_to_key
    sorted_items = sorted(items, key=cmp_to_key(lambda a, b: a.compare_to(b)))
    print("\n=== Отсортировано (Comparable) ===")
    for item in sorted_items:
        # item может быть и Printable, тогда покажем красиво
        if isinstance(item, Printable):
            print(item.to_string())
        else:
            print(item)


def main():
    # Создаём объекты (теперь из lab04 – они поддерживают интерфейсы)
    s1 = Student(1234567, "Иванов Иван", 20, 4.8, 3)
    b1 = BakalavrStudent(2345678, "Петрова Анна", 21, 4.2, 4, "Информатика", True)
    b2 = BakalavrStudent(3456789, "Сидоров Олег", 22, 3.9, 3, "Физика", False)
    m1 = MagaStudent(4567890, "Козлова Мария", 23, 4.9, 2, "Проф. Смирнов", "ИИ в медицине")
    m2 = MagaStudent(5678901, "Новиков Денис", 24, 4.5, 1, "Проф. Иванова")  # без темы

    # Наполняем коллекцию
    col = ExtendedStudentCollection()
    for obj in (s1, b1, b2, m1, m2):
        col.add(obj)

    # ===== СЦЕНАРИЙ 1: Полиморфный вывод через интерфейс Printable =====
    print("=" * 50)
    print("СЦЕНАРИЙ 1: Вывод всех объектов через Printable")
    print("=" * 50)
    printables = col.get_printable()
    print_all(printables)                     # универсальная функция
    # Покажем, что все они действительно Printable
    print("\nПроверка isinstance:")
    for obj in col:
        print(f"{obj.name}: Printable={isinstance(obj, Printable)}, Comparable={isinstance(obj, Comparable)}")

    # ===== СЦЕНАРИЙ 2: Сортировка через интерфейс Comparable =====
    print("\n" + "=" * 50)
    print("СЦЕНАРИЙ 2: Сортировка всех студентов (через compare_to)")
    print("=" * 50)
    sorted_students = col.get_sorted_comparables()
    for s in sorted_students:
        print(f"  {s.to_string()}")

    # ===== СЦЕНАРИЙ 3: Фильтрация коллекции по интерфейсам и архитектурное поведение =====
    print("\n" + "=" * 50)
    print("СЦЕНАРИЙ 3: Фильтрация только Comparable и работа с ними")
    print("=" * 50)
    comps = col.get_comparable()
    print(f"Объектов с Comparable: {len(comps)}")
    show_comparable_info(comps)

    # Дополнительно: покажем, что коллекция может работать с объектами,
    # не реализующими некоторые интерфейсы (если бы такие были).
    # В нашем случае все студенты реализуют оба интерфейса, но если добавить чистый Student
    # из lab03 (без интерфейсов), он не попадёт в get_printable/get_comparable.
    # Покажем разницу:
    print("\n=== Сравнение с обычным Student (без интерфейсов) ===")
    # Импортируем оригинальный класс (без интерфейсов)
    from src.lab03.base import Student as OldStudent
    old_s = OldStudent(9999999, "БезИнтерфейсов", 30, 3.0, 2)
    col.add(old_s)   # коллекция позволяет, т.к. это Student
    print("Объект без интерфейсов добавлен.")
    print(f"isinstance Printable: {isinstance(old_s, Printable)}")
    print(f"isinstance Comparable: {isinstance(old_s, Comparable)}")
    # get_printable не вернёт его
    new_printables = col.get_printable()
    print(f"Количество Printable объектов: {len(new_printables)}")   # 5, без old_s
    # Обход всей коллекции с проверкой интерфейса вручную (но вывод через интерфейс, если есть)
    print("\nРучной обход с полиморфизмом:")
    for obj in col:
        if isinstance(obj, Printable):
            print(obj.to_string())
        else:
            print(f"{obj.name}: не поддерживает Printable")


if __name__ == "__main__":
    main()