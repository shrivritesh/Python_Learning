"""
Project 2 — Pass / Fail Checker

Ask the user for their marks.

Rules: 
40 or above pass, 
Below 40 fails
"""

marks = int(input("Enter your marks:"))

if marks >= 40:
    print("you are passed")
else:
    print("failed!!")