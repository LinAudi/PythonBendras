# class Rectangle:
#     def __init__(self, width: float, height: float) -> None:
#         self.width = width
#         self.height = height
#     def area(self) -> float:
#         return self.width * self.height
#     @classmethod
#     def from_square(cls, side_length: float) -> 'Rectangle':
#         return cls(side_length, side_length) # 2.0, 2.0
# rectangle1 = Rectangle(3.0, 4.0)
# # rectangle2 = Rectangle(2.0, 2.0)
# rectangle2 = Rectangle.from_square(2.0)
# print(rectangle1.area())  # 12.0
# print(rectangle2.area())  # 4.0










# class Car:
#     total_cars_sold: int = 0
#
#     def __init__(self, make: str, model: str):
#         self.make = make
#         self.model = model
#         Car.total_cars_sold += 1
#
#     @classmethod
#     def get_total_cars_sold(cls) -> int:
#         return cls.total_cars_sold
#
# car1: Car = Car('Toyota', 'Camry')
# car2: Car = Car('Honda', 'Civic')
#
# print(Car.get_total_cars_sold())  # 2
#
#
#
#
#
class Student:
    all_students: list['Student'] = []

    def __init__(self, name: str, grade: float):
        self.name = name
        self.grade = grade
        Student.all_students.append(self)

    @classmethod
    def get_highest_grade(cls) -> 'Student':
        return max(cls.all_students, key=lambda student: student.grade)

    @classmethod
    def get_lowest_grade(cls) -> 'Student':
        return min(cls.all_students, key=lambda student: student.grade)

student1: Student = Student('John', 90)
student2: Student = Student('Jane', 95)
student3: Student = Student('Alice', 80)

print(f"BEST STUDENT: {Student.get_highest_grade().name}")  # Jane
print(Student.get_lowest_grade().name)  # Alice




