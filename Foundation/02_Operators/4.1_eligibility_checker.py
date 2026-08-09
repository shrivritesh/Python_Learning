"""
Your program should check:

1.Is the person 18+ AND has an ID?

2.Is the person younger than 18 OR has no ID?

3.Does the person NOT have an ID?

Use:

and
or
not
"""

age = 24
has_id = True

print(age > 18 and has_id)
print(age < 18 or not has_id)
print(not has_id)

age = 16
has_id = False

print(age > 18 and has_id) # False
print(age < 18 or not has_id) # True
print(not has_id)               # True

# Logical operators are used to combine or reverse conditions and produce True or False.