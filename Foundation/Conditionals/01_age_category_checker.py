"""
Project 1 — Age Category Checker
Create a program that asks the user for their age and displays:

Age < 0       → Invalid Age
0–12          → Child
13–17         → Teenager
18–59         → Adult
60+           → Senior

USe....,input(),int(),if,elif,else,print()

"""



age = int(input("Enter your age: "))

if age < 0:
    print("Invalid Age!")
elif age <= 12:
    print("Child")
elif age <= 17:
    print("Teenager!")
elif age < 60:
    print("Adult!!")
else:
    print("senior")
