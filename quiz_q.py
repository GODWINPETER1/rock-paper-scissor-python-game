print("To master object oriented programming....");

class Person:
    
    def __init__(self , name , age):
        self.name = name
        self.__age = age # I made this attribute private 
    
    def introduce(self):
        print(f"My name is {self.name} and i am {self.age} years old.")
        
    # getter method
    def get_age(self):
        return self.__age
    
    # setter method for age
    def set_age(self , age):
        
        if age > 0:
            self.__age = age
        else:
            print("Enter a valid age.")

new_object = Person("Godwin" , 30)
new_object.set_age(45)

# Encapsulation

# Inheritance . a child class inheritance the parent attributes and method

class Student(Person):
    
    def __init__(self, name, age , student_id):
        super().__init__(name, age)
        self.student_id = student_id
    
    
    
    def study(self):
        
        print(f"{self.name} with an age of {self.get_age()} and with id number {self.student_id}")


obj_num_one = Student("Peter" , 40 , 1828388484)
print(obj_num_one.study())