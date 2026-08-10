""""
Project 5 — Simple Login Checker

Store a username and password in variables.

Ask the user to enter their username and password.

If both are correct:

Loggin Successfully

otherwise:
Invalid username or password
"""

stored_user_name = "ritesh"
stored_password = "ritesh@123"

user_name = input("Enter your Username :")
pass_word = input("Enter your password :")

if stored_user_name == user_name and stored_password == pass_word:
    print("Login Successfully")
else:
    print("Invalid username or password")