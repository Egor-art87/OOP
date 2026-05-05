"""
Модуль strategies.py
Содержит все функции-стратегии, предикаты, фабрики и callable-объекты
для обработки коллекции студентов.
Каждая функция и класс имеют docstring.
"""

import sys
from pathlib import Path

project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from src.lab03.models import MagaStudent   # адаптируйте путь под свой проект

# ------------------------ Стратегии сортировки (key-функции) ------------------------

def by_name(student):
    """Возвращает имя студента для сортировки по алфавиту."""
    return student.name

def by_gpa_desc(student):
    """Возвращает отрицательный GPA для сортировки по убыванию среднего балла (шкала 0-5)."""
    return -student.gpa

def by_course_and_name(student):
    """Возвращает кортеж (курс, имя) для сортировки сначала по курсу, потом по имени."""
    return (student.course, student.name)

# ------------------------ Стратегии-фильтры (предикаты) ------------------------

def is_excellent(student):
    """
    Возвращает True, если средний балл (GPA) >= 4.5 (отличник).
    Шкала GPA: 0.0 – 5.0
    """
    return student.gpa >= 4.5

def is_master_student(student):
    """True, если студент является магистрантом (проверка через isinstance)."""
    return isinstance(student, MagaStudent)

def is_active(student):
    """True, если студент активен (не отчислен)."""
    return student.is_active

# ------------------------ Функции для map (преобразование) ------------------------

def get_name(student):
    """Возвращает только имя студента (для map)."""
    return student.name

def student_to_dict(student):
    """Преобразует студента в словарь с основными полями."""
    return {
        'name': student.name,
        'gpa': student.gpa,
        'course': student.course,
        'is_active': student.is_active,
    }

def get_scholarship_info(student):
    """Возвращает строку со стипендией, если метод calculate_scholarship существует."""
    if hasattr(student, 'calculate_scholarship'):
        try:
            scholarship = student.calculate_scholarship()
            return f"{student.name}: {scholarship:.2f} руб."
        except Exception:
            return f"{student.name}: ошибка расчёта стипендии"
    return f"{student.name}: стипендия не рассчитана"

# ------------------------ Функции для apply (действие с побочным эффектом) ------------------------

def promote_student(student):
    """
    Переводит студента на следующий курс.
    Если перевод невозможен (максимальный курс или неактивен), игнорирует ошибку.
    """
    try:
        student.promote()
    except ValueError:
        pass

def activate_student(student):
    """Восстанавливает студента (делает активным)."""
    student.active()

def expel_student(student):
    """Отчисляет студента (делает неактивным)."""
    student.expel()

# ------------------------ Фабрика функций ------------------------

def make_min_gpa_filter(min_gpa):
    """
    Возвращает функцию-фильтр, которая отбирает студентов с GPA не ниже заданного порога.
    Параметры:
        min_gpa (float): минимальный средний балл (шкала 0-5).
    Возвращает:
        function: функция-предикат.
    """
    def filter_fn(student):
        return student.gpa >= min_gpa
    filter_fn.__doc__ = f"Фильтр: GPA >= {min_gpa}"
    return filter_fn

# ------------------------ Callable-объекты (стратегии как классы) ------------------------

class GpaBooster:
    """
    Callable-стратегия: увеличивает GPA студента на заданную величину.
    Не позволяет GPA превысить 5.0 (шкала 0-5).
    """
    def __init__(self, increment: float):
        self.increment = increment

    def __call__(self, student):
        new_gpa = student.gpa + self.increment
        if new_gpa > 5.0:
            new_gpa = 5.0
        student.gpa = new_gpa

class StudentFormatter:
    """
    Callable-стратегия: форматирует информацию о студенте в строку по шаблону.
    Используется с map().
    """
    def __init__(self, template: str = "{name} (GPA: {gpa}, Course: {course})"):
        self.template = template

    def __call__(self, student):
        return self.template.format(
            name=student.name,
            gpa=student.gpa,
            course=student.course,
            active="Active" if student.is_active else "Inactive"
        )