from abc import ABC, abstractmethod


class Shapes(ABC):
    def __init__(self, name: str, sides: int):
        self.name = name
        self.sides = sides

    @abstractmethod
    def area(self):
        raise NotImplementedError


class Rectangle(Shapes):
    def __init__(self, width: float, height: float):
        super().__init__("Rectangle", 4)
        self.width = width
        self.height = height

    def area(self):
        return f"Area of {self.name} = {self.width * self.height}"


class Square(Shapes):
    def __init__(self, side_length: float):
        super().__init__("Kvadratas", 4)
        self.side_length = side_length

    def area(self):
        return f"Area of {self.name} = {self.side_length**2}"


rectangle = Rectangle(50, 20)
square = Square(50)

print(rectangle.area())
print(square.area())
