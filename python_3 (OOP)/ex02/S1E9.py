from abc import ABC, abstractmethod

class Character(ABC):
    """Abstract class for a character, alive or dead.
    this class can't be instanciated"""
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """abstract method to initialize the character, does nothing but can be overriden"""
        self.first_name = first_name
        self.is_alive = is_alive

class Stark(Character):
    """concrete class for a Stark character, inherits from Character"""
    def __init__(self, first_name=None, is_alive=True):
        """initialize the Stark character"""
        self.first_name = first_name
        self.is_alive = is_alive
        
    def is_alive(self):
        """check if the character is alive"""
        return self.is_alive
    def die(self):
        """change the status of the character to dead"""
        self.is_alive = False
        