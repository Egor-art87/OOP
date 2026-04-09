from model import Student
from collection import StudentCollection


def show_collection(collection: StudentCollection, message: str = "Текущая коллекция"):
    print(f"\n{message} (всего: {len(collection)}):")
    if len(collection) == 0:
        print("  <пусто>")
        return
    for s in collection:
        print(
            f"  ID {s.student_id}: {s.name} (курс {s.course}) | Активен: {s.is_active}"
        )


def main():
    print("СОЗДАНИЕ СТУДЕНТОВ")
    students = [
        Student(1234567, "Анна Смирнова", 19, 4.8, 2),
        Student(1000001, "Иван Петров", 20, 4.2, 3),
        Student(1111111, "Мария Иванова", 18, 4.9, 1),
        Student(2222222, "Дмитрий Сидоров", 21, 3.8, 4),
        Student(3333333, "Елена Козлова", 20, 4.5, 2),
    ]
    for s in students:
        print(f"  {s}")

    print("БАЗОВЫЕ ОПЕРАЦИИ")
    group = StudentCollection()
    for s in students:
        group.add(s)
    show_collection(group, "После добавления 5 студентов")

    print("\nПытаемся добавить студента с ID=1000001 (дубликат):")
    try:
        duplicate = Student(1000001, "Дубликат", 22, 3.0, 5)
        group.add(duplicate)
    except ValueError as e:
        print(f"  Ожидаемая ошибка: {e}")

    print("\nИспользуем get_all():")
    all_students = group.get_all()
    print(f"  Первые два студента: {all_students[0].name}, {all_students[1].name}")

    print("\nУдаляем студента с ID=2222222 (Дмитрий Сидоров):")
    group.remove(students[3])
    show_collection(group, "После удаления")

    print("ПОИСК, ДЛИНА, ИТЕРАЦИЯ")

    print("\nПоиск студента с ID=1000001 (Иван Петров):")
    found = group.find_by_id(1000001)
    print(f"  Результат: {found.name if found else 'не найден'}")

    print("\nПоиск студента с ID=9999999 (не существует):")
    found = group.find_by_id(9999999)
    print(f"  Результат: {found}")

    print(f"\nКоличество студентов через len(): {len(group)}")

    print("\nПеребор всех студентов:")
    for s in group:
        print(f"  - {s.name} (курс {s.course})")

    # ========== 4. ИНДЕКСАЦИЯ И УДАЛЕНИЕ ПО ИНДЕКСУ ==========
    print("\nИНДЕКСАЦИЯ И УДАЛЕНИЕ ПО ИНДЕКСУ")

    print("\nДоступ по индексам:")
    print(f"  group[0] -> {group[0].name}")
    print(f"  group[1] -> {group[1].name}")
    print(f"  group[2] -> {group[2].name}")

    print("\nПопытка получить group[100] (выход за границы):")
    try:
        group[100]
    except IndexError as e:
        print(f"  Ожидаемая ошибка: {e}")

    print("\nУдаляем элемент по индексу 1 (второй студент):")
    group.remove_at(1)
    show_collection(group, "После удаления по индексу")

    print("СОРТИРОВКА")

    group.add(students[3])
    show_collection(group, "Перед сортировкой (исходный порядок добавления)")

    print("\nСортировка по имени (А→Я):")
    group.sort(key=lambda s: s.name)
    show_collection(group, "После сортировки по имени")

    print("\nФИЛЬТРАЦИЯ (НОВЫЕ КОЛЛЕКЦИИ)")

    inactive_student = group.find_by_id(1000001)
    if inactive_student:
        inactive_student.expel()
        print(f"\nСтудент {inactive_student.name} стал неактивным (expel)")

    active_group = group.get_active()
    show_collection(active_group, "Активные студенты (новая коллекция)")

    course2_group = group.get_by_course(2)
    show_collection(course2_group, "Студенты 2-го курса (новая коллекция)")

    show_collection(group, "Исходная коллекция (не изменилась)")

    print("ДОПОЛНИТЕЛЬНЫЕ СЦЕНАРИИ")

    print("\nСценарий 1: Повышение курса студента с ID=1111111")
    s = group.find_by_id(1111111)
    if s:
        print(f"  До: {s.name}, курс {s.course}")
        s.promote()
        print(f"  После: курс {s.course}")

    print("\nСценарий 2: Лучший по GPA среди активных студентов")
    active = group.get_active()
    active.sort(key=lambda s: s.gpa, reverse=True)
    if len(active) > 0:
        best = active[0]
        print(f"  Лучший: {best.name}, GPA = {best.gpa}")

    print("\nСценарий 3: Студенты 1-го и 3-го курсов (новая коллекция)")
    special = StudentCollection()
    for s in group:
        if s.course == 1 or s.course == 3:
            special.add(s)
    show_collection(special, "Студенты 1 и 3 курсов")

    print("\nСценарий 4: Удаление всех неактивных студентов из коллекции")
    for i in range(len(group) - 1, -1, -1):
        if not group[i].is_active:
            print(f"  Удаляем {group[i].name} (ID {group[i].student_id})")
            group.remove_at(i)
    show_collection(group, "После удаления неактивных")


if __name__ == "__main__":
    main()
