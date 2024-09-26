class Animal:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def print_hi(self):
        print("Hello everyone!")


class Dog(Animal):
    def __init__(self, name, breed, barker):
        super().__init__(name, breed)
        self.barker = barker


class Cat(Animal):
    def __init__(self, name, color, breed):
        super().__init__(name, breed)
        self.color = color


d = Dog("Ogis", "Auksaspalvis", False)
c = Cat("Tomas", "Melynas", "Melynspalvis")

d2 = Dog("Arcis", "Auksaspalvis", True)


print(d.breed)
print(c.breed)
c.print_hi()

print("Is Barker:", d.barker)
print(d2.barker)
