from .Taskable import Taskable
from datetime import datetime

# This is the Person class. It is used to define the attributes and methods of a person. This is the parent class of the AdministrativePersonal, Teacher and Student classes.
class Person (Taskable):
    def __init__(self, name, last_name, birth_date, dni):
        self.name = name
        self.last_name = last_name
        self.birth_date = birth_date
        self.dni = dni

# With this method, we can get the age of the person. The method receives the birth_date attribute and returns the age of the person. This uses the datetime class from the datetime module to calculate the age of the person. It uses the strptime method to convert the birth_date attribute to a datetime object. It uses the today method to get the current date. It uses the days attribute to get the number of days between the current date and the birth date. It uses the // operator to divide the number of days by 365 to get the age of the person. It returns the age of the person.
    def getBirthday(self):
        dateBirth = datetime.strptime(self.birth_date, "%Y-%m-%d")
        return ((datetime.today() - dateBirth).days//365)

# This is the task method. It is used to define the task that will be performed by the person. This method is implemented by the Taskable interface. It returns a string with the name, last name, age, and charge of the person. Here we have an abstract method that will be implemented by the classes that inherit from the Person class.
    def task(self):
        pass