names = "ritesh"
print(names[0])
print(names[2])
print(names[5])

print("python"[0:3])

word = "Ritesh"
print(word.upper())

text = "Hello Python 123!"

result = text.upper()
print(result)

"""
🟢 Question 1 — Indexing
What will this print?

"""
word = "Programming"


print(word[0]) # P
print(word[-1]) # g
print(word[3]) # g
print(word[-3]) # i

# 🟢 Question 2 — Slicing

word = "Programming"

print(word[0:6]) # Progra
print(word[3:8]) # gramm
print(word[:4]) # Prog
print(word[5:]) # amming
print(word[::-1]) # gnimmargorp

# 🟢 Question 3 — Concatenation + Repetition
first = "Py"
second = "thon"

word = first + second

print(word) # Python
print(word * 2) # PythonPython
print(word + "!") #  Python!

# 🟢 Question 4 — String Methods

text = "  hello PYTHON world  "


print(text.strip()) # hello PYTHON world
print(text.upper()) #       HELLO PYTHON WORLD
print(text.lower()) #       hello python world
print(text.capitalize())  # Hello python world
print(text.title()) #       Hello Python World

# 🟢 Question 5 — find() + count()

# Don't run it. 🧠

text = "Python is easy. Python is powerful."


print(text.find("Python")) # 0
print(text.find("is"))      # 7
print(text.count("Python")) # 2
print(text.count("is"))     # 2
print(text.find("Java"))    # -1

# 🟢 Question 6 — .split() + .join()

# Now let's combine two methods:

text = "Python is very easy"


words = text.split()


result = "-".join(words)


print(words) # ["Python","is","very", "easy"]
print(result) # Python-is-very-easy

# 🟢 Question 7 — Validation + Methods

value = input("Enter a value: ")
# 123a5 --> Invalid number
# 1234 --> Valid number

if value.isdigit():
    print("Valid number")
else:
    print("Invalid number")

age = input("Enter your age: ")

if age.isdigit():
    age = int(age)
    print("Your age is :", age)
else:
    print("Please enter digits only.")



# 🟢 Question 8 — Combined String Challenge


text = "  Python is AWESOME  "


text = text.strip()
text = text.lower()


words = text.split()


print(words) #     ['python', 'is', 'awesome']
print(len(words))#  3


# 🟢 Question 9 — Mini String Problem
"""
Let's now solve a practical one.

Write a program that asks the user for a sentence and:

Removes extra spaces from the beginning/end.
Converts the sentence to lowercase.
Counts how many words it contains.
Prints the cleaned sentence.
Prints the number of words.
Example :
Enter sentence:    Python Is Very Easy   

Cleaned sentence: python is very easy
Number of words: 4

"""

# sentence = input("Enter your sentences :").strip()

# cleaned = sentence.strip()
# lower = sentence.lower()
# words = sentence.split()


# print("Cleaned sentence :",sentence)
# print("Lowercase :",lower)
# print("Number of words is :",len(words))

# 🟢 Question 10 — String Challenge

# Now let's combine .find(), .count(), .replace(), .strip(), .lower().
#    Python is easy. I love Python.

sentence = input("Enter a sentence :")

sentence = sentence.strip()
sentence = sentence.lower()
word_count = sentence.count("python")
rep = sentence.replace("python","java")

print("Word Count :",word_count)
print("Final Sentence :",rep)


