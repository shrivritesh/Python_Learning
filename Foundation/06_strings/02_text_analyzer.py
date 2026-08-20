"""
The Text Analyzer mini-project problem is:

🟢 Mini Project — Text Analyzer

Create a Python program that asks the user to enter a sentence and analyzes it.

# Your program should:
Remove leading/trailing spaces.
Convert the sentence to lowercase.
Count the number of words.
Count how many times "python" appears.
Find the position of the first "python".
Replace "python" with "java".
Check whether the sentence starts with "python".
Check whether the sentence ends with "python".
Display a final report.
Example

Input:

   Python is easy. I love Python.


Expected report:

========== Text Analyzer ==========


Cleaned Sentence: python is easy. i love python.
Number of Words: 6
Python Count: 2
First Python Position: 0
Starts With Python: True
Ends With Python: False
Final Sentence: java is easy. i love java.
"""

sentence = input("Enter your sentence :")

sentence = sentence.lower()
cleaned_sentence = sentence.strip()


count_words = cleaned_sentence.split()
python_count = cleaned_sentence.count("python")
first_python = cleaned_sentence.find("python")
rep = cleaned_sentence.replace("python","java")
start = cleaned_sentence.startswith("python")
ends = cleaned_sentence.endswith("python")


print("===============Text Analyzer================")

print("Cleaned sentence :",cleaned_sentence)
print("number of words: ",len(count_words))
print("Python Count :",python_count)
print("First Python position is :",first_python)
print("Start with python :",start)
print("Ends with python :",ends)
print("Final Sentence :", rep)
print("Number of characters :",len(cleaned_sentence))