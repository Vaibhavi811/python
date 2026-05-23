# 1. Write a Program to implement destructor and constructors using _del_() and  
# _init_() 
class Student:
    def __init__(self,name,age):
        self.name= name
        self.age= age
        print("Constructor called.Object created for:",self.name)

    def __del__(self):
        print("Destructor called.Object deleted for:",self.name)

S1= Student("vaibhavi",19)
del S1
print("Program finished.")

