"""TASK 2"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.enrolled_courses = []
        self.grades = {}  # Dictionary to store grades for courses

    def enroll(self, course):
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)
            course.add_student(self)

    def performance_report(self, course):
        grade = self.grades.get(course)
        print(f"Student: {self.name}, Course: {course.name}, Grade: {grade}")

    def record_grade(self, course, grade):
        if course in self.enrolled_courses:
            self.grades[course] = grade


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
        self.courses = []

    def list_courses(self):
        return [course.name for course in self.courses]


class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students = []
        self.attendance = {}
        self.lesson = []
        teacher.courses.append(self)  # Add this course to the teacher's course list

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            self.attendance[student] = []

    def record_attendance(self, student, date, status):
        if student in self.students:
            self.attendance[student].append((date, status))

    def generate_report(self):
        for student in self.students:
            attendance_record = self.attendance.get(student, [])
            attendance_status = ", ".join([f"{data}: {status}" for data, status in attendance_record])
            print(f"Student: {student.name}, Attendance: {attendance_status}")

    def add_lesson(self, lesson):
        self.lesson.append(lesson)

    def get_lessons(self):
        if not self.lesson:
            print(f"No lesson in {self.name} yet.")
        else:
            for lesson in self.lesson:
                print(lesson.lesson_info())


class Lesson:
    def __init__(self, lesson_topic, date, material):
        self.lesson_topic = lesson_topic
        self.date = date
        self.material = material

    def lesson_info(self):
        return f"Lesson Topic: {self.lesson_topic}\nDate: {self.date}\nMaterials Provided: {self.material}\n"


# Example usage
math_teacher = Teacher("Mr. Smith", 40, "Math")
math_course = Course("Mathematics", math_teacher)
english_teacher = Teacher("Jonas", 54, "english")
english_course = Course("English", english_teacher)

alice = Student("Alice", 20)
bob = Student("Bob", 21)
maryte = Student("Maryte", 22)

alice.enroll(math_course)
bob.enroll(math_course)
maryte.enroll(english_course)
bob.enroll(english_course)

# Recording attendance
math_course.record_attendance(alice, "2024-01-21", "Present")
math_course.record_attendance(bob, "2024-01-21", "Absent")
english_course.record_attendance(bob, "2024-01-22", "Present")
english_course.record_attendance(maryte, "2024-01-22", "Present")


# adding lesson
lesson1 = Lesson("Algebra Basics", "2024-02-01", ["Algebra Textbook Chapter 1"])
lesson2 = Lesson("Introduction to Geometry", "2024-02-08", ["Geometry Workbook"])


# Recording grades
alice.record_grade(math_course, "A")
bob.record_grade(math_course, "B")
maryte.record_grade(english_course, "B")
bob.record_grade(english_course, "C")

# Generating reports
math_course.generate_report()  # Student: Alice, Attendance: ['2024-01-21: Present'], Student: Bob, Attendance: ['2024-01-21: Absent']
english_course.generate_report()

math_course.add_lesson(lesson1)
math_course.add_lesson(lesson2)


math_course.get_lessons()

# Testing implemented methods
alice.performance_report(math_course)  # Student: Alice, Course: Mathematics, Grade: A
bob.performance_report(math_course)
bob.performance_report(english_course)
maryte.performance_report(english_course)

print("Courses taught by Mr. Smith:", math_teacher.list_courses())  # Courses taught by Mr. Smith: ['Mathematics']
