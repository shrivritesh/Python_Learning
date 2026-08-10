"""

**Age Validation Rules**
age < 0    → Invalid age
0-12       → Child
13-17      → Teenager
18+        → Adult

marks grade rules
90-100 → A
80-89  → B
70-79  → C
60-69  → D
40-59  → E
0-39   → Fail

"""

name = input("Enter student name :")
age = int(input("Enter age of the student:"))
# marks = int(input("Enter marks of the student :"))

# take marks of all Subject

maths = int(input("Enter Maths marks: "))
Physics = int(input("Enter Physics marks: "))
Chemistry = int(input("Enter Chemistry marks: "))
English = int(input("Enter English marks: "))
Computer = int(input("Enter Computer marks: "))

total_marks = 0
percentage = 0
grade = "Invalid marks!"

# Validate Marks.
valid_marks= True

if maths < 0 or maths > 100:
    valid_marks = False
if Physics < 0 or Physics > 100:
    valid_marks = False
if Chemistry < 0 or Chemistry > 100:
    valid_marks = False
if English < 0 or English > 100:
    valid_marks = False
if Computer < 0 or Computer > 100:
    valid_marks = False

total = 500
if valid_marks:
    total_marks = maths + Physics + Chemistry + English + Computer
    percentage = total_marks / total * 100


# print(f"{name}. {age}. {marks}")


# Age Validation:
if age < 0:
    age_category ="Invalid age."
elif age <= 12:
    age_category = "Child."
elif age <= 17:
    age_category = "Teenager"
else:
    age_category = "Adult!"

# Marks Validation

if not valid_marks:
    grade = "Invalid marks!."
elif percentage >= 90:
    grade = "A grade."
elif percentage >= 80:
    grade = "B grade."
elif percentage >= 70:
    grade = "C grade."
elif percentage >= 60:
    grade = "D grade."
elif percentage >= 40:
    grade = "E grade."
else:
    grade = "Fail!."


# print(percentage)

print("**--------------STUDENT_REPORT**--------------------")
print(f"Name: {name}.")
print(f"age: {age}.")
print(f"Category: {age_category}")


print(f"maths :{maths}.")
print(f"Physics :{Physics}.")
print(f"Chemistry: {Chemistry}.")
print(f"English:{English}.")
print(f"Computer:{Computer}.")

print(f"Total Marks: {total_marks}/{total}.")
print(f"Percentage: {percentage}")
print(f"Grade: {grade}")

# A condition decides what happens, and a variable can store the result for later use.


# Remember this project as:

# Input → Validate → Store → Calculate → Decide → Report