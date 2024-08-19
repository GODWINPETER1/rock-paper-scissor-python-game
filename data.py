class Person():
    
    def __init__(self , name , age):
        self.name = name
        self.age = age
    
    def  introduce(self):
        print(f"Hello my name is {self.name} and i am {self.age} years old.")
    

class Student(Person):
    
    def __init__(self, name, age , student_id):
        super().__init__(name, age)
        self.student_id = student_id
    
    def introduce(self):
        print(f"My name is {self.name} , a student with id number {self.student_id}")
    
class Teacher(Person):
    
    def __init__(self, name, age , subject):
        super().__init__(name, age)
        self.subject = subject
    
    def introduce(self):
        print(f"Hello , i am {self.name} , a teacher of {self.subject}.")

# Demostration polytmorphism
def intoduce_person(person):
    person.introduce()
    
student = Student("Godwin" , 40 , 23839494)
teacher = Teacher("Pendo" , 50 , "Math")

intoduce_person(student)
intoduce_person(teacher)
