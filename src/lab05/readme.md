# lab05
## Ход мыслей при выполнении работы

При выполнении лабораторной работы основной целью было освоение передачи функций как объектов первого класса и реализация паттерна «Стратегия» без изменения существующей объектно-ориентированной модели. На основе классов студентов, созданных в ЛР‑1 (базовый класс `Student`), иерархии из ЛР‑3 (`BakalavrStudent`, `MagaStudent`), а также контейнера `StudentCollection` из ЛР‑2, необходимо было расширить последний возможностью гибкой обработки хранимых объектов.

Первым шагом стало вынесение всех алгоритмов сортировки, фильтрации и преобразований в отдельный модуль `strategies.py`. Это позволило реализовать логику обработки в виде отдельных функций и классов, которые можно взаимозаменять без модификации кода коллекции. В результате каждая стратегия представляет собой функцию с сигнатурой `(Student) -> ...`, что делает возможным передачу их в методы `sort_by`, `filter_by`, `apply` и встроенные функции `map`, `filter`, `sorted`.

Вторым важным решением было добавление в `StudentCollection` методов, поддерживающих «цепочки» операций. Метод `sort_by` возвращает `self` после сортировки, метод `filter_by` создаёт новый экземпляр коллекции с отфильтрованными элементами, а метод `apply` применяет побочное действие к каждому элементу и также возвращает `self`. Это позволяет записывать последовательность операций в виде единого выражения.

Для демонстрации гибкости использованы три сценария: полная цепочка обработки, замена стратегий без изменения кода коллекции и применение callable-объектов как стратегий. Также задействованы фабрика функций (для создания настраиваемых фильтров) и лямбды для простых однострочных условий. Все функции и классы в `strategies.py` снабжены docstring, что упрощает их сопровождение и переиспользование.

## Сценарии 

### Сценарий 1 – Цепочка filter → sort → apply
1. Исходная коллекция содержит студентов – бакалавров и магистров.
2. С помощью `filter_by(is_excellent)` отбираются только студенты с GPA ≥ 4.5 (отличники).
3. Полученная коллекция сортируется по имени с помощью `sort_by(by_name)`.
4. К каждому отобранному студенту применяется `apply(promote_student)`, которая повышает курс (если это возможно).
5. Каждый промежуточный результат выводится на экран. Исходная коллекция остаётся неизменной структурно, так как `filter_by` создаёт новый экземпляр.

## Вывод
```txt
Сценарий 1: цепочка filter → sort → apply

--- Исходная коллекция ---
1. Student: Alice
Age: 20
GPA: 4.80
Course: 2
Status: Active
Specialization: Computer Science
Practice: Пройдена
2. Student: Bob
Age: 22
GPA: 3.90
Course: 1
Status: Active
Supervisor: Dr. Smith
Thesis topic: Artificial Intelligence
3. Student: Charlie
Age: 21
GPA: 3.20
Course: 3
Status: Active
Specialization: Mathematics
Practice: Не пройдена
4. Student: Diana
Age: 23
GPA: 4.90
Course: 2
Status: Active
Supervisor: Dr. Brown
Thesis topic: Robotics
5. Student: Eve
Age: 19
GPA: 4.50
Course: 1
Status: Active
Specialization: Physics
Practice: Пройдена

--- После filter(is_excellent) → sort(by_name) → apply(promote_student) ---
1. Student: Alice
Age: 20
GPA: 4.80
Course: 3
Status: Active
Specialization: Computer Science
Practice: Пройдена
2. Student: Diana
Age: 23
GPA: 4.90
Course: 2
Status: Active
Supervisor: Dr. Brown
Thesis topic: Robotics
3. Student: Eve
Age: 19
GPA: 4.50
Course: 2
Status: Active
Specialization: Physics
Practice: Пройдена

Исходная коллекция (без изменений структуры):
Alice 4.8 course: 3
Bob 3.9 course: 1
Charlie 3.2 course: 3
Diana 4.9 course: 2
Eve 4.5 course: 2
```

### Сценарий 2 – Замена стратегий без изменения кода коллекции
- Одна и та же коллекция последовательно сортируется тремя разными key-функциями: `by_name`, `by_gpa_desc` (сортировка по убыванию GPA) и `by_course_and_name` (сначала по курсу, затем по имени).
- Затем выполняется фильтрация с использованием именованного предиката `is_master_student` и анонимной лямбда-функции `lambda s: s.gpa > 4.0`. В обоих случаях вызывается один и тот же метод `filter_by`, который не зависит от конкретной логики проверки.
- На этом примере показано, что новый алгоритм можно передать в коллекцию простой заменой аргумента без изменения её реализации.

