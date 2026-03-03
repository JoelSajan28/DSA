"""
What @dataclass Generates

When you write:

@dataclass
class Properties:
    name: str
    age: int
    call: str

Python generates something equivalent to:

def __init__(self, name: str, age: int, call: str):
    self.name = name
    self.age = age
    self.call = call

The order of parameters in __init__ matches the order of fields in the class definition.

Order matters.

"""
from dataclasses import dataclass

@dataclass
class Properties():
    name: str
    age: int
    call: str
    typ: str
    
class Animal():
    def __init__(self, properties: Properties):
        self._properties = properties
    
    def name(self):
        print(self._properties.name)
    
    def age(self):
        print(self._properties.age)

    def typ(self):
        print(self._properties.typ)
        return self._properties.typ
    
    @property
    def age_after_10_yrs(self):
        print(f"Age after 10 years is {self._properties.age + 10}")
    
    @age_after_10_yrs.setter
    def age_after_10_yrs(self, value: int):
        self._properties.age = self._properties.age + value

    
    @staticmethod
    def mapple_tree_lover(typ):
        if typ.lower() == "cat":
            return False
        return True
    
if __name__ == "__main__":
    kitty = Animal(Properties("Kitty", 12, "Meow", "Cat"))
    kitty.name()
    kitty.age_after_10_yrs = 10
    kitty.age()
    if not Animal.mapple_tree_lover(kitty.typ()):
        print("Cats hate maple tree")


    
