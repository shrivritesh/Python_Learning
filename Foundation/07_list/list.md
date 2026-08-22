# Python Lists

## 1. What is a List?
list is an ordered , mutable collection in python.
which is used to store elements, including elements of different data types.
It is created using square brackets [] with elements seperated by comma.

## Syntax
lst = [ 1 , 3, "names",True]
lst[-3] # 3



## 2. Creating a List

A list is created using square brackets `[]`.

### Examples

```python
nums = [1, 23, 22.0, 23, 1]

languages = ["Python", "Django", "FastAPI"]
mixed = ["Ritesh", 20, 22.5, True]
mix = ["Ritesh",20,False]
name = ["A","B","C"]
nums = [1,2,4,3.0,23,12]

```
nums = [1,2,4,3.0,23,12]
print(len(nums)) # total elements in nums #6

## 3.LIST Indexing 
Indexing means accessing an element from a list using its specific index.

Python uses zero-based indexing, which means the first element has index `0`.

### Example

```python
languages = ["Python", "Django", "FastAPI", "Docker"]

print(languages[0])  # Python
print(languages[1])  # Django
print(languages[3])  # Docker

name = ["ABC","CDE","FGH"]
print(name[0]) # ABC 
print(name[1]) # CDE
print(name[2]) # FGH
```
## Positive Indexing

```python
Positive indexes access elements  from start of  the list.

name = ["ABC","CDE","FGH"]
print(name[0]) # ABC 
print(name[1]) # CDE
print(name[2]) # FGH

## Negative Indexing

Negative indexes access elements from the end of the list.
name = ["ABC","CDE","FGH"]
print(name[-1]) # "FGH"
print(name[-2]) # "CDE"
print(name[-3]) # "ABC"
```
## example :
name = ["ABC","CDE","FGH"]
print(name[-1]) # FGH
print(name[-2]) # CDE 
print(name[-3]) # ABC

## 5. List Methods

### `append()`

`append()` is used to add one individual item at the end of a list.

### Example

languages = ["Python", "Django"]

languages.append("FastAPI")

print(languages)
# ["Python", "Django", "FastAPI"]


### 🧠 Important

If you append a list:
================================================================================
languages.append(["FastAPI", "Docker"])

the entire list becomes one item:

["Python", "Django", ["FastAPI", "Docker"]]


## `insert()`

`insert()` is used to add an item at a specific index in a list.

### Syntax

# ```python
list.insert(index, item)

anguages = ["Python", "FastAPI", "Docker"]

language.insert(1,"Flask")
#["Python","Flask", "FastAPI", "Docker"]



### `remove()`

`remove()` is used to remove an item from a list by its value.

### Example

=======================================================================
languages = ["Python", "Django", "FastAPI", "Docker"]

languages.remove("Django")

print(languages)
# ["Python", "FastAPI", "Docker"]

### `pop()`

`pop()` is used to remove an item by its index and return the removed item.

### Example


languages = ["Python", "Django", "FastAPI", "Docker"]

removed = languages.pop(1)

print(removed)
# Django

print(languages)
# ["Python", "FastAPI", "Docker"]

pop(index) → remove by index + return the removed item.

### `clear()`

`clear()` is used to remove all items from a list, making the list empty.

### Example

========================================================================
languages = ["Python", "Django", "FastAPI"]

languages.clear()

print(languages)
# []

## clear() modifies the original list and returns None.
===============================================================================
### `extend()`

`extend()` is used to add multiple items individually at the end of a list.

### Example

================================================================================
languages = ["Python", "Django"]

languages.extend(["FastAPI", "Docker"])

print(languages)
# ["Python", "Django", "FastAPI", "Docker"]


### `index()`

`index()` is used to get the position (index) of an item in a list.


================================
### Example
languages = ["Python", "Django", "FastAPI", "Docker"]

position = languages.index("Docker")

print(position)
# 3
index() returns the index of the first occurrence of the value.

languages = ["Python", "Django", "FastAPI", "Docker","Docker"]

position = languages.index("Docker")

print(position)
# 3

### `count()`

`count()` is used to find how many times a specific value appears in a list.

### Example

=====================================================
languages = ["Python", "Django", "Python", "FastAPI", "Python"]

print(languages.count("Python"))
# 3
len() → total items
count(value) → occurrences of that value

### `sort()`

`sort()` is used to rearrange the items of a list in ascending order by default.

### Example

numbers = [10, 3, 7, 1, 5]

numbers.sort()

print(numbers)
# [1, 3, 5, 7, 10]


### `reverse()`

`reverse()` is used to reverse the current order of items in a list.

### Example


languages = ["Python", "Django", "FastAPI", "Docker"]

languages.reverse()

print(languages)
# ["Docker", "FastAPI", "Django", "Python"]


### 🧠 Remember

reverse() → reverse original list
[::-1]    → get reversed version using slicing

### `copy()`

`copy()` is used to create a new list containing the same elements as an existing list.

### Example


languages = ["Python", "Django", "FastAPI"]

new_languages = languages.copy()

print(new_languages)
# ["Python", "Django", "FastAPI"]



## 6. List Slicing

List slicing is used to access a range of elements from a list.

### Syntax


list[start:stop:step]

start-> from where to start / 
stop -> where to stop
step -> how many position to jump 
# Start = where, Stop = until where, Step = how far each jump.

## 7. Membership Operators

Membership operators are used to check whether an item exists in a list.

### `in`

`in` returns `True` if an item exists in the list.


languages = ["Python", "Django", "FastAPI"]

print("Python" in languages)
# True

print("Java" in languages)
# False

## 8. Looping Through Lists

<!-- A for loop can be used to visit each item in a list one by one. -->

languages = ["Python", "Django", "FastAPI"]

for language in languages:
    print(language)
#Python
#Django
#FastAPI

```
enumerate(): 

When you need both the index and value:
for index, language in enumerate(languages):
    print(index, language)

#0 Python
#1 Django
#2 FastAPI
    
```

## 🟢 Section 9: Nested Lists
## 9. Nested Lists

A nested list is a list that contains other lists as its elements.

### Example

```python
students = [
    ["Ritesh", 85],
    ["Amit", 72],
    ["Rahul", 91]
]
Accessing Nested List Elements:
print(students[0])
# ["Ritesh", 85]

print(students[0][0])
# Ritesh

print(students[0][1])
# 85
Looping through nested list 

for name, marks in students:
    print(name, marks)

Ritesh 85
Amit 72
Rahul 91


### 🧠 Remember

```text
students[1]     → second inner list
students[1][0]  → first item inside that list
students[1][1]  → second item inside that list
```

## 🟢 Section 10: List Unpacking

## 10. List Unpacking

List unpacking means assigning the elements of a list to multiple variables.

### Example

```python
student = ["Ritesh", 85]

name, marks = student

print(name)
# Ritesh

print(marks)
# 85
```

## Unpacking in a Loop
students = [
    ["Ritesh", 85],
    ["Amit", 72],
    ["Rahul", 91]
]

for name, marks in students:
    print(name, marks)

Ritesh 85
Amit 72
Rahul 91



# 🟢 Section 11: List Comprehension
# A list comprehension is a short way to create a new list from an existing iterable.
List comprehension is a concise way to create a new list using an expression, a loop, and optionally a condition.
### List Comprehension with a Condition

A condition can be added to a list comprehension using `if`.

### Syntax

```python
[expression for item in iterable if condition]