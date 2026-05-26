from typing import List, Callable, Any
from src.lib.collection import StudentCollection
from src.lab03.models import BakalavrStudent, MagaStudent
from src.lab07.exceptions import StudentNotFoundError, DuplicateStudentError
from src.lab07 import storage

class StudentApp:
    
    def __init__(self, filepath: str = "students_data.json"):
        self.filepath = filepath
        self.collection: StudentCollection = storage.load(self.filepath)

    def save_data(self) -> None:
        """Сохраняет текущее состояние коллекции в файл."""
        storage.save(self.collection, self.filepath)

    def add_student(self, student) -> None:
        """Добавляет студента в коллекцию с проверкой дубликатов."""
        if self.collection.find_by_id(student.student_id):
            raise DuplicateStudentError(student.student_id)
        self.collection.add(student)

    def remove_student(self, student_id: int) -> None:
        """Удаляет студента по ID."""
        student = self.collection.find_by_id(student_id)
        if not student:
            raise StudentNotFoundError(student_id)
        self.collection.remove(student)

    def find_student(self, student_id: int):
        """Возвращает студента по ID или вызывает исключение."""
        student = self.collection.find_by_id(student_id)
        if not student:
            raise StudentNotFoundError(student_id)
        return student

    def get_all_students(self) -> List:
        """Возвращает список всех студентов."""
        return self.collection.get_all()

    def filter_by_min_gpa(self, min_gpa: float) -> List:
        """Фильтрует студентов по минимальному баллу (используя метод коллекции)."""
        filtered_collection = self.collection.get_by_gpa_threshold(min_gpa)
        return filtered_collection.get_all()

    def sort_students(self, key_func: Callable[[Any], Any], reverse: bool = False) -> None:
        """Сортирует коллекцию на месте."""
        self.collection.sort(key=key_func, reverse=reverse)
#
    def register_student(self, s_type: str, s_id: int, name: str, age: int,
                        gpa: float, course: int, extra: str) -> None:
        if s_type == '1':
            student = BakalavrStudent(s_id, name, age, gpa, course, extra)
        elif s_type == '2':
            student = MagaStudent(s_id, name, age, gpa, course, extra)
        else:
            raise StudentNotFoundError("Неверный тип студента (допустимо 1 или 2)")
        self.add_student(student)