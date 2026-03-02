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