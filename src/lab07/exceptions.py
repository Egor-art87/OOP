class StudentAppError(Exception):
    """Базовое исключение для всех ошибок приложения."""
    pass

class StudentNotFoundError(StudentAppError):
    """Выбрасывается, когда студент с указанным ID не найден."""
    def __init__(self, student_id: int):
        super().__init__(f"Студент с ID {student_id} не найден.")
        self.student_id = student_id

class DuplicateStudentError(StudentAppError):
    """Выбрасывается при попытке добавить студента с уже существующим ID."""
    def __init__(self, student_id: int):
        super().__init__(f"Студент с ID {student_id} уже существует в коллекции.")
        self.student_id = student_id

class InvalidInputError(StudentAppError):
    """Выбрасывается, если пользователь ввел некорректные данные в CLI."""
    pass