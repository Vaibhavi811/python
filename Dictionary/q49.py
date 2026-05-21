# Write a program to demonstrate working with dictionaries in python
student= {
    "name": "vaibhavi",
    "age":19,
    "marks": 89    
}

print("name:", student["name"])
student["marks"]= 96
student.pop("age")
student["course"]= "Btech cse"

for key,value in student.items():
    print(key,":", value)