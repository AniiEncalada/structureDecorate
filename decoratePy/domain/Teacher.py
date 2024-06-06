from .Person import Person

# This is the Teacher class. It is used to define the attributes and methods of a teacher. This class inherits from the Person class.
class Teacher (Person):
    def __init__(self, academicDegree, name, last_name, birth_date, dni):
        super().__init__(name, last_name, birth_date, dni)
        self.academicDegree = academicDegree

# This is the task method. It is used to define the task that will be performed by the teacher. This method is implemented by the Taskable interface. It returns a string with the name, last name, age, and charge of the teacher.      
    def task(self):
        return f"Hi, I am {self.name} {self.last_name}, I am {self.getBirthday()}, and I am a teacher with academic degree {self.academicDegree}"