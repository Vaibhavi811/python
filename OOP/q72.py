# Write a Program to implement Getters and Setters in a class
class Student:
    def __init__(self,name,age):
        self.name= name
        self.age= age

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def set_name(self,name):
        self.name= name
        
    def set_age(self,age):
        self.age= age

S1= Student("vaibhavi",19)
print(S1.get_name())
# print(S1.get_age())
S1.set_age(20)
print(S1.get_age())