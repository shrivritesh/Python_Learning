"""
🟢 String Looping

A string is an iterable,
which means Python can go through its characters one by one.
"""
# Question : 1
print("============Answer One :===============")
word = "python"

for char in word:
    print(char)


# Question 2:
print("============Answer Two=========")
word = "DOG"

for letter in word:
    print(letter)

# Question 3 : Count characters
print("=====================Count characters=====================")
wor = "python"
count = 0

for x in wor:
    print(x)    
    count += 1

print(count)


# 🟢 Question 4 — Count a Specific Character
print("=========================Count a specific char ========================")
word = "Banana"
count = 0
for letter in word:
    if letter == "a":
        count += 1
    print("character count is :",count)
print("Final char count is :",count)


# 🎯 Question 5 — Count Vowels
# Write a program that counts the total number of vowels in: aeiou

print("===================Count Vowels :===================")
word = "programming"
count = 0
for letter in word:
    if letter in "aeiou": #in checks whether the current character exists inside "aeiou"
        count += 1
print("Number of vowels :",count)



# 🟢 Question 6 — Count Vowels and Consonants
print("======================Count vowels and consonants======================")
word = "programming"
vowels = 0
consonants = 0
for letter in word:
    if letter in "aeiou": #in checks whether the current character exists inside "aeiou"
        vowels += 1
    else:
        consonants += 1
print("Number of vowels :",vowels)
print("Number of Consonants :",consonants)


# 🟢 Q7 — Count Uppercase & Lowercase
print("==========================Count UpperCase & LowerCase ==========================")
text = "PyThOn Programming"
upperCase = 0
lowerCase = 0
for char in text:
    if char.isupper():
        upperCase += 1
    elif char.islower():
        lowerCase += 1

print("UpperCase :",upperCase)
print("LowerCase :",lowerCase)

# 🟢 Q8 — Reverse a String Using a Loop
print("====================Reverse string====================")
word = "Python"

reverse = ""
for char in word:
    reverse = char + reverse
print("Reverse of word is :",reverse)


# 🎯 Q9 — Palindrome Check
# A palindrome is a word that reads the same forward and backward.
print("====================Palindrome check====================")
word = "Ritesh"
reverse = ""
for char in word:
    reverse = char + reverse
if word == reverse:
    print("Palindrome.")
else:
    print("Not a Palindrome.")
        

# 🟢 Q10 — Character Frequency

print("===========================Character Frequency===========================")

word = "banana"
count = 0
seen = ""

# for char in word:
#     if char == "n":
#         count +=1

# print("n appears : ",count,"times.")

for char in word:
    if char not in seen:
        seen += char
        count = word.count(char)
        print(char, "->", count)
# print(seen)

# Final 


print("======================Final Program======================")
word = "Programming"

vowels = 0
consonants = 0
uppercase = 0
lowercase = 0

for char in word:
    if char in "aeiou":
        vowels += 1
    else:
        consonants += 1
    if char.isupper():
        uppercase += 1
    elif char.islower():
        lowercase += 1
print("Vowels :",vowels)
print("consonants :",consonants)
print("upperCase :",uppercase)
print("lowercase :",lowercase)