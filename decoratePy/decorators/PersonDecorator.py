from domain.Person import Person

class PersonDecorator (Person):
    def __init__(self, person):
        self._person=person
    
    def task(self): 
        return self._person.task()

class PersonExtraHours (PersonDecorator):
    def __init__(self, person):
        super().__init__(person)
    
    def task(self): 
        return self._person.task() + ". I am doing extra hours"

class PersonExtraHoursAndBonus (PersonDecorator):
    def __init__(self, person):
        super().__init__(person)
    
    def task(self): 
        return self._person.task() + ". I am doing extra hours and earning bonus"

class PersonBonus (PersonDecorator):
    def __init__(self, person):
        super().__init__(person)
    
    def task(self): 
        return self._person.task() + ". I am earning bonus"