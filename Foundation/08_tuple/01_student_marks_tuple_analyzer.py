"""
Your program should:

Print every student's name and marks.
Find the highest marks.
Find the lowest marks.
Calculate total marks.
Calculate average marks.
Print students who scored 80+.
Restriction

Use only concepts we've learned so far.

Don't use sorted(), dictionaries, sets, or functions that we haven't learned yet.

"""
students = (
    ("Ritesh", 85),
    ("Amit", 72),
    ("Rahul", 91),
    ("Priya", 68)
)
highest = 0
lowest = 100
total = 0
for name,marks in students:
    print(name,marks)

    if marks > highest:
        highest = marks
    if marks < lowest:
        lowest = marks

    total += marks
average = total / len(students)
print("Highest marks is :",highest)
print("Lowest marks is :",lowest)
print("Total marks is :",total)
print("Average marks is :",average)


print("students who scored 80+")
for name, marks in students:
    if marks >= 80:
        print(name , marks)


# [expression for item in iterable if condition]
score = [(name,marks) for name, marks in  students if marks > 80 ]
print(score)

"""
Tuple :
A tuple in Python is a built-in, ordered, immutable collection used to store multiple elements,
including elements of different data types.
It is commonly created using parentheses (), with elements separated by commas

Tuple unpacking means assigning the elements of a tuple to multiple variables.
"""

lang = (["Python","Backend"],["JavaScript","Frontend"])
language , use = lang
print(language)
print(use)

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
# print(languages.index(2))
print("Flask" in languages)
print(languages[::-1])