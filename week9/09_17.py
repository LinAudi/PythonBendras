class Person:
    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self._age = age

    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str) -> None:
        self._name = name

    def get_age(self) -> int:
        return self._age

    def set_age(self, age: int) -> None:
        self._age = age


person = Person("Alice", 25)
# Getting an attribute:
print(person._name)  # Neturėtų būti taip daroma, nes su betarpiškai kreipiamės į "self._name" (su pabraukimu)
#
# Setting an attribute:
person._name = "Monica"  # Neturėtų būti taip daroma, nes betarpiškai kreipiamės į "self._name" (su pabraukimu)

# Getter:
#
print(person.get_name())  # "Alice"# Setter:person.set_name("Monica")  # OK


# 2PVZ


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.__name = name
        self.__age = age

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> None:
        self.__name = name

    def get_age(self) -> int:
        return self.__age

    def set_age(self, age: int) -> None:
        self.__age = age


person = Person("Alice", 25)
# Getting an attribute:
print(person.__name)  # AttributeError

# Setting an attribute:
person.__name = "Monica"  # AttributeError(?)

# Getting an attribute (with NAME MANGLING):
print(person._Person__name)

# Setting an attribute (with NAME MANGLING):
person._Person__name = "Monica"

# Getter:
print(person.get_name())  # "Alice"

# Setter:
person.set_name("Monica")  # OK


# 3PVZ
class Person:
    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self._age = age

    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str) -> None:
        self._name = name

    def get_age(self) -> int:
        return self._age

    def set_age(self, age: int) -> None:
        self._age = age


class Student(Person):

    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)

    def say_hello(self):
        print(f"Hello, my name is {self._name}")


person = Person("Alice", 25)

student = Student("Bob", 30)

student.say_hello()
