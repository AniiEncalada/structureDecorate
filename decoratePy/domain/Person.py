from .Taskable import Taskable
from datetime import datetime

class Person (Taskable):
    def __init__(self, name, last_name, birth_date, dni):
        self.name = name
        self.last_name = last_name
        self.birth_date = birth_date
        self.dni = dni

    def getBirthday(self):
        dateBirth = datetime.strptime(self.birth_date, "%Y-%m-%d")
        return ((datetime.today() - dateBirth).days//365)

    def task(self):
        pass