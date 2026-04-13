from base import Student

class BakalavrStudent(Student):
    def __init__(self, student_id: int, name: str, age: int, gpa: float, course: int,
                specialization: str, has_practice: bool = False ):
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

class MagaStudent(Student):
        def __init__(self, student_id: int, name: str, age: int, gpa: float, course: int,
                supervisor: str, thesis_topic: str = "Не определена"):
            super().__init__(student_id, name, age, gpa, course)
            self._supervisor = supervisor           
            self._thesis_topic = thesis_topic

        @property
        def supervisor(self):
             return self._supervisor

        @property
        def  thesis_topic(self):
             return self._thesis_topic
        
        @thesis_topic.setter
        def thesis_topic(self, new_topic: str):
             if not self._is_active:
                  raise ValueError("Студент не активен")
             self._thesis_topic = new_topic

