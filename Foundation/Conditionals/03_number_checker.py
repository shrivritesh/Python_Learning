"""
Project 3 — Number Checker

Ask the user to enter a number.

Determine whether the number is:
Negative
positive
Zero

"""

num = int(input("Enter any number:"))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

