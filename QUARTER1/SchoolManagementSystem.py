class Person:
    def __init__(self, name):
        self.name = name
    def introduce(self):
        print("Hello! My name is ", self.name)

class Board:
    def __init__(self, color):
        self.color = color

class Classroom:
    def __init__(self):
        self.board = Board("White")

class Laptop:
    def __init__(self, brand):
        self.brand = brand

class Lab:
    def __init__(self, laptop):
        self.laptop = laptop

class Thermometer:
    def measure(self):
        print("Temperature measured.")

class Scientist:
    def conduct_experiment(self, thermometer):
        thermometer.measure()

class Student:
    def __init__(self, name, grade_level):
        self.name = name
        self.grade_level = grade_level
        self.course = []
    def enroll(self, course):
        self.course.append(course)

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
        self.student = []
    def add_student(self, student):
        self.student.append(student)
    def teach(self):
        print(self.name, " is teaching.")

class Course:
    def __init__(self, name):
        self.name = name
        self.student = []

s1 = Student("Sofia", 9)
s2 = Student("Gabriel", 10)
s3 = Student("Keon", 11)
t1 = Teacher("Majid", "Science")
c1 = Classroom()

sci = Course("Science")
math = Course("Mathematics")
eng = Course("English")

laptop1 = Laptop("Dell")
lab1 = Lab(laptop1)

scientist = Scientist()
thermometer = Thermometer()
scientist.conduct_experiment(thermometer)

s1.enroll(sci)
s1.enroll(math)
s1.enroll(eng)
s2.enroll(sci)
s2.enroll(eng)
s3.enroll(eng)

t1.add_student(s1)
t1.add_student(s2)
t1.add_student(s3)

print("Teacher Name: ", t1.name)
print("Subject: ", t1.subject)
print("Classroom: ", c1.board.color)
print()
print("List of Students: ")
for student in t1.student:
    print("Name: ", student.name)
    print("Grade Level: ", student.grade_level)
    print()

print("--" * 28)
print()
print("Course Name: ", sci.name)
print("List of Students: ")
print("Name: ", s1.name, ", Grade Level: ", s1.grade_level)
print("Name: ", s2.name, ", Grade Level: ", s2.grade_level)
print("Name: ", s3.name, ", Grade Level: ", s3.grade_level)
print()

print("--" * 28)
print()
print("Course Name: ", math.name)
print("List of Students: ")
print("Name: ", s1.name, ", Grade Level: ", s1.grade_level)
print("Name: ", s2.name, ", Grade Level: ", s2.grade_level)
print("Name: ", s3.name, ", Grade Level: ", s3.grade_level)
print()

print("--" * 28)
print()
print("Course Name: ", eng.name)
print("List of Students: ")
print("Name: ", s1.name, ", Grade Level: ", s1.grade_level)
print("Name: ", s2.name, ", Grade Level: ", s2.grade_level)
print("Name: ", s3.name, ", Grade Level: ", s3.grade_level)
print()
