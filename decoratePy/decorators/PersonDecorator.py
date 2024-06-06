from domain.Person import Person

# This is the PersonDecorator class. It is used to define the decorators that will be used to add extra functionality to the Person class. This class inherits from the Person class.
class PersonDecorator (Person):
    def __init__(self, person):
        self._person=person

# Implement the task method. This method is used to return the task of the person. It returns the task of the person that is being decorated. 
    def task(self): 
        return self._person.task()

# This is the PersonExtraHours class. It is used to define the decorator that will be used to add extra hours to the task of the person. This class inherits from the PersonDecorator class.
class PersonExtraHours (PersonDecorator):
    def __init__(self, person):
        super().__init__(person)

# Implement the task method. This method is used to return the task of the person with extra hours. It returns the task of the person that is being decorated with the message "I am doing extra hours".
    def task(self): 
        return self._person.task() + ". I am doing extra hours"

# This is the PersonExtraHoursAndBonus class. It is used to define the decorator that will be used to add extra hours and bonus to the task of the person. This class inherits from the PersonDecorator class.
class PersonExtraHoursAndBonus (PersonDecorator):
    def __init__(self, person):
        super().__init__(person)

# Implement the task method. This method is used to return the task of the person with extra hours and bonus. It returns the task of the person that is being decorated with the message "I am doing extra hours and earning bonus".   
    def task(self): 
        return self._person.task() + ". I am doing extra hours and earning bonus"

# This is the PersonBonus class. It is used to define the decorator that will be used to add bonus to the task of the person. This class inherits from the PersonDecorator class.
class PersonBonus (PersonDecorator):
    def __init__(self, person):
        super().__init__(person)

# Implement the task method. This method is used to return the task of the person with bonus. It returns the task of the person that is being decorated with the message "I am earning bonus".  
    def task(self): 
        return self._person.task() + ". I am earning bonus"