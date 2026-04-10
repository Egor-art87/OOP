from validation_student import (
    validate_name,
    validate_age,
    validate_gpa,
    validate_course,
)


class Student:
    university_name = "НИТУ МИСиС"

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
            raise ValueError("Student is not active")
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
        return self._name == other._name and self._age == other._age
