import sys
from pathlib import Path

project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from src.lab03.models import BakalavrStudent, MagaStudent
from src.lib.collection import StudentCollection

def main():

    col = StudentCollection()

    col.add(BakalavrStudent(1234567, "Иван Петров", 20, 4.7, 3, "Информатика", False))
    col.add(BakalavrStudent(2345678, "Анна Смирнова", 21, 4.1, 4, "Физика", True))
    col.add(MagaStudent(3456789, "Дмитрий Волков", 23, 5.0, 1, "Проф. Кузнецов", "Квантовые вычисления"))
    col.add(MagaStudent(4567890, "Елена Соколова", 24, 4.8, 2, "Д-р Иванова", "Машинное обучение"))
    col.add(BakalavrStudent(5678901, "Олег Новиков", 19, 3.9, 2, "Химия", False))

    print("--- Сценарий 1: Единый интерфейс display_info() ---")
    for student in col:
        student.display_info()
        print("-" * 50)

    print("\n--- Сценарий 2: Фильтрация по типу ---")
    bachelors = col.get_bakalavr_students()
    magisters = col.get_maga_students()

    print(f"Бакалавры ({len(bachelors)}):")
    for b in bachelors:
        print(f"  - {b.name}, курс {b.course}, специализация: {b.specialization}")

    print(f"\nМагистры ({len(magisters)}):")
    for m in magisters:
        print(f"  - {m.name}, курс {m.course}, руководитель: {m.supervisor}")

    print("\n--- Сценарий 3: Стипендии отличников (GPA >= 4.5) ---")
    excellent = col.get_by_gpa_threshold(4.5)
    for student in excellent:
        print(f"{student.name} (GPA: {student.gpa}) получает {student.calculate_scholarship():.2f} руб.")

    print("\n--- Дополнительный сценарий: Бизнес-операции ---")
    ivan = next((s for s in col if isinstance(s, BakalavrStudent) and not s.has_practice), None)
    if ivan:
        print(ivan.complete_practice())
        print(f"Новая стипендия Ивана: {ivan.calculate_scholarship():.2f} руб.")
        ivan.display_info()

    dmitry = next((s for s in col if isinstance(s, MagaStudent) and s.course == 1), None)
    if dmitry:
        try:
            print(dmitry.defend_thesis())
        except ValueError as e:
            print(f"Ошибка: {e}")
        dmitry.promote()
        print(f"Дмитрий переведён на {dmitry.course} курс.")
        print(dmitry.defend_thesis())

if __name__ == "__main__":
    main()