# A class is a blueprint for an object. It is called a user-defined data type because we can define different types of data within it
# for example, int, float, strings.
# We define a class named Person
class Person:
    # The constructor initializes the parameters when an object of the class is created
    # self is used to indicate that these are the attributes of this class
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    # Method to display the info of the person
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Address: {self.address}")

# Example usage of Person
# person = Person("Rimsha", 21, "123 Main St")
# person.display_info()

# We define another class Student which inherits from the Person class 
# Inheritance means accessing the methods and attributes of the parent class 
# super keyword is used to call the parent class constructor
class Student(Person):
    def __init__(self, name, age, address, student_id):
        super().__init__(name, age, address)
        self.student_id = student_id  
        self.courses = []

    def enroll_course(self, course):
        self.courses.append(course)

    def display_student_info(self):
        self.display_info()
        print(f"Student ID: {self.student_id}, Enrolled Courses: {self.courses}")

# Example usage of Student
# student = Student("Rimsha", 21, "123 Main St", 12)
# student.enroll_course("Math")
# student.enroll_course("Science")
# student.display_student_info()

class Teacher(Person):
    def __init__(self, name, age, address, employee_id):
        super().__init__(name, age, address)
        self.employee_id = employee_id
        self.subjects = []

    def assign_subject(self, subject):
        self.subjects.append(subject)

    def display_teacher_info(self):
        self.display_info()
        print(f"Employee ID: {self.employee_id}, Assigned Subjects:{self.subjects}")
# teacher = Teacher("Rimsha",21 ,"123 Main St",45) 
# teacher.assign_subject("Mathematics")
# teacher.assign_subject("Physics")
# teacher.display_teacher_info()  

class Course:
    def __init__ (self,course_name,course_code,teacher):
        self.course_name = course_name
        self.course_code = course_code
        self.teacher = teacher
    def display_course_info(self):
        print(f"Course Name: {self.course_name}, Course Code: {self.course_code}, Teacher: {self.teacher.name}")
        
teacher = Teacher("Rimsha",21 ,"123 Main St",45)  
teacher.assign_subject("Mathematics") 

course=Course("Calculus","math01",teacher)
course.display_course_info()
     
  
