from .Person import Person

class AdministrativePersonal (Person):
    def __init__(self, charge, name, last_name, birth_date, dni):
        super().__init__(name, last_name, birth_date, dni)
        self.charge = charge

    def task(self):
        return f"Hi, I am {self.name} and I Work"    