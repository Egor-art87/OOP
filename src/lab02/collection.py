from model import Student


class StudentCollection:
    def __init__(self):
        self._items = []


    def add(self, student: Student) -> None:
        if not isinstance(student, Student):
            raise TypeError("Студент должен быть объектом Student")
        if student in self._items:
            raise ValueError("Студент уже существует")
        self._items.append(student)

    def remove(self, student: Student) -> None:
        if student not in self._items:
            raise ValueError("Такого студента не существует, нечего удалять")
        self._items.remove(student)

    def get_all(self) -> list:
        return self._items.copy()
    
    def find_by_id(self, student_id: int) -> Student | None:
        if not isinstance(student_id, int):
            raise TypeError("id студента должно быть типа integer")
        for student in self._items:
            if student.student_id == student_id:
                return student
        return None
    
    def __len__(self) -> int:
        return len(self._items)
    
    def __iter__(self):
        return iter(self._items)
    
    def __getitem__(self, index: int) -> Student:
        if not isinstance(index, int):
            raise TypeError("Индекс должен быть типа integer")
        if index < 0 or index > len(self._items):
            raise IndexError("Индекс не может быть меньше 0 или болбше длины списка")
        return self._items[index]
    
    def remove_at(self, index: int) -> None:
        if not isinstance(index, int):
            raise TypeError("Индекс должен быть типа integer")
        if index < 0 or index >= len(self._items):
            raise IndexError("Индекс не может быть меньше 0 или болбше длины списка")
        del self._items[index]

    def sort(self, key=None, reverse=False) -> None:
        self._items.sort(key=key, reverse=reverse)
    
    def get_active(self):
        new_col = StudentCollection()
        for s in self._items:
            if s.is_active:
                new_col.add(s)
        return new_col
    
    def get_by_course(self, course: int):
        if not isinstance(course, int):
            raise TypeError("Курс должен быть типа ineger")
        new_col = StudentCollection()
        for s in self._items:
            if s.course == course:
                new_col.add(s)
        return new_col

        
    

