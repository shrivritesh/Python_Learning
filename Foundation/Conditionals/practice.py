"""
**Q.What is a Conditional?**
>A conditional statement allows a program to make a decision based on whether a condition is True or False.



if statements:

if condition:
    statement
age = 21
if age >= 18:
    print("Adult")
else:
    print("Minor :")

if          → tells Python to check something
age >= 18   → condition
:           → starts the if block
print()     → runs if the condition is True

else:       -> else runs when the if condition is False.

value = input()

if condition:
    # do this
else:
    # otherwise do this

elif : 
    # For multiple condition

if     → Try this
elif   → Otherwise, try this
elif   → Otherwise, try this
else   → If nothing worked

if    → check the first condition
elif  → check another condition if the previous one was False
else  → run if all conditions were False



if → checks the first condition.
elif → checks another condition if the previous one was false.
else → runs when none of the previous conditions are true.
"""


age = 21
if age >= 18:
    print("Adult")
else:
    print("Minor :")

