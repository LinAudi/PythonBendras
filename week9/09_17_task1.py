from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def speak(self):
        pass

    def return_name(self):
        return f"Animal name: {self.name}"


class Dog(Animal):
    def speak(self):
        return "Dog says woof"


class Cat(Animal):
    def speak(self):
        return "Cat says meow"


dog = Dog("Bob")
cat = Cat("Tom")

print(dog.speak())
print(dog.return_name())
print(cat.speak())
print(cat.return_name())
