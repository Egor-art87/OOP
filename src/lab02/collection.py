from model import Student

class StudentCollection:

    def __init__(self):
        self._items = []

    def add(self, student: Student) -> None:
        if not isinstance(student, Student):
            raise TypeError("Only Student objects can be added")
        if student in self._items:
            raise ValueError(f"Student with id {student.student_id} already exists")
        self._items.append(student)

    def remove(self, student: Student) -> None:
        if student not in self._items:
            raise ValueError("Student not found in collection")
        self._items.remove(student)

    def get_all(self) -> list:
        return self._items.copy()

    def find_by_id(self, student_id: int) -> Student | None:
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
            raise TypeError("Index must be integer")
        if index < 0 or index >= len(self._items):
            raise IndexError("Index out of range")
        return self._items[index]

    def remove_at(self, index: int) -> None:
        if not isinstance(index, int):
            raise TypeError("Index must be integer")
        if index < 0 or index >= len(self._items):
            raise IndexError("Index out of range")
        del self._items[index]

    def sort(self, key=None, reverse=False) -> None:
        self._items.sort(key=key, reverse=reverse)

    def get_active(self):
        new_coll = StudentCollection()
        for s in self._items:
            if s.is_active:
                new_coll.add(s)
        return new_coll

    def get_by_course(self, course: int):
        new_coll = StudentCollection()
        for s in self._items:
            if s.course == course:
                new_coll.add(s)
        return new_coll