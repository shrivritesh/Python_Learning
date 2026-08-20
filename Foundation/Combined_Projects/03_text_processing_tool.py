"""
===========🟢 Text Processing Tool =============
📌 Project Description

Text Processing Tool is a Python-based command-line application that analyzes and processes user-provided text.
It combines fundamental Python string concepts such as string methods, indexing, slicing, searching, replacing, splitting,
looping, and character validation into one practical project.

⚙️ What it does

The application allows users to:

Clean and normalize text
Count characters and words
Search for specific words
Count word occurrences
Replace words with other words
Count vowels and consonants
Count uppercase, lowercase, and numeric characters
Reverse text
Check whether text is a palindrome
"""

print("=================Text Processing Tool=====================")

original_text = input("Enter your sentence : ")

text = original_text.strip()
text = text.lower()
words = text.split()

# Search specific word input given by user:

search_word = input("Enter word to search :").lower()

position = text.find(search_word)

occurrences = text.count(search_word)

# replacements of words :
replacement = input("Enter replacement word :").lower()

updated_text = text.replace(search_word,replacement)

# Character Analysis
analysis_text = original_text.strip()
vowels = 0
consonant = 0
uppercase = 0
lowercase = 0
digits = 0

for char in analysis_text:
    if char.lower() in "aeiou":
        vowels += 1
    elif char.islower() or char.isupper():
        consonant += 1

    if char.islower():
        lowercase += 1
    elif char.isupper():
        uppercase += 1
    if char.isdigit():
        digits += 1

# Reverse the string

reverse = ""
for char in text:
    reverse = char + reverse

if text == reverse:
    palindrome = True
else:
    palindrome = False

print("Clean and Normalize Text :", text)
print("Number of character :",len(text))
print("Number of words : ",len(words))
print("Position of search word :", position)
print("Occurences :",occurrences)
print("Text after Replacement :", updated_text)
print("vowels :",vowels)
print("Consonant :", consonant)
print("Lowercase :",lowercase)
print("UpperCase :",uppercase)
print("Digit :", digits)
print("Reverse :",reverse)
print("Palindrome :", palindrome)


