from .Person import Person

# This is the Student class. It is used to define the attributes and methods of a student. This class inherits from the Person class.
class Student (Person): 
    def __init__(self, socialEconomicLevel, name, last_name, birth_date, dni):
        super().__init__(name, last_name, birth_date, dni)
        self.socialEconomicLevel = socialEconomicLevel

# This is the task method. It is used to define the task that will be performed by the student. This method is implemented by the Taskable interface. It returns a string with the name, last name, age, and charge of the student.
    def task(self):
        return f"Hi, I am {self.name} {self.last_name}, I am {self.getBirthday()} and I am student"