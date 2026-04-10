# ------------------
#   Validation
# ------------------


def validate_name(name):
    if not isinstance(name, str):
        raise TypeError("Name must be tupe string")
    if not name.strip():
        raise ValueError("Name cannot be empty")


def validate_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be tupe integer")
    if age < 16:
        raise ValueError("Studen must be at least 16 years")


def validate_gpa(gpa):
    if not isinstance(gpa, (int, float)):
        raise TypeError("Gpa must be tupe ineger or float")
    if not 0 <= gpa <= 5:
        raise ValueError("Gpa must be range from 0 to 5")


def validate_course(course):
    if not isinstance(course, int):
        raise TypeError("Course must be tupe integer")
    if not 1 <= course <= 6:
        raise ValueError("Course must be range form 1 to 6")
