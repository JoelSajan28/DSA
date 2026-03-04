"""
Classes

Staff(Doc/Non Doc) - > Salary
Patients -> Disease
Patients -> Payment

"""


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["age"])

    @classmethod
    def guest(cls):
        return cls("Guest", 0)
    
data = {"name": "Joel", "age": 26}

u1 = User.from_dict(data)
u2 = User.guest()

print(u1.name, u1.age)
print(u2.name, u2.age)