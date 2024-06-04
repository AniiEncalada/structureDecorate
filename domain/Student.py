from .Person import Person


class Student (Person): 
    def __init__(self, socialEconomicLevel, name, last_name, birth_date, dni):
        super().__init__(name, last_name, birth_date, dni)
        self.socialEconomicLevel = socialEconomicLevel

    def task(self):
        return f"Hi, I am {self.name} and I study"