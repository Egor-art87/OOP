# lab 01
## Класс и инкапсуляция 


### Файл с основной логикой model.py

### Содержит основной класс Student, реализующий доменную модель студента. В классе инкапсулированы атрибуты (_name, _age, _gpa, _course, _is_active), реализована валидация входных данных через внешний модуль, добавлены свойства (@property) для контролируемого доступа к полям, а также бизнес-методы (promote, expel, activate, age_up). Поведение объекта зависит от логического состояния студента (активен / неактивен). Также переопределены магические методы __str__, __repr__ и __eq__.

```python
from validation_student import (
    validate_name,
    validate_age,
    validate_gpa,
    validate_course
)


class Student:
    university_name = 'НИТУ МИСиС'
    
    def __init__(self, name: str, age: int, gpa: float, course: int):
        validate_name(name)
        validate_age(age)
        validate_gpa(gpa)
        validate_course(course)

        self._name = name
        self._age = age
        self._gpa = gpa
        self._course = course
        self._is_active = True

        
    @property
    def name(self):
        return self._name

    @property
    def gpa(self):
        return self._gpa

    @gpa.setter
    def gpa(self, value):
        validate_gpa(value)
        if not self._is_active:
            raise ValueError("Cannot change GPA of inactive student")
        self._gpa = value

    @property
    def course(self):
        return self._course

    @property
    def is_active(self):
        return self._is_active
    
    # bisiness method

    def promote(self):
        if not self._is_active:
            raise ValueError("Inactive student cannot be promoted")

        if self._course >= 6:
            raise ValueError("Maximum course reached")

        self._course += 1

    def age_up(self):
        if not self._is_active:
            raise ValueError("Inactive student cannot be promoted")
        self._age += 1

    def expel(self):
        self._is_active = False

    def active(self):
        self._is_active = True

        # megic method 

    def __str__(self):
        status = "Active" if self._is_active else "Inactive"
        return (
            f"Student: {self._name}\n"
            f"Age: {self._age}\n"
            f"GPA: {self._gpa:.2f}\n"
            f"Course: {self._course}\n"
            f"Status: {status}"
        )

    def __repr__(self):
        return (
            f"Student(name={self._name!r}, "
            f"age={self._age}, "
            f"gpa={self._gpa}, "
            f"course={self._course})"
        )

    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return (
            self._name == other._name and
            self._age == other._age
        )
```

### файл с валидацией validation_student.py

### Содержит функции валидации данных: validate_name, validate_age, validate_gpa, validate_course. Отвечает исключительно за проверку корректности типов и допустимых диапазонов значений. Логика проверки вынесена в отдельный модуль для соблюдения принципа единственной ответственности и исключения дублирования кода.

```python 

#------------------
#   Validation
#------------------

def validate_name(name):
        if not isinstance(name, str):
            raise TypeError('Name must be tupe string')
        if not name.strip():
            raise ValueError("Name cannot be empty")
        

def validate_age(age):
    if not isinstance(age, int):
        raise TypeError('Age must be tupe integer')
    if age < 16:
        raise ValueError('Studen must be at least 16 years')
        

def validate_gpa(gpa):
    if not isinstance(gpa, (int, float)):
        raise TypeError('Gpa must be tupe ineger or float')
    if not 0 <= gpa <= 5:
        raise ValueError('Gpa must be range from 0 to 5')
        
        
def validate_course(course):
    if not isinstance(course, int):
        raise TypeError('Course must be tupe integer')
    if not 1 <= course <= 6:
        raise ValueError('Course must be range form 1 to 6')
```

### Демонстрационный файл demo.py

### Содержит демонстрацию работы программы. В файле показаны основные сценарии использования класса Student: создание объектов, сравнение, изменение GPA, изменение логического состояния (исключение и восстановление), обработка ошибок валидации и демонстрация атрибута класса. Файл используется для проверки корректности работы всей системы.

```python
from model import Student

# Сценарий 1
s1 = Student("Egor", 18, 4.5, 2)
print(s1)

# Сценарий 2 — сравнение
s2 = Student("Egor", 18, 3.8, 2)
print("Equal:", s1 == s2)

# Сценарий 3 — изменение GPA
s1.gpa = 4.8
print("Updated GPA:", s1.gpa)

# Сценарий 4 — состояние (не активен)
s1.expel()

try:
    s1.promote()
except ValueError as e:
    print("Error:", e)

# Сценарий 5 — ошибка валидации
try:
    Student("", 10, 10, 20)
except Exception as e:
    print("Validation error:", e)

# Атрибут класса
print(Student.university_name)
print(s1.university_name)
```
## Итог демонстрации 
![demo](/imeges/lab01/demo.png)
