import random
import string
from dataclasses import dataclass, field

def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k = 15))

def generate_login(name: str, surname: str) -> str:
    return name.upper()[0] + surname.lower()

@dataclass
class Student:
    """a class for holding student data"""
    name: str
    surname: str
    login: str = field(init = False) 
    id: str = field(init=False, default_factory = generate_id)
    
    def __post_init__(self):
        self.login = generate_login(self.name, self.surname)
