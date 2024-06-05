# person_age.py
from person_base import Person

class Person(Person):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name)
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("Invalid age")
        self._age = age