from abc import ABC, abstractmethod

class Character(ABC):
    """Character class is abstract"""

    @abstractmethod
    def __init__(self, first_name , is_alive=True):
            self.first_name = first_name
            self.is_alive = is_alive

class Stark(Character):
    """Stark Class inherits from Character abstract class"""

    def __init__(self, first_name , is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        self.is_alive = False