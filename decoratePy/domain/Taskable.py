from abc import ABC, abstractmethod

# This is the Taskable interface. It is used to define the task method that will be implemented by the classes that implement this interface.
class Taskable (ABC):
    @abstractmethod 
    def task(self):
        pass

