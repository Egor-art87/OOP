import sys
from pathlib import Path

project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from src.lab03.base import Student
from src.lib.collection import StudentCollection


class BakalavrStudent(Student):

    def __init__(self, student_id: int, name: str, age: int, gpa: float, course: int,
                 specialization: str, has_practice: bool = False):
        super().__init__(student_id, name, age, gpa, course)
        self._specialization = specialization
        self._has_practice = has_practice

    @property
    def specialization(self):
        return self._specialization

    @specialization.setter
    def specialization(self, specialization: str):
        if not self._is_active:
            raise ValueError("Студент не активен")
        self._specialization = specialization

    @property
    def has_practice(self):
        return self._has_practice

    @has_practice.setter
    def has_practice(self, practic: bool):
        if not self._is_active:
            raise ValueError("Студент не активен")
        self._has_practice = practic

    def complete_practice(self) -> str:
        if not self._is_active:
            raise ValueError("Неактивный студент не может пройти практику")
        self._has_practice = True
        return f"{self._name} успешно прошёл(ла) практику."

    def can_apply_master(self) -> bool:
        return self._course >= 4 and self._gpa >= 4.0 and self._is_active

    def promote(self):
        if not self._is_active:
            raise ValueError("Inactive student cannot be promoted")
        if self._course >= 4:
            raise ValueError("Bachelor student cannot exceed course 4")
        self._course += 1

    def __str__(self):
        base_str = super().__str__()
        practice_status = "Пройдена" if self._has_practice else "Не пройдена"
        return (f"{base_str}\n"
                f"Specialization: {self._specialization}\n"
                f"Practice: {practice_status}")

    def calculate_scholarship(self) -> float:
        if not self._is_active:
            return 0.0
        base = super().calculate_scholarship()
        if self._has_practice:
            base += 500
        return base

    def display_info(self) -> None:
        print("=== Bachelor Student ===")
        print(str(self))
        print(f"Scholarship: {self.calculate_scholarship():.2f} RUB")
        print(f"Can apply to Master: {self.can_apply_master()}")


class MagaStudent(Student):
    """Студент магистратуры (1-2 курс)"""

    def __init__(self, student_id: int, name: str, age: int, gpa: float, course: int,
                 supervisor: str, thesis_topic: str = "Не определена"):
        super().__init__(student_id, name, age, gpa, course)
        self._supervisor = supervisor
        self._thesis_topic = thesis_topic

    @property
    def supervisor(self):
        return self._supervisor

    @property
    def thesis_topic(self):
        return self._thesis_topic

    @thesis_topic.setter
    def thesis_topic(self, new_topic: str):
        if not self._is_active:
            raise ValueError("Студент не активен")
        self._thesis_topic = new_topic

    def defend_thesis(self) -> str:
        if not self._is_active:
            raise ValueError("Неактивный студент не может защищаться")
        if self._course < 2:
            raise ValueError("Защита возможна только на 2 курсе")
        if self._thesis_topic == "Не определена":
            raise ValueError("Сначала выберите тему диссертации")
        return f"{self._name} успешно защитил(а) диссертацию на тему '{self._thesis_topic}'"

    def promote(self):
        if not self._is_active:
            raise ValueError("Inactive student cannot be promoted")
        if self._course >= 2:
            raise ValueError("Master student cannot exceed course 2")
        self._course += 1

    def __str__(self):
        base_str = super().__str__()
        return (f"{base_str}\n"
                f"Supervisor: {self._supervisor}\n"
                f"Thesis topic: {self._thesis_topic}")

    def calculate_scholarship(self) -> float:
        if not self._is_active:
            return 0.0
        base = super().calculate_scholarship()
        if self._thesis_topic != "Не определена":
            base += 1000
        return base

    def display_info(self) -> None:
        print("=== Master Student ===")
        print(str(self))
        print(f"Scholarship: {self.calculate_scholarship():.2f} RUB")