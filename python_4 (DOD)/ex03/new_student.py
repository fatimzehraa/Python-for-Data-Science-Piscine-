import random
import string
from dataclasses import dataclass, field

def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k = 15))
@dataclass
class Student:
    """a class for holding student data"""
    name = str
    surname = str
    active = bool
    login = str
    id = generate_id()
    
    
student = Student(name = "Edward", surname = "agle")
print(student)