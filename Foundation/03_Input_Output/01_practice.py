"""
# print() is a built-in function used to display information on the screen.

# input() is a built-in function used to take data from the user through the keyboard.

Then print(name) displays it.

input() → 📥 Take data from user
print() → 📤 Show data to user

input() gives a String
eg:
age = input("Enter your age:")
if user type : 24
python automatic store this value as string

we use int() when you need integer
it stored 24 as int

"""

#Example:
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"My name is {name}")
print(f"I am {age} years old")