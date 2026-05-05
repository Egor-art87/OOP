"""
Модуль demo.py
Демонстрирует работу с коллекцией студентов с использованием стратегий,
фабрик, callable-объектов и цепочек операций.
"""

import sys
from pathlib import Path

project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from src.lab05.collection import StudentCollection
from src.lab03.models import BakalavrStudent, MagaStudent  # ваш наследник
from src.lab05.strategies import (
    by_name,
    by_gpa_desc,
    by_course_and_name,
    is_excellent,
    is_master_student,
    get_name,
    promote_student,
    get_scholarship_info,
    make_min_gpa_filter,
    GpaBooster,
    StudentFormatter,
)

def print_collection(title, collection):
    """Вспомогательная функция для красивого вывода коллекции."""
    print(f"\n--- {title} ---")
    if len(collection) == 0:
        print("(пусто)")
        return
    for i, student in enumerate(collection, 1):
        print(f"{i}. {student}")


students_data = [
    BakalavrStudent(1000001, "Alice", 20, 4.8, 2, "Computer Science", has_practice=True),
    MagaStudent(2000001, "Bob", 22, 3.9, 1, "Dr. Smith", "Artificial Intelligence"),
    BakalavrStudent(1000002, "Charlie", 21, 3.2, 3, "Mathematics"),
    MagaStudent(2000002, "Diana", 23, 4.9, 2, "Dr. Brown", "Robotics"),
    BakalavrStudent(1000003, "Eve", 19, 4.5, 1, "Physics", has_practice=True),
]

col = StudentCollection()
for s in students_data:
    col.add(s)

# ================== Сценарий 1: полная цепочка filter -> sort -> apply ==================
print("\n" + "Сценарий 1: цепочка filter → sort → apply")
print_collection("Исходная коллекция", col)

# Цепочка: оставить отличников (GPA >= 4.5), отсортировать по имени, повысить курс
result_chain = (col
                .filter_by(is_excellent)
                .sort_by(by_name)
                .apply(promote_student))

print_collection("После filter(is_excellent) → sort(by_name) → apply(promote_student)", result_chain)

# Покажем, что исходная коллекция не изменилась структурно
print("\nИсходная коллекция (без изменений структуры):")
for s in col:
    print(s.name, s.gpa, "course:", s.course)

# ================== Сценарий 2: замена стратегии без изменения кода коллекции ==================
print("\n" + "Сценарий 2: замена стратегий сортировки")

# Создаём отдельную коллекцию, чтобы не портить предыдущие результаты
col2 = StudentCollection()
for s in col:   # копируем текущее состояние студентов
    col2.add(s)

print("Сортировка по имени:")
col2.sort_by(by_name)
print_collection("Результат сортировки by_name", col2)

print("\nСортировка по убыванию GPA (шкала 0-5):")
col2.sort_by(by_gpa_desc)   # возвращает -gpa
print_collection("Результат сортировки by_gpa_desc", col2)

print("\nСортировка по курсу и имени:")
col2.sort_by(by_course_and_name)
print_collection("Результат сортировки by_course_and_name", col2)

# Продемонстрируем фильтрацию с заменой предиката
print("\nФильтр: только магистранты:")
mag_only = col2.filter_by(is_master_student)
print_collection("Только магистранты", mag_only)

print("\nТот же метод filter_by, но с lambda – только студенты с GPA > 4.0:")
high_gpa = col2.filter_by(lambda s: s.gpa > 4.0)
print_collection("GPA > 4.0", high_gpa)

# ================== Сценарий 3: демонстрация callable-объектов ==================
print("\n" + "Сценарий 3: Callable-объекты")

# Создадим свежую коллекцию из исходных данных (чтоб не мешать другим сценариям)
col3 = StudentCollection()
for s in students_data:   # используем первоначальные данные
    col3.add(s)

print("GPA до применения GpaBooster:")
for s in col3:
    print(f"  {s.name}: {s.gpa}")

# Применяем callable-объект GpaBooster через apply с небольшим шагом
booster = GpaBooster(0.2)
col3.apply(booster)

print("\nGPA после col3.apply(GpaBooster(0.2)):")
for s in col3:
    print(f"  {s.name}: {s.gpa}")

# Callable в map: форматируем информацию
formatter = StudentFormatter("Студент {name}, балл {gpa}, курс {course} ({active})")
formatted_list = list(map(formatter, col3))
print("\nРезультат map(StudentFormatter):")
for line in formatted_list:
    print("  ", line)

# Дополнительно: фабрика функций
print("\nФабрика функций: фильтр по минимальному GPA = 4.0")
filter_4_0 = make_min_gpa_filter(4.0)
filtered_by_factory = col3.filter_by(filter_4_0) 
print_collection("Студенты с GPA >= 4.0 (после буста)", filtered_by_factory)
