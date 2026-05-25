from typing import TypeVar, Generic, Callable, Optional, Any

from typing import Protocol

class Displayable(Protocol):
    """Протокол: объект должен иметь метод display() -> str."""
    def display(self) -> str:
        ...

class Scorable(Protocol):
    """Протокол: объект должен иметь метод score() -> float."""
    def score(self) -> float:
        ...

T = TypeVar('T')
R = TypeVar('R')
D = TypeVar('D', bound=Displayable)
S = TypeVar('S', bound=Scorable)

class TypedCollection(Generic[T]):
    """Generic-коллекция, повторяющая интерфейс StudentCollection из ЛР-2."""

    def __init__(self) -> None:
        self._items: list[T] = []

    def add(self, item: T) -> None:
        """Добавляет элемент в коллекцию."""
        if item in self._items:
            raise ValueError("Элемент уже существует в коллекции")
        self._items.append(item)

    def remove(self, item: T) -> None:
        """Удаляет элемент из коллекции."""
        if item not in self._items:
            raise ValueError("Элемент не найден в коллекции")
        self._items.remove(item)

    def get_all(self) -> list[T]:
        """Возвращает копию списка всех элементов."""
        return self._items.copy()

    def find_by_id(self, item_id: int) -> Optional[T]:
        """Ищет элемент по идентификатору (предполагается наличие атрибута student_id)."""
        for item in self._items:
            if hasattr(item, 'student_id') and item.student_id == item_id:
                return item
        return None

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index: int) -> T:
        if not isinstance(index, int):
            raise TypeError("Индекс должен быть целым числом")
        if index < 0 or index >= len(self._items):
            raise IndexError("Индекс вне диапазона")
        return self._items[index]

    def remove_at(self, index: int) -> None:
        """Удаляет элемент по индексу."""
        if not isinstance(index, int):
            raise TypeError("Индекс должен быть целым числом")
        if index < 0 or index >= len(self._items):
            raise IndexError("Индекс вне диапазона")
        del self._items[index]

    def sort(self, key: Callable[[T], Any] = None, reverse: bool = False) -> None:
        """Сортирует элементы на месте."""
        self._items.sort(key=key, reverse=reverse)

    def get_active(self) -> 'TypedCollection[T]':
        """
        Возвращает новую коллекцию, содержащую только активные элементы.
        Предполагается, что элемент имеет атрибут is_active.
        """
        new_col: TypedCollection[T] = TypedCollection()
        for item in self._items:
            if hasattr(item, 'is_active') and item.is_active:
                new_col.add(item)
        return new_col

    def get_by_course(self, course: int) -> 'TypedCollection[T]':
        """
            Возвращает новую коллекцию элементов заданного курса.
            Предполагается наличие атрибута course.
        """
        new_col: TypedCollection[T] = TypedCollection()
        for item in self._items:
            if hasattr(item, 'course') and item.course == course:
                new_col.add(item)
        return new_col

    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        """Возвращает первый элемент, удовлетворяющий предикату, или None."""
        for item in self._items:
            if predicate(item):
                return item
        return None

    def filter(self, predicate: Callable[[T], bool]) -> list[T]:
        """Возвращает список элементов, удовлетворяющих предикату."""
        return [item for item in self._items if predicate(item)]

    def map(self, transform: Callable[[T], R]) -> list[R]:
        """Применяет функцию transform ко всем элементам и возвращает список результатов."""
        return [transform(item) for item in self._items]

    def __repr__(self) -> str:
        return f"TypedCollection({self._items!r})"
    
