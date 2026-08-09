score = 100

score += 50
print(score) #150

score -= 20
print(score) #130

score *=2 
print(score) # 260

score /= 5
print(score) # 52.0

score //= 3
print(score) # 17
score %= 4
print(score) # 1.0
score **= 2 
print(score) # 1.0

'''
Assignment operators perform an operation AND store the new result back into the variable.
'''

x = 30

x*5
print(x) # 150

x *= 5 
print(x)

"""

Q1.What does this mean?
x += 5 -> perform and update the new value in x
Q2

What's the difference between:

x * 5 this will only perform multiplication but not upadating or assigning value

and

x *= 5 this will perform and update/ assign the value 
Q3

What does this mean?

score %= 3 Find the remainder and store it back in the variable.
Answer these first. Then we'll learn and, or, and not.
"""