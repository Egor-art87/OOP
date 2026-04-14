# src/lab03/base.py
import sys
from pathlib import Path

# Добавляем корень проекта в sys.path
project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from src.lib.validation_student import (
    validate_name,
    validate_age,
    validate_gpa,
    validate_course,
    validate_student_id,
)


class Student:
    university_name = "НИТУ МИСИС"

    def __init__(self, student_id: int, name: str, age: int, gpa: float, course: int):
        validate_name(name)
        validate_age(age)
        validate_gpa(gpa)
        validate_course(course)
        validate_student_id(student_id)

        self._name = name
        self._age = age
        self._gpa = gpa
        self._course = course
        self._student_id = student_id
        self._is_active = True

    @property
    def student_id(self):
        return self._student_id

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, val_age):
        validate_age(val_age)
        if not self._is_active:
            raise ValueError("Cannot change age of inactive student")
        self._age = val_age

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

    @course.setter
    def course(self, val):
        validate_course(val)
        if not self._is_active:
            raise ValueError("Cannot change course of inactive student")
        self._course = val

    @property
    def is_active(self):
        return self._is_active

    def promote(self):
        if not self._is_active:
            raise ValueError("Inactive student cannot be promoted")
        if self._course >= 6:
            raise ValueError("Maximum course reached")
        self._course += 1

    def age_up(self):
        if not self._is_active:
            raise ValueError("Student is not active")
        self._age += 1

    def expel(self):
        self._is_active = False

    def active(self):
        self._is_active = True

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
            f"Student(student_id={self._student_id},name={self._name!r}, "
            f"age={self._age}, "
            f"gpa={self._gpa}, "
            f"course={self._course})"
        )

    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return self._student_id == other._student_id

    # Полиморфные методы (для ЛР-3)
    def calculate_scholarship(self) -> float:
        if not self._is_active:
            return 0.0
        if self._gpa >= 4.5:
            return 2500.0
        else:
            return 2000.0

    def display_info(self) -> None:
        print(str(self))