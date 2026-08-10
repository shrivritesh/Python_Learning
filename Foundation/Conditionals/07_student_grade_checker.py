name = input("Enter student name :")
marks = int(input("Enter student marks:"))
"""
# Marks < 0 or Marks > 100 → Invalid marks
90–100 → A
80–89  → B
70–79  → C
60–69  → D
40–59  → E
0–39   → Fail
"""

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print(f"{name},Your grade is A.")
elif marks >= 80:
    print(f"{name},Your grade is B.")
elif marks >= 70:
    print(f"{name},Your grade is C.")
elif marks >= 60 :
    print(f"{name},Your grade is D.")
elif marks >= 40:
    print(f"{name},Your grade is E.")
else:
    print(f"{name},You failed!!.")



# A conditional statement makes a decision based on whether a condition is True or False.