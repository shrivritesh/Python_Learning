""" 
Q1.What is tuple?
A tuple in Python is a built-in, ordered, immutable collection used to store multiple elements,
including elements of different data types.
Tuples are usually created using parentheses (), and their elements can be accessed using indexing and slicing.
"""

tup = ("ritesh",34,3.14,True,"ritesh")
print(type(tup))
print(tup)
print(tup[1])
print(tup.count("ritesh"))
print(tup.index(3.14))

print("=================Positive Indexing=====================")

language =( "Python","JavaScript","Golang","C++")

print(language[0]) # Python
print(language[1]) #javascript
print(language[2]) #Golang
print(language[3]) # C++

print("=================Negative Indexing=====================")
print(language[-1]) # C++
print(language[-2]) # Golang
print(language[-3]) # JavaScript
print(language[-4]) # Python


language = ("Python", "JavaScript", "Golang")

# language[1] = "Django"
# print(language)

print("==================Tuple Slicing===============")

# Tuple Slicing
languages =( "Python","JavaScript","Golang","C++")
print(languages[1:4]) # py js go 


languages = ("Python", "Django", "FastAPI", "Docker", "Flask")
print(languages[1:5:2]) # Django , Docker
print(languages[0:4:2]) # Python , FastAPI

"""
# Tuple Methods
Tuples have fewer methods than Lists because they are immutable.
The two important built-in tuple methods are:

1. count()
Counts how many times a value occurs.
2.Index()
Returns the index of the first occurrence of a value.
"""
print(languages.count("FastAPI")) # 1
print(languages.index("Docker")) # 3
print(len(languages)) # 5


"""
--> Tuple Packing & Unpacking
tuple packing :
putting multiple tuple values into single tuple

tuple unpacking :
take values out into seperate variables
"""
languages = "Python","JavaScript","Golang","C++"
print(languages) # Tuple packing

a, b, c, d = languages
print(a)
print(b)
print(c) # unpacking tuple into seprate var.

data = ("Python", ["Django", "FastAPI"])

data[1].append("Flask")
print(data) #("Python", ["Django", "FastAPI"],"Flask")


data = ("Python", "Django", "FastAPI")

a, b ,c= data
print(a)
print(b) #ValueError: too many values to unpack

# Tuple Looping
languages = ("Python", "Django", "FastAPI")
for language in languages:
    print(language)

for index, language in enumerate(languages):
    print(index, language)

# 0 Python
# 1 Django
# FastAPi

languages = ("Python", "Django", "FastAPI", "Docker")

for language in languages:
    print(language)

# Python
# Django 
# FastAPI
# Docker

# Tuple Membership
languages = ("Python", "Django", "FastAPI")

print("Python" in languages)
# True

print("Java" in languages)
# False

print("Java" not in languages)
# True

languages = ("Python", "Django", "FastAPI")

print("Django" in languages) # True
print("Java" not in languages) # True
print("Docker" in languages) # False


"""
====Tuple Concatenation

Since tuples are immutable, you can't use methods like append() or extend().
But you can create a new tuple by combining tuples using +.
"""
tuple1 = ("Python", "Django")
tuple2 = ("FastAPI", "Docker")

result = tuple1 + tuple2

print(result) #('Python', 'Django', 'FastAPI', 'Docker')

a = (1, 2, 3)
b = (4, 5, 6)
c = a + b
print(c) #(1, 2, 3, 4, 5, 6)

# Tuple min(), max(), sum()

num = (23,44,24,98,42,11)
print(min(num)) # 11
print(max(num)) # 98
print(sum(num)) # 242


marks = (85, 72, 91, 68)
print(min(marks)) # 68
print(max(marks)) # 91
print(sum(marks)) # 316
print(len(marks)) # 4

# Converting list <--> tuple

tup = ("Ritesh","Srivastav","Master's","Python")
lst = list(tup)
print(lst)

lst = tuple(lst)
print(lst)

# Tuple * Unpacking
start, *middle, last = lst
print(start) #--> Ritesh
print(*middle)  # Srivastav Master's
print(last) # # Python




languages = ("Python", "Django", "FastAPI", "Docker", "Python")
"""
Your program should:

Print the tuple.
Print its length.
Count "Python".
Find the index of "FastAPI".
Check whether "Flask" exists.
Print the tuple in reverse.
"""

print(tuple(languages))
print(len(languages))
print(languages.count("Python"))
print(languages.index("FastAPI"))
print("Flask" in languages)
print(languages[::-1])