class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self): # naudojma vartotojui pateikti
        return f"Person name: {self.name.upper()},\nAge: {self.age}"

    def __repr__(self): # naudojama programuotojamas
        return f"Person('{self.name}',{self.age})"

    def __eq__(self, other):
        if isinstance(other,Animal):
            print("lyginame zmogu su gyvuny")
            return self.name == other.name
        elif isinstance(other, Person):
            print("Lyginame zmogu su zmogumi")
            return self.name == other.name and self.age ==other.age

class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def __str__(self): # naudojma vartotojui pateikti
        return f"Person name: {self.name.upper()},\nAge: {self.color}"

    def __repr__(self): # naudojama programuotojamas
        return f"Person('{self.name}',{self.color})"

    def __eq__(self, other):
        return self.age == other.color


person1 = Person("Jonas",10)
person2 = Person("Jonas",10)
person3 = Animal("Jonas","juodas")
print(person1)
print(person2.name, person1.age)
print(repr(person1))


person4 = eval(repr(person2)) #eval funkcijai galime paduoti koda str formatu ir ji ta koda paleidzia
print(person2)

print(person1 == person2)
print(person2 == person3)

