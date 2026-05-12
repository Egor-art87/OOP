import sys
from pathlib import Path

project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from src.lab03.models import BakalavrStudent, MagaStudent  
from src.lab06.container import TypedCollection, Displayable, Scorable


class DisplayableBachelor(BakalavrStudent):
    def display(self) -> str:
        """Соответствует протоколу Displayable."""
        return f"Бакалавр {self.name}, курс {self.course}, GPA: {self.gpa:.2f}"

    def score(self) -> float:
        """Соответствует протоколу Scorable (просто возвращает GPA)."""
        return self.gpa

class DisplayableMaster(MagaStudent):
    def display(self) -> str:
        return f"Магистр {self.name}, курс {self.course}, тема: {self.thesis_topic}"

    def score(self) -> float:
        return self.gpa + 0.5

diana = DisplayableBachelor(1000001, "Diana", 21, 4.8, 3, "Computer Science", has_practice=True)
peter = DisplayableMaster(2000001, "Peter", 23, 4.5, 2, "Dr. Ivanov", "Machine Learning")
vlad = DisplayableBachelor(1000002, "Vlad", 20, 3.7, 1, "Mathematics")

print("\nСценарий 1: TypedCollection, ограниченная Displayable")
print("Требуется, чтобы у объектов был метод display() -> str.\n")

coll: TypedCollection[Displayable] = TypedCollection()
coll.add(diana)
coll.add(peter)
coll.add(vlad)

print("Содержимое коллекции (display):")
for item in coll:
    print("  ", item.display())   


print("\nПоиск первого студента с GPA > 4.6:")
found = coll.find(lambda s: s.gpa > 4.6) 
print(f"  Результат: {found.display() if found else 'не найден'}")

print("\nФильтр: все студенты с курсом >= 2:")
filtered = coll.filter(lambda s: s.course >= 2)
for s in filtered:
    print("  ", s.display())

print("\nMap: преобразование в строку с именем и курсом:")
names_and_courses = coll.map(lambda s: f"{s.name} (курс {s.course})")
print("  ", names_and_courses)

print("\n" + "Сценарий 2: TypedCollection, ограниченная Scorable")
print("Требуется, чтобы у объектов был метод score() -> float.\n")

score_coll: TypedCollection[Scorable] = TypedCollection()
score_coll.add(diana)
score_coll.add(peter)
score_coll.add(vlad)

print("Оценки (score) элементов:")
for item in score_coll:
    print(f"  {item.display()}: {item.score():.2f}") 

print("\nФильтр: все с оценкой > 4.0:")
high_scorers = score_coll.filter(lambda s: s.score() > 4.0)
for s in high_scorers:
    print(f"  {s.display()} – {s.score():.2f}")

print("\nMap: извлечение списка оценок (list[float]):")
scores: list[float] = score_coll.map(lambda s: s.score())
print("  ", scores)