## Вывод
```txt
Сценарий 2: замена стратегий сортировки
Сортировка по имени:

--- Результат сортировки by_name ---
1. Student: Alice
Age: 20
GPA: 4.80
Course: 3
Status: Active
Specialization: Computer Science
Practice: Пройдена
2. Student: Bob
Age: 22
GPA: 3.90
Course: 1
Status: Active
Supervisor: Dr. Smith
Thesis topic: Artificial Intelligence
3. Student: Charlie
Age: 21
GPA: 3.20
Course: 3
Status: Active
Specialization: Mathematics
Practice: Не пройдена
4. Student: Diana
Age: 23
GPA: 4.90
Course: 2
Status: Active
Supervisor: Dr. Brown
Thesis topic: Robotics
5. Student: Eve
Age: 19
GPA: 4.50
Course: 2
Status: Active
Specialization: Physics
Practice: Пройдена

Сортировка по убыванию GPA (шкала 0-5):

--- Результат сортировки by_gpa_desc ---
1. Student: Diana
Age: 23
GPA: 4.90
Course: 2
Status: Active
Supervisor: Dr. Brown
Thesis topic: Robotics
2. Student: Alice
Age: 20
GPA: 4.80
Course: 3
Status: Active
Specialization: Computer Science
Practice: Пройдена
3. Student: Eve
Age: 19
GPA: 4.50
Course: 2
Status: Active
Specialization: Physics
Practice: Пройдена
4. Student: Bob
Age: 22
GPA: 3.90
Course: 1
Status: Active
Supervisor: Dr. Smith
Thesis topic: Artificial Intelligence
5. Student: Charlie
Age: 21
GPA: 3.20
Course: 3
Status: Active
Specialization: Mathematics
Practice: Не пройдена

Сортировка по курсу и имени:

--- Результат сортировки by_course_and_name ---
1. Student: Bob
Age: 22
GPA: 3.90
Course: 1
Status: Active
Supervisor: Dr. Smith
Thesis topic: Artificial Intelligence
2. Student: Diana
Age: 23
GPA: 4.90
Course: 2
Status: Active
Supervisor: Dr. Brown
Thesis topic: Robotics
3. Student: Eve
Age: 19
GPA: 4.50
Course: 2
Status: Active
Specialization: Physics
Practice: Пройдена
4. Student: Alice
Age: 20
GPA: 4.80
Course: 3
Status: Active
Specialization: Computer Science
Practice: Пройдена
5. Student: Charlie
Age: 21
GPA: 3.20
Course: 3
Status: Active
Specialization: Mathematics
Practice: Не пройдена

Фильтр: только магистранты:

--- Только магистранты ---
1. Student: Bob
Age: 22
GPA: 3.90
Course: 1
Status: Active
Supervisor: Dr. Smith
Thesis topic: Artificial Intelligence
2. Student: Diana
Age: 23
GPA: 4.90
Course: 2
Status: Active
Supervisor: Dr. Brown
Thesis topic: Robotics

Тот же метод filter_by, но с lambda – только студенты с GPA > 4.0:

--- GPA > 4.0 ---
1. Student: Diana
Age: 23
GPA: 4.90
Course: 2
Status: Active
Supervisor: Dr. Brown
Thesis topic: Robotics
2. Student: Eve
Age: 19
GPA: 4.50
Course: 2
Status: Active
Specialization: Physics
Practice: Пройдена
3. Student: Alice
Age: 20
GPA: 4.80
Course: 3
Status: Active
Specialization: Computer Science
Practice: Пройдена
```

### Сценарий 3 – Callable-объекты и фабрика функций
- В начале создаётся свежая коллекция на основе исходных данных. Выводится текущий GPA студентов.
- Создаётся экземпляр класса `GpaBooster(0.2)`, который реализует метод `__call__`. Он передаётся в `apply`, что увеличивает GPA каждого студента на 0.2 (но не более 5.0). Результат отображается.
- Затем другой callable-объект – `StudentFormatter` – используется совместно с `map()` для преобразования элементов коллекции в строки по заданному шаблону.
- В конце демонстрируется фабрика функций `make_min_gpa_filter(4.0)`, возвращающая сконфигурированный предикат, который применяется через `filter_by` для отбора студентов с баллом не ниже 4.0.

Таким образом, сценарии последовательно показывают: (1) объединение нескольких стратегий в единую цепочку, (2) независимость кода коллекции от конкретной стратегии и (3) работу callable-объектов и фабрик как полноценных стратегий.

## Вывод 
```txt
Сценарий 3: Callable-объекты
GPA до применения GpaBooster:
  Alice: 4.8
  Bob: 3.9
  Charlie: 3.2
  Diana: 4.9
  Eve: 4.5

GPA после col3.apply(GpaBooster(0.2)):
  Alice: 5.0
  Bob: 4.1
  Charlie: 3.4000000000000004
  Diana: 5.0
  Eve: 4.7

Результат map(StudentFormatter):
   Студент Alice, балл 5.0, курс 3 (Active)
   Студент Bob, балл 4.1, курс 1 (Active)
   Студент Charlie, балл 3.4000000000000004, курс 3 (Active)
   Студент Diana, балл 5.0, курс 2 (Active)
   Студент Eve, балл 4.7, курс 2 (Active)

Фабрика функций: фильтр по минимальному GPA = 4.0

--- Студенты с GPA >= 4.0 (после буста) ---
1. Student: Alice
Age: 20
GPA: 5.00
Course: 3
Status: Active
Specialization: Computer Science
Practice: Пройдена
2. Student: Bob
Age: 22
GPA: 4.10
Course: 1
Status: Active
Supervisor: Dr. Smith
Thesis topic: Artificial Intelligence
3. Student: Diana
Age: 23
GPA: 5.00
Course: 2
Status: Active
Supervisor: Dr. Brown
Thesis topic: Robotics
4. Student: Eve
Age: 19
GPA: 4.70
Course: 2
Status: Active
Specialization: Physics
Practice: Пройдена
```

## Заключение

В ходе выполнения лабораторной работы были достигнуты следующие результаты:

- Реализована передача функций как аргументов в методы `sort_by`, `filter_by`, `apply` и в функции высшего порядка (`map`, `filter`, `sorted`).
- Показано применение паттерна «Стратегия», где алгоритмы вынесены в отдельные функции и классы, а коллекция остаётся неизменной при смене поведения.
- Освоена техника создания цепочечного API: методы возвращают `self` или новый объект, позволяя собирать последовательности операций.
- Изучены lambda-выражения, фабрики функций и callable-объекты как способы создания гибких и настраиваемых стратегий.
- Продемонстрирована интеграция функционального стиля с ранее созданными классами предметной области и контейнером.

Полученные навыки позволяют легко расширять поведение классов в будущем, добавляя новые стратегии обработки без нарушения принципа открытости/закрытости кода.