"""
A list in Python is a built-in, ordered,
mutable data structure used to store multiple values,
including values of different data types, in a single collection.

==================================================================

A list is an ordered and mutable, collection in python.
that can store multiple elements of different data types.
It is created using square brackets [] seperated with commaa (,) 

Since list are mutable. we can change the value after list creation.
syntax : 
lst = [23,32,93,23]

"""


lst =[ "Python", "Django", "FastAPI" ,"Docker"]
print(lst)
print(lst[1])
print(lst[-1])

# Modifying a List
lst[1] = "Flask"
print(lst)

# Adding Items — append() = put something at the end of the queue.
lst.append("Django")
print("Append Item :",lst)

# Adding items on specific position .insert() is used when you want to add an item at a specific position, not necessarily at the end.
lst1 = ["Python", "Flask", "Docker"]
lst1.insert(2,"Django")
print(lst1)

# 🧠 Syntax
# list.insert(index, value)
# append → "Put it at the back." 🚶

# insert → "Put it exactly here." 📍

# remove() removes by value, not by index.

lst2 = ["Python","C++","JAVA","JAVASCRIPT"]
lst2.remove("C++")
print(lst2)

# pop() removes an item using its index and also returns the removed item.

lst3 = lst2 #['Python', 'JAVA', 'JAVASCRIPT']
lst3.pop(0) # ['JAVA', 'JAVASCRIPT']
print("Pop Item :",lst3)
# remove("Java") → remove by VALUE = → tell Python WHAT to remove
# pop(1)         → remove by INDEX  = pop() → tell Python WHERE to remove
# removes and gives you the removed item.

# clear() removes all items from a list.
lst = ["Python", "Java", "C++"]

lst.clear()

print(lst)

# del is used to delete an item using its index.
lst = ["Python", "Java", "C++", "Go"]
del lst[1]
print("DEL",lst)
# remove item

# extend() → add multiple items to the end

lst= ["Python", "Java", "C++", "Go"]
lst.extend(["Django","flask","Crow","GO-Routine"])
print(lst) # ['Python', 'Java', 'C++', 'Go', 'Django', 'flask', 'Crow', 'GO-Routine']


# append() is used to add one item to the end of a list.
lst = ["A", "B"]

lst.append(["C", "D"])
print(lst) # ["A","B",["C","D"]]

# index() tells you the position/index of a value in a list.
lst = ["Python", "Django", "FastAPI", "Docker"]

# position = lst.index("FastAPI")
position = lst.index("Docker")

print(position)

# count()
lst = ["Python", "Django", "FastAPI", "Docker","Python"]
count = lst.count("Python")
print(count)

# sort() arranges the items in a list in ascending order by default.
numbers = [5, 2, 8, 1, 3]

numbers.sort()

print(numbers)

name = ["Ritesh","Sahil","Abhishek"]
name.sort()
print(name) # ['Abhishek', 'Ritesh', 'Sahil']

# List .reverse() reverses the order of items in the original list.
# sort()     → arrange items
# reverse()  → reverse current order
lst = ["A", "B", "C", "D"]
lst.reverse()
print(lst)

# copy() creates a new list containing the same items.

old_lst = ["A","B","C","D","E"]
new_lst = old_lst.copy()
new_lst.append(["X","Y","Z"]) 
new_lst.extend(["G","H","I"])
new_lst.insert(6,"Z")

print("Old List :",old_lst)
print("New List :",new_lst)


languages = ["Python", "Django"]
languages.append(["FastAPI", "Docker"])
print(languages) # ["Python", "Django",["FastAPI", "Docker"]]
# Because append() adds its argument as one item.

languages = ["Python", "FastAPI", "Docker"]

languages.insert(1, "Django")# add item on specific index 

print(languages) # ["Python", "Django","FastAPI", "Docker"]

# ==========================
lst = ["Python", "Java", "C++", "Go"]
lst.remove("C++") # Remove uses value,not index
# remove(value) → removes the first matching value from the list.
print(lst) 
# ["Python", "Java", "Go"]


lst = ["Python", "Java", "C++"]
removed = lst.pop(2) # removes an item using its index and return the removed item 
print(removed) #--> "C++"
print("After removed :",lst) # --> ["Python","Java"]

# remove() removes an item by its value.
# pop() removes an item by its index and returns the removed item.

lst = ["A", "B", "C"]
lst.clear() # remove all item from the list.
print("Empty list :",lst) # return empty list..


lst = ["A", "B"]
lst.extend(["C", "D"])# add items to the end of a list
print(lst) #["A", "B","C","D"]

# Inedx() --> return the index/position of the item.
# index() returns the first occurrence.

lst= ["A", "B", "C", "D", "C"]
position = lst.index("C") # 2
print(position)

# Count()

lst = ["Python", "Java", "Python", "C++", "Python"]
print(lst.count("Python")) # 3


# sort()
# sort() arranges the items of a list in ascending order by default.
numbers = [10, 3, 7, 1, 5]
numbers.sort() #[1,3,5,7,10]
print(numbers)

# reverse()
# reverse() reverses the current order of the list.
lst = ["Python", "Django", "FastAPI", "Docker"]
lst.reverse()
print(lst) # ["Docker","FastAPI","Django","Python"]


