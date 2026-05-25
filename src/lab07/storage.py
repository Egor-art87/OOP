import json
import os
from typing import Dict, Any
from src.lab03.models import BakalavrStudent, MagaStudent
from src.lib.collection import StudentCollection

def student_to_dict(student) -> Dict[str, Any]:
    """Конвертирует объект студента в словарь для JSON."""
    data = {
        "student_id": student.student_id,
        "name": student.name,
        "age": student.age,
        "gpa": student.gpa,
        "course": student.course,
        "is_active": student.is_active
    }
    
    if isinstance(student, BakalavrStudent):
        data["__type__"] = "bachelor"
        data["specialization"] = student.specialization
        data["has_practice"] = student.has_practice
    elif isinstance(student, MagaStudent):
        data["__type__"] = "master"
        data["supervisor"] = student.supervisor
        data["thesis_topic"] = student.thesis_topic
        
    return data

def dict_to_student(data: Dict[str, Any]):
    """Воссоздает объект студента из словаря."""
    student_type = data.get("__type__")
    
    if student_type == "bachelor":
        student = BakalavrStudent(
            student_id=data["student_id"],
            name=data["name"],
            age=data["age"],
            gpa=data["gpa"],
            course=data["course"],
            specialization=data["specialization"],
            has_practice=data["has_practice"]
        )
    elif student_type == "master":
        student = MagaStudent(
            student_id=data["student_id"],
            name=data["name"],
            age=data["age"],
            gpa=data["gpa"],
            course=data["course"],
            supervisor=data["supervisor"],
            thesis_topic=data["thesis_topic"]
        )
    else:
        raise ValueError("Неизвестный тип студента в файле сохранения")
        
    if not data.get("is_active", True):
        student.expel()
        
    return student

def save(collection: StudentCollection, filepath: str) -> None:
    """Сохраняет коллекцию в JSON-файл."""
    data_list = [student_to_dict(s) for s in collection.get_all()]
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data_list, f, ensure_ascii=False, indent=4)

def load(filepath: str) -> StudentCollection:
    """Загружает коллекцию из JSON-файла."""
    collection = StudentCollection()
    if not os.path.exists(filepath):
        return collection
        
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data_list = json.load(f)
            for item in data_list:
                student = dict_to_student(item)
                collection.add(student)
    except Exception as e:
        print(f"Ошибка при загрузке данных: {e}")
        
    return collection