from .Person import Person

class Teacher (Person):
    def __init__(self, academicDegree, name, last_name, birth_date, dni):
        super().__init__(name, last_name, birth_date, dni)
        self.academicDegree = academicDegree
        
    def task(self):
        return f"Hi, I am {self.name} and I Teach"