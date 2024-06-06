from .Person import Person

# This is the AdministrativePersonal class. It is used to define the attributes and methods of an administrative personal. This class inherits from the Person class.
class AdministrativePersonal (Person):
    def __init__(self, charge, name, last_name, birth_date, dni):
        super().__init__(name, last_name, birth_date, dni)
        self.charge = charge

# This is the task method. It is used to define the task that will be performed by the administrative personal. This method is implemented by the Taskable interface. It returns a string with the name, last name, age, and charge of the administrative personal.
    def task(self):
        return f"Hi, I am {self.name} {self.last_name}, I am {self.getBirthday()}, I am Administrative Personal and my charge is {self.charge}"    