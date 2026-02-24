class Student:
    university_name = 'НИТУ МИСиС'
    
    def __init__(self, name: str, age: int, gpa: float, course: int):
        self._validate_name(name)
        self._validate_age(age)
        self._validate_gpa(gpa)
        self._validate_course(course)

        self._name = name
        self._age = age
        self._gpa = gpa
        self._course = course
        self._is_active = True

        # validstion metods

    def _validate_name(self, name):
        if not isinstance(name, str):
            raise TypeError('Name must be tupe string')
        if not name.strip():
            raise ValueError("Name cannot be empty")
        
    def _validate_age(self, age):
        if not isinstance(age, int):
            raise TypeError('Age must be tupe integer')
        if age < 16:
            raise ValueError('Studen must be at least 16 years')
        
    def _validate_gpa(self, gpa):
        if not isinstance(gpa, (int, float)):
            raise TypeError('Gpa must be tupe ineger or float')
        if not 0 <= gpa <= 5:
            raise ValueError('Gpa must be range from 0 to 5')
        
    def _validate_course(self, course):
        if not isinstance(course, int):
            raise TypeError('Course must be tupe integer')
        if not 1 <= course <= 6:
            raise ValueError('Course must be range form 1 to 6')
        
    @property
    def name(self):
        return self._name

    @property
    def gpa(self):
        return self._gpa

    @gpa.setter
    def gpa(self, value):
        self._validate_gpa(value)
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

    def expel(self):
        self._is_active = False

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
           





        