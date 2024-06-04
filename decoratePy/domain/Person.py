from .Taskable import Taskable

class Person (Taskable):
    def __init__(self, name, last_name, birth_date, dni):
        self.name = name
        self.last_name = last_name
        self.birth_date = birth_date
        self.dni = dni

    def task(self):
        pass