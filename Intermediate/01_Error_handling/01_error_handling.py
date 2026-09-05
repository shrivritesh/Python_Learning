"""
Q1.What is an Error?

An error is a problem in a program that prevents it from behaving as expected.

Python has different kinds of errors.

Types of error:
1.--Syntax error
A syntax error occurs when Python's rules/grammar are violated.
Python can't properly understand the structure of your code.

2-Runtime Error/ Exception
Runtime errors are occur while your program is executing.
These error represent unexpected condition that interrupt normal program flow.
like tryimg to divide by zero accessing a non existent file or calling a function that doesn't exist.

3-Logical Error
A logical error when a program runs succesfully
without producing an expection but the output or result is incorrect because the program's logic wrong. 

=====Exception======
Errors detected during execution are called exceptions and are not unconditionally fatal.

Python provides four main keywords for handling exceptions: 
try, except, else and finally each plays a unique role. :

Syntax:

try:
    # Code that may raised exception
except:
    # catch and handle the exception if one occurs
else:
    # Executes only if no exception occurs in try.
finally:
    # Runs regardless of what happens useful for cleanup tasks like closing files.
"""

# example of syntax error

name = input("Enter a name.: " )
if name == "Ritesh":  # : SyntaxError : : expected.
    print(name)
else:
    print("Please enter valid name")


# example of runtime Error.

a = 20
b = 0
res = a/ b
print(res) 
#ZeroDivisionError

# 2 example
str , num = "Ritesh" , 10
print(str + num)
#TypeError

# 3 Example
num = [10,20,30,40]
print(num[5])
# IndexError

# Without exception handling
number = int(input("Enter a number :"))
print(number)

# if user enter abc instead of number. then the python raise ValueError

# With Exception Handling
try:
    number = int(input("Enter a number :"))
except ValueError:
    print("Please Enter a valid number....")
print("Program Continues........")



# num1 = 8
# num2 = 0
# result = num1 / num2
# print(result)


try:
    num = int(input("Enter number:"))
    result = 100/ num
    print(result)
except ValueError:
    print("Invalid number")
except ZeroDivisionError :
    print("Cannot Divide by Zero .")


# Exception Handling.
a = input("Enter the number:")
print(f"Multiplication table of {a} is : ")

try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a) * i} ")
except Exception as e:
    print("Sorry Some error occured .",e)
except IndentationError as i:
    print(i)
finally:
    print("program finished!")



try:
    n = 0
    res = 100 / n
    
except ZeroDivisionError:
    print("You can't divide by zero!")
    
except ValueError:
    print("Enter a valid number!")
    
else:
    print("Result is", res)
    
finally:
    print("Execution complete.")