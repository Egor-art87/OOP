from typing import List
from src.lab07.app import StudentApp
from src.lab03.models import BakalavrStudent, MagaStudent
from src.lab07.exceptions import StudentAppError
from src.lab05 import strategies

class CLI:
    """Класс консольного интерфейса."""
    
    def __init__(self, app: StudentApp):
        self.app = app

    def run(self) -> None:
        """Запускает бесконечный цикл меню."""
        print("Добро пожаловать в систему управления студентами!")
        while True:
            self._print_menu()
            try:
                choice = input("Выберите пункт меню: ").strip()
                if choice == '1':
                    self._show_all()
                elif choice == '2':
                    self._add_student()
                elif choice == '3':
                    self._find_student()
                elif choice == '4':
                    self._remove_student()
                elif choice == '5':
                    self._filter_students()
                elif choice == '6':
                    self._sort_students()
                elif choice == '0':
                    print("Сохранение данных и выход...")
                    self.app.save_data()
                    break
                else:
                    print("Ошибка: неверный пункт меню.")
            except StudentAppError as e:
                print(f"Ошибка приложения: {e}")
            except ValueError as e:
                print(f"Ошибка ввода: {e}")
            except Exception as e:
                print(f"Непредвиденная ошибка: {e}")
            print("-" * 40)

    def _print_menu(self) -> None:
        print("\n=== ГЛАВНОЕ МЕНЮ ===")
        print("1. Показать всех студентов")
        print("2. Добавить студента")
        print("3. Найти студента по ID")
        print("4. Удалить студента")
        print("5. Фильтр (GPA выше порога)")
        print("6. Сортировка")
        print("0. Выход")

    def _print_table(self, students: List) -> None:
        """Форматированный табличный вывод списка студентов."""
        if not students:
            print("Список пуст.")
            return
        print(f"{'ID':<10} | {'Имя':<15} | {'Курс':<5} | {'GPA':<5} | {'Тип'}")
        print("-" * 50)
        for s in students:
            s_type = "Бакалавр" if isinstance(s, BakalavrStudent) else "Магистр"
            print(f"{s.student_id:<10} | {s.name:<15} | {s.course:<5} | {s.gpa:<5.2f} | {s_type}")

    def _show_all(self) -> None:
        print("\n--- Все студенты ---")
        self._print_table(self.app.get_all_students())

    def _add_student(self) -> None:
        print("\n--- Добавление студента ---")
        s_type = input("Тип (1 - Бакалавр, 2 - Магистр): ").strip()
        s_id = int(input("ID (7 цифр): "))
        name = input("Имя: ")
        age = int(input("Возраст: "))
        gpa = float(input("GPA (0-5): "))
        course = int(input("Курс: "))

        if s_type == '1':
            spec = input("Специализация: ")
            student = BakalavrStudent(s_id, name, age, gpa, course, spec)
        elif s_type == '2':
            sup = input("Научный руководитель: ")
            student = MagaStudent(s_id, name, age, gpa, course, sup)
        else:
            print("Неверный тип.")
            return
            
        self.app.add_student(student)
        print("Студент успешно добавлен.")

    def _find_student(self) -> None:
        s_id = int(input("Введите ID для поиска: "))
        student = self.app.find_student(s_id)
        print("\nНайден студент:")
        student.display_info()

    def _remove_student(self) -> None:
        s_id = int(input("Введите ID студента для удаления: "))
        student = self.app.find_student(s_id)
        
        confirm = input(f"Вы уверены, что хотите удалить студента {student.name}? (y/n): ").strip().lower()
        if confirm == 'y':
            self.app.remove_student(s_id)
            print("Студент удален.")
        else:
            print("Отмена операции.")

    def _filter_students(self) -> None:
        min_gpa = float(input("Введите минимальный GPA: "))
        filtered = self.app.filter_by_min_gpa(min_gpa)
        print(f"\n--- Студенты с GPA >= {min_gpa} ---")
        self._print_table(filtered)

    def _sort_students(self) -> None:
        print("\nСортировать по:")
        print("1. Имени")
        print("2. GPA (по убыванию)")
        print("3. Курсу и Имени")
        choice = input("Ваш выбор: ").strip()
        
        if choice == '1':
            self.app.sort_students(strategies.by_name)
        elif choice == '2':
            self.app.sort_students(strategies.by_gpa_desc)
        elif choice == '3':
            self.app.sort_students(strategies.by_course_and_name)
        else:
            print("Неверный выбор.")
            return
            
        print("Коллекция отсортирована.")
        self._show_all()