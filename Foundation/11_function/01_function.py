"""
Q1.What is function?
Function is a reuseable block of code that performs a specific task.
A function in Python is defined using the def keyword, followed by the function name and parentheses ().

syntax:
def fun_name():
    #code
fun_name()

Parameter:
A parameter is the variable written inside the function definition.

Argumet:
A argument is the variable written inside the function while calling.
An argument is the actual value passed when the function is called.


A parameter (also called a formal argument) is a variable defined in the function definition.
An actual argument is the value passed when the function is called.
"""
name = input("Enter your name :")
def greet(): #function with no parameter.
    return f"Hello {name}."

fun_call = greet()
print(fun_call)

def say_hello():
    print("Hello! Python")
say_hello()


def greet(name): # function with parameter
    return f"Namastey {name}"

result = greet("Ritesh") # actual value.
print(result)

# *args
def show(*args):
    print(args)

show(10, 20, 30)

#variable length keyword arguments.
def show(**kwargs):
    print(type(kwargs))
    print(kwargs)

show(name="Ritesh", age=25)



# Positional Arguments -->Arguments are matched according to their position. order matters.
print("Positional arguments :")
def student(name, age):
    print(name, age)

student("Ritesh", 25) # positional args.


# Keyword Arguments :--> Arguments are matched using the parameter name.
print("KeyWord Arguments :")
obj = student(name="Ritesh", age= 24) #keyword arg.
print(obj)
# order does not matter because python matches arguments by parameter.


# Positional + Keyword Arguments Together
def student(name, age, city):
    print(name, age, city)

student("Ritesh", age=25, city="Delhi")

#Ritesh - > positional arguments
# age =25 - > keyword arg.
# city = "delhi" -> keyword arg.

# Positional arguments must come before keyword arguments.


def calculate_total(numbers):
    total = 0
    for number in numbers:
        total += number
    return total 

result = calculate_total([21,3,43,54,29])
print(result)

# Functions can return multiple values

def calculate(a,b):
    return a+b , a-b , a*b , a /b 

sum,subs,mul,division = calculate(15,10)
print(sum)
print(subs)
print(mul)
print(division)

# Function Composition

def square(n):
    return n * n

sqr = square(2)
print(sqr) # 4

def double(n):
    return n * 2
twice = double(square(5))# 2(5^2) --> 50
print(twice)

def add(a,b):
    return a + b

sum = add(5,9)

def squaree(n):
    return n * n
sqr = square(add(3,2))

print(sqr)

def multiply(a,b):
    return a * b
product = multiply(3,5)

def add_five(n):
    return n + 5

five = add_five(multiply(3,7))
print(five)



# Functions — Mini Project
"""
🎯 Project: Calculator Function

Create a function:

def calculator(a, b):

It should return:

Addition
Subtraction
Multiplication
Division

Then unpack the returned values:
"""
print("=================Calculater function =================")
def calculate(a,b):
    return a+b, a-b, a*b, a/b
addition,subtraction ,multiplication,division = calculate(10,3)
print(addition)
print(subtraction)
print(multiplication)
print(division)