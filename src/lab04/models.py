import sys
from pathlib import Path

project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))


from src.lab03.base import Student as BaseStudent
from src.lab03.models import BakalavrStudent as _BakalavrStudent
from src.lab03.models import MagaStudent as _MagaStudent
from src.lib.collection import StudentCollection
from src.lab04.interfaces import Printable, Comparable


class Student(BaseStudent, Printable, Comparable):
    """Студент с контрактами Printable и Comparable."""
    def to_string(self) -> str:
        return str(self)

    def compare_to(self, other) -> int:
        if not isinstance(other, BaseStudent):
            raise TypeError("Сравнение только с объектами Student")
        if self.gpa < other.gpa:
            return -1
        elif self.gpa > other.gpa:
            return 1
        return 0


class BakalavrStudent(_BakalavrStudent, Printable, Comparable):
    """Бакалавр с интерфейсами."""
    def to_string(self) -> str:
        return str(self)

    def compare_to(self, other) -> int:
        if not isinstance(other, BaseStudent):
            raise TypeError("Сравнение только с объектами Student")
        # Сортируем по курсу, затем по GPA
        if self.course != other.course:
            return -1 if self.course < other.course else 1
        if self.gpa != other.gpa:
            return -1 if self.gpa < other.gpa else 1
        return 0


class MagaStudent(_MagaStudent, Printable, Comparable):
    """Магистрант с интерфейсами."""
    def to_string(self) -> str:
        return str(self)

    def compare_to(self, other) -> int:
        if not isinstance(other, BaseStudent):
            raise TypeError("Сравнение только с объектами Student")
        # Если other тоже магистрант — сравниваем по теме, затем по GPA
        if isinstance(other, MagaStudent):
            self_has = self.thesis_topic != "Не определена"
            other_has = other.thesis_topic != "Не определена"
            if self_has != other_has:
                return 1 if self_has else -1
            if self.gpa != other.gpa:
                return -1 if self.gpa < other.gpa else 1
            return 0
        else:
            if self.course != other.course:
                return -1 if self.course < other.course else 1
            if self.gpa != other.gpa:
                return -1 if self.gpa < other.gpa else 1
            return 0


class ExtendedStudentCollection(StudentCollection):
    """Коллекция с фильтрацией по интерфейсам."""
    
    def get_printable(self) -> list[Printable]:
        return [obj for obj in self if isinstance(obj, Printable)]

    def get_comparable(self) -> list[Comparable]:
        return [obj for obj in self if isinstance(obj, Comparable)]

    def get_sorted_comparables(self, reverse: bool = False) -> list[Comparable]:
        from functools import cmp_to_key
        comps = self.get_comparable()
        return sorted(comps, key=cmp_to_key(lambda a, b: a.compare_to(b)), reverse=reverse)