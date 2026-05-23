# Write a Program to calculate student grade using class
class Student:
    def __init__(self,name,marks):
        self.name= name
        self.marks= marks

    def cal_grade(self):
        if(self.marks>=90 and self.marks<100):
            return "A"
        elif(self.marks>=75 and self.marks<90):
            return "B"
        else:
            return "C"
        
    def display(self):
        grade= self.cal_grade()
        print("Name:",self.name)
        print("Marks:",self.marks)
        print("Grade:", grade)

s1= Student("Anant",50)
s1.display()