lst = ["A", "B", "C", "D"]
lst.reverse()
print(lst) # ["D","c","B","A"]


"""
============List Slicing================
Syntax :
[start:stop:step]
lst = ["Python","Django","FastAPI","Flask","C++","Crow","Golang","Go-Routine"]
print(lst[1:7:2]) # ["Django", "Flask","Crow",]
"""
lst = ["Python","Django","FastAPI","Flask","C++","Crow","Golang","Go-Routine"]
print(lst[1:7:2]) 


lst = ["A", "B", "C", "D", "E", "F"]

print(lst[::-1]) # ["F","E","D","C","B","A",]

# List Length — len()
lst = ["Python", "Django", "FastAPI", "Docker"]
print(len(lst)) # 4

lst = ["A", "B", "C", "D", "E"]

print(len(lst)) # 5

# Membership — in and not in
# You can check whether an item exists in a list using in.

languages = ["Python", "Java", "C++","Golang","Elixir"]

print("Python" in languages) # True
print("Django" not in languages) # True
print("Flask" in languages) # False

lst = ["Python", "Django", "FastAPI"]

print("Django" in lst) # True
print("Java" not in lst) # True

# Looping Through a List
languages = ["Python", "Django", "FastAPI", "Docker"]

for language in languages:
    print(language,end= " * ") #Python * Django * FastAPI * Docker *

# Modifying List Items with a Loop


numbers = [10, 20, 30, 40]
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
print(numbers)

# enumerate()
# Python gives us a cleaner way to get both index and value
languages = ["Python", "Django", "FastAPI"]

for index, language in enumerate(languages):
    print(index, language)


fruits = ["Apple", "Banana", "Mango"]

for index, fruit in enumerate(fruits):
    print(index, fruit) 
# Output:
# 0 Apple
# 1 Banana
# 2 Mango


# Nested List
students = [
    ["Ritesh", 86],
    ["Abhishek", 99],
    ["Sahil", 100],
]
for name, marks in students:
    print(name,marks)  #"Take two values from each inner list and assign them to name and marks."


data = [
    ["Python", 3],
    ["Django", 5],
    ["FastAPI", 4]
]

for language, years in data:
    print(language, years) 
# sequence unpacking.


# Nested List + enumerate()
students = [
    ["Ritesh", 85],
    ["Amit", 90],
    ["Rahul", 78]
]
for index, (name, marks) in enumerate(students):
    print(index, name, marks)

# 
languages = [
    ["Python", "Backend"],
    ["JavaScript", "Frontend"],
    ["SQL", "Database"]
]

for index, (language , use) in enumerate(languages):
    print(index, language, use)
# Output:
# 0 Python Backend
# 1 JavaScript Frontend
# 2 SQL Database




"""
Q1. What's the difference between append() and extend()?
A1.extend() add multiple item individually at the end of the list.
append() add one item in the end of the list.
Q2. What's the difference between remove() and pop()?
A2.remove() remove item by value. not index.
pop() remove item using index. and return removed item.
Q3. What does enumerate() give you when looping through a list?
A3.index , inner list


enumerate() gives us both the index and the item while looping


"""

languages = ["Python", "Django", "FastAPI", "Docker","Docker"]

position = languages.index("Docker")

print(position)
# 3

## Unpacking in a Loop
students = [
    ["Ritesh", 85],
    ["Amit", 72],
    ["Rahul", 91]
]

for name, marks in students:
    print(name, marks)

# Ritesh 85
# Amit 72
# Rahul 91

data = [["Python", "Backend"],["JavaScript", "Frontend"]]
language, category = data 

print(language)
print(category)
# ['Python', 'Backend']
# ['JavaScript', 'Frontend']

# 🟢 Section 11: List Comprehension
# A list comprehension is a short way to create a new list from an existing iterable.

# Normal way:

# Square of numbers:

numbers = [12,2,3,5,2,19]
square = []
for number in numbers:
    square.append(number * number)
print(square)

# using list comprehension
numbers = [1,2,3,5,7,5,3,9]
square = [number * number for number in numbers]
print(square)

# [expression for item in iterable]

nums = [3,5,6,7,4,7,3,9]
square = [num * num for num in nums]
print(square)

# ============================

numbers = [1,3,4,56,78,64,77,23]
double = [x*2 for x in numbers]
print(double)

# Cube

numbers = [3,5,6,8,6,8,9]
cube = [x * 3 for x in numbers]
print(cube)

# Even number

numbers = [3,5,6,8,6,8,9]
even = []

for number in numbers:
    if number % 2 == 0:
        even.append(number)
print(even)

# using list comprehension

numbers = [2,3,4,5,6,78,97,5,45,34,39,57]
even = [number for number in numbers if number % 2 == 0]
print(even)

numbers = [3,6,8,9,32,45,32,13,21]
odd = [number for number in numbers if number % 2 != 0]
print("Odd number is :",odd)

# Create a list containing only numbers greater than 4 using list comprehension.


numbers = [1, 2, 3, 4, 5, 6, 7, 8]
greater = [number for number in numbers if number > 4 ]
print(greater)

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

greater = [number for number in numbers if number > 5]
print(greater)