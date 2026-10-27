class Student:
    def __init__(self, name):
        self.name = name

class School: 
    def __init__(self, name):
        self.name = name
        self.students = []
    def add_student(self, student):
        self.students.append(student)



school1 = School("IPSA")
s1 = Student("Keon")
s2 = Student("Denise")
school1.add_student(s1)
school1.add_student(s2)
print("School: ", {school1})
for student in school1.students:
    print(f"Name of student: {student.name}")
