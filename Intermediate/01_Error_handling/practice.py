
# Basic try/except
try:
    num = int(input("Enter number :"))
    print(num)
except ValueError:
    print("Invalid number. ")

# ValueError + ZeroDivisionError
try:
    number = int(input("Enter number :"))
    subs = 100/ number
    print("Resullt is ", subs)
except ValueError:
    print("Invalid number. ")
except ZeroDivisionError:
    print("Cannot divide by zero")

# Exception stops the try

try:
    print("Start")
    number = int("hello")
    print("Middle")
    print("End")

except ValueError:
    print("Invalid conversion")

print("Program continues") 


# Calculator
try:
    num1 = int(input("Enter first number :"))
    num2 = int(input("Enter second number :"))
    operator = input("Enter operator: ")
    if operator == "+":
        add = num1 + num2
        print("Addition of 2 numbers is :",add)
    elif operator == "-":
        subs = num1 - num2
        print("Subtraction of two numbers is :",subs)
    elif operator == "*":
        multi = num1 * num2
        print("Multiplication of two number is :",multi)
    elif operator == "/":
        div = num1 / num2
        print("Division of two number is :",div)
    else:
        print("Invalid Operator!.")

except ValueError:
    print("Please Enter numbers only: ")
except ZeroDivisionError:
    print("Cannot divide by Zero.")

else:
    print("Successfully Calculation") # No exception occurred anywhere in the try block.
finally:
    print("Program Done! ")

# age = -5
# raise ValueError("Age Cannot be negative:")


# 
# age = int(input())
def check_age(age):
    if age < 0 or age > 120:
        raise ValueError("Age must be between 0 to 120 ")
    return age

try:
    age = int(input("Enter age :"))
    print(check_age(age))
except ValueError as e:
    print(e)

"""
try:
    # Some Code to check for errors
except:
    # If an error in the
    # try block then execute this block
else:
    # If no exception then execute this
finally:
    # This code always executed after the try-except
"""


"""
# Custom Exception
Q. Why Custom Exception?
A. To increase the readability of code.
===============================================================
Custom exceptions improve code readability and maintainability
by giving application-specific errors meaningful names,
making them easier to understand and handle.”

"""
# example
def validate(name):
    if len(name) < 4:
        raise ValueError("Name is too short")
    
user_name = input("Enter your name :")
try:    
    validate(user_name)
except ValueError as e:
    print(e)
else:   
    print(f'Hello {user_name} ')

"""
Q1. Exception propagation?
Exception propagation is the process where an exception 
moves back through the call stack until it is handled by a matching exception handler.


If a function raises an exception and doesn't handle it,
the exception propagates to the caller. This continues up the call stack until a matching handler is found; otherwise, the program terminates

"""
def calculate():
    return 100 / 0

def process():
    calculate()

try:
    process()
except ZeroDivisionError:
    print("Handled")

# Question: Where does the exception actually occur, and where is it handled?

# Exception occures - inside the calculate()
# pass through - process()
# Exception handle : by ZeroDivisionError
