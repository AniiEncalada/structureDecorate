from abc import ABC, abstractmethod

class Taskable (ABC):
    @abstractmethod 
    def task(self):
        pass

