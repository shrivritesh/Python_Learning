"""

The program should:

Print every student's name and marks.
Find the highest marks.
Find the lowest marks.
Calculate the total marks.
Calculate the average marks.
Print students who scored 80 or more.
Restrictions

Use only concepts we've learned:

Lists
Nested lists
for
enumerate()
if
len()
variables
basic arithmetic
"""

students = [
    ["Ritesh", 85],
    ["Amit", 72],
    ["Rahul", 91],
    ["Priya", 68]
]
highest = 0
lowest = 100
total = 0
for name, marks in students:
    print(name, marks)
    #Comapring highest marks
    if marks > highest:
            highest = marks
    #Comapring lowest marks
    if marks < lowest:
            lowest = marks
    total += marks
avg = total / len(students)


print("highest marks is :",highest)
print("Lowest marks is :", lowest)
print("Total marks is :", total)
print("Average of marks is :",avg)

print("students who scored 80 or more.")

for name, marks in students:
    if marks >= 80:
        print(name, marks)