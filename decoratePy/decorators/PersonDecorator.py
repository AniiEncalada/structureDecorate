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
        return self._person.task() + " and extra hours"

class PersonExtraHoursAndBonus (PersonDecorator):
    def __init__(self, person):
        super().__init__(person)
    
    def task(self): 
        return self._person.task() + " and extra hours and bonus"

class PersonBonus (PersonDecorator):
    def __init__(self, person):
        super().__init__(person)
    
    def task(self): 
        return self._person.task() + " and bonus"