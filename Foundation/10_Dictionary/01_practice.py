"""
What is Dictionary?
Dictionary is unordered , mutable collection that store data as key -value pairs.

- Keys are unique.
- Values can be of any data type.
- Keys must be hashable.
- Dictionaries are written using curly braces `{}`.
- Dictionary items are accessed using keys, not numeric indexes.
- Python dictionaries preserve insertion order.

"""


student = {
    "name": "Ritesh",
    "age": 25
}

student["language"] = "Python"
student["age"] = 26

print(student)

#accesing value using key
# print(student["list"]) #raise error if the key is not present KeyError.

# Safe access.
print(student.get("name"))
# Ritesh
print(student.get("list")) # returns None if the key is not present.
# None

# get with default value:
print(student.get("List","list key is Not found."))
# Not found

# return all the keys of dict.
print(student.keys())

student = {
    "name": "Ritesh",
    "age": 25,
    "language": "Python"
}
for key in student:
    print(key)
# Output.
# name 
# age 
# language

student = {
    "name": "Ritesh",
    "age": 25,
    "language": "Python"
}
for key in student.values():
    print(key)
# Ritesh
# 25
# Python

student.items()
print(student.items())
# dict_items([('name', 'Ritesh'), ('age', 25), ('language', 'Python')])

for key, value in student.items():
    print(key, value)


# Adding new key-value pairs to the existing dictionary
student.update(
    {"Location":"Delhi NCR",
    "PIN code": "201007"}
)
print(student) 
# {'name': 'Ritesh', 'age': 25, 'language': 'Python', 'Location': 'Delhi NCR', 'PIN code': '201007'}

# Pop() removes a specific key-value pair and returns the removed value.
print(student.pop("name"))
print(student)


# popitem() removes and returns the last inserted key-value pair.
student = {
    "name": "Ritesh",
    "age": 25,
    "language": "Python"
}

result = student.popitem()

print(result) #('language', 'Python') #popitem() return tuple
print(student) # {"name": "Ritesh","age": 25}


result = student.clear()
print(student)
print(result)

student = {
    "name": "Ritesh",
    "age": 25,
    "language": "Python"
}

# Dict Membership 
# Membership checks the keys, not the values.
print("name" in student) #True

print("city" in student) # False

student = {
    "name": "Ritesh",
    "age": 25
} 
print("name" in student) # True
print("Ritesh" in student) # False
print("city" not in student) # True

# looping through dictionary

for key in student:
    print(key) # name  age

for value in student.values():
    print(value) # Ritesh 25

for key, val in student.items():
    print(key, val) # name ritesh age 

    

# nested dictionary

students = {
    "student1":{"name":"ritesh","Age":24, "location":"Ghaziabad"},
    "student2":{"name":"Durov","age":42,"location":"Dubai"}   
}
students["student1"]["location"] = "Delhi"
print(students.keys()) #dict_keys(['student1', 'student2'])
print(students.values()) #dict_values([{'name': 'ritesh', 'Age': 24, 'location': 'Delhi'}, {'name': 'Durov', 'age': 42, 'location': 'Dubai'}])

# Even number using dict comprehension

numbers = [23,43,2,4,53,54,21,87,42,55]
even = {number : number * number for number in numbers if number % 2 == 0}
print(even)
# {2: 4, 4: 16, 54: 2916, 42: 1764}

# Dictionary comprehension
# {x: x * x for x in numbers}

# Dictionary Conversion

# Just like Sets, we can convert between dictionary-related views and lists.

student = {
    "name": "Ritesh",
    "age": 25,
    "language": "Python"
}

keys = list(student.keys())
value = list(student.values())
print(keys) # ['name','age','language']
print(value) # ['Ritesh','25','Python']


student = {
    "name": "Ritesh",
    "age": 25
}
print(student.items()) #dict_items([('name', 'Ritesh'), ('age', 25)])

# list(dictionary.keys())   → list of keys
# list(dictionary.values()) → list of values
# list(dictionary.items())  → list of tuples

"""
🏆 Dictionary Mini-Project
🎯 Student Marks Analyzer
Your program should:

Print every student's name and marks.
Find the highest marks.
Find the lowest marks.
Calculate total marks.
Calculate average marks.
Create a dictionary containing students who scored 80+
"""

print("🎯 Student Marks Analyzer")
students = {
    "Ritesh": 85,
    "Amit": 72,
    "Rahul": 91,
    "Priya": 68,
    "Neha": 88
}
highest = 0
lowest = 100
total = 0
top_students = {}
for name , marks in students.items():
    print(name,marks)
    if marks > highest:
        highest = marks
    if marks < lowest:
        lowest = marks
    total += marks
    if marks >= 80:
        top_students[name] = marks
        
average = total / len(students)
print("Highest marks :",highest)
print("Lowest marks :",lowest)
print("Total marks :",total)
print("Average :",average)
print("Top student who score 80+ :",top_students)
