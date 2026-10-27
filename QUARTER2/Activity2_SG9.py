#Single Inheritance
class Adult:
    def __init__(self, name, job):
        self._name = name
        self._job = job

    @property
    def job(self):
       pass

    @property
    def name(self):
        pass

    @job.setter
    def job(self, new_job):
        if new_job == "Unemployed" or new_job == "":
            print("You need a job")
        else:
            self._job = new_job

    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("You need a name.")
        else:
            self._name = new_name

class Parent(Adult): 
    def __init__(self, name, job, child_name):
        super().__init__(name, job)
        self._child_name = child_name

    @property
    def child_name(self):
        pass

    @child_name.setter
    def child_name(self, new_child_name):
        if new_child_name == "":
            print("Name your child")
        else: 
            self._child_name = new_child_name

adult1 = Parent("Gabriel", "Unemployed", "No Child")
input_name = str(input("Enter new child name: "))
adult1.child_name = input_name
print (f"Your child's name is now {adult1.child_name}")

input_job = str(input("Enter new job: "))
adult1.job = input_job

#Multilevel Inheritance
class Student(Parent):
    def __init__(self, college, age, course, job, name, child_name):
        super().__init__(name, job, child_name)
        self._college = college
        self._age = age
        self._course = course

    def display_info(self):
        print(f"College: {self._college}")
        print(f"Age: {self._age}")
        print(f"Course: {self._course}")

    @property
    def college(self):
        pass

    @property
    def age(self):
        pass

    @property
    def course(self):
        pass
    
    @college.setter
    def college(self, new_college):
        if new_college == "":
            print("You need to choose your college.")
        else:
            self._college = new_college

    @course.setter
    def course(self, new_course):
        if new_course == "":
            print("You need to choose your course.")
        else:
            self._course = new_course

student1 = Student("Not Enrolled", 20, "No Course", "Unemployed", "Dennis", "Helen")
input_college = str(input("Enter new college: "))
student1.college = input_college
input_course = str(input("Enter new course: "))
student1.course = input_course
student1.display_info()

#Hierarchical Inheritance
class Teacher(Adult):
    def __init__(self, name, job, subject):
        super().__init__(name, job)
        self._subject = subject

    def display_info(self):
        print(f"Name: {self._name}")
        print(f"Job: {self._job}")
        print(f"Subject: {self._subject}")

    @property
    def subject(self):
        pass 

    @subject.setter
    def subject(self, new_subject):
        if new_subject == "":
            print("In order to teach, you need a subject.")
        else:
            self._subject = new_subject

teacher1 = Teacher("Mr. Orsolino", "Teacher", "Math")
