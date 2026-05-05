"""
Модуль collection.py
Расширенная коллекция студентов с методами sort_by, filter_by, apply.
Поддерживает цепочки операций.
"""

import sys
from pathlib import Path
project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from src.lab03.base import Student  # или ваш точный путь к базовому классу

class StudentCollection:
    def __init__(self):
        self._items = []   # список объектов Student

    # ---------- Базовые методы (как в ЛР-2) ----------
    def add(self, student: Student) -> None:
        """Добавляет студента в коллекцию."""
        if not isinstance(student, Student):
            raise TypeError("Добавляемый объект должен быть Student")
        if student in self._items:
            raise ValueError("Студент уже существует в коллекции")
        self._items.append(student)

    def remove(self, student: Student) -> None:
        """Удаляет студента из коллекции."""
        if student not in self._items:
            raise ValueError("Студент не найден в коллекции")
        self._items.remove(student)

    def get_all(self) -> list:
        """Возвращает копию списка всех студентов."""
        return self._items.copy()

    def find_by_id(self, student_id: int):
        """Ищет студента по идентификатору."""
        for s in self._items:
            if s.student_id == student_id:
                return s
        return None

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index: int) -> Student:
        if not isinstance(index, int):
            raise TypeError("Индекс должен быть целым числом")
        if index < 0 or index >= len(self._items):
            raise IndexError("Индекс вне диапазона")
        return self._items[index]

    def remove_at(self, index: int) -> None:
        if not isinstance(index, int):
            raise TypeError("Индекс должен быть целым числом")
        if index < 0 or index >= len(self._items):
            raise IndexError("Индекс вне диапазона")
        del self._items[index]

    def sort(self, key=None, reverse=False) -> None:
        """Стандартная сортировка списка студентов."""
        self._items.sort(key=key, reverse=reverse)

    def get_active(self):
        """Возвращает новую коллекцию, содержащую только активных студентов."""
        new_col = StudentCollection()
        for s in self._items:
            if s.is_active:
                new_col.add(s)
        return new_col

    def get_by_course(self, course: int):
        """Возвращает новую коллекцию студентов заданного курса."""
        if not isinstance(course, int):
            raise TypeError("Курс должен быть целым числом")
        new_col = StudentCollection()
        for s in self._items:
            if s.course == course:
                new_col.add(s)
        return new_col

    # ---------- Новые методы для ЛР-5 (стратегии и цепочки) ----------

    def sort_by(self, key_func):
        """
        Сортирует студентов в коллекции по заданной key-функции.
        Возвращает self для возможности цепочек.
        """
        self._items.sort(key=key_func)
        return self

    def filter_by(self, predicate):
        """
        Создаёт и возвращает новую коллекцию, содержащую только студентов,
        для которых predicate(student) истинен.
        Исходная коллекция не изменяется.
        """
        new_col = StudentCollection()
        for student in self._items:
            if predicate(student):
                new_col.add(student)
        return new_col

    def apply(self, func):
        """
        Применяет функцию func к каждому студенту в коллекции.
        Возвращает self для цепочек.
        """
        for student in self._items:
            func(student)
        return self