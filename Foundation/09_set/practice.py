"""
What is set?
A set is a built-in, unordered , mutable collection  that store unique elements. it does not support duplicates value.
It is created using curly braces {} with elements seperated by comma .
syntax: 
empty = set() # empty set
indexing is not allow in set. because it is unorderd.

"""
languages = {"Python","Django" ,"Python","Docker","Django"}
print(languages) # {"Python","Django" ,"Docker"} # order can change every time.


print(len(languages))

# Set Methods 
# add() to add one element in set.
languages = {"Python", "Django"}
languages.add("Docker")
languages.add("FastAPi")
print(languages)

# Update() methods used to add multiple elements

languages.update(["FastAPI","Docker","Flask"])
print(languages)

print(languages.discard("Java")) # NOne
# print(languages.remove("Java")) # Raise Key Error.

numbers = {10, 20, 30}

removed = numbers.pop()#vwill remove anyone

print(removed)

numbers = {1, 2, 3, 4}

result = numbers.clear()

print(numbers) #set()
print(result) # none

numbers = {1, 2, 3}

numbers.add(4)

print(numbers) # {1, 2, 3, 4}

# Membership 
# In and not in
languages = {"Python", "Django", "FastAPI"}

print("Django" in languages) # True 
print("Java" not in languages) # True
print("Docker" in languages) # False

# Union --> Union = everything from both sets, without duplicates.

a = {1, 2, 3}
b = {3, 4, 5}

result = a.union(b)
print(result) # {1, 2, 3, 4, 5}


python = {"Python", "Django", "FastAPI"}
javascript = {"JavaScript", "React", "Django"}
uni = python.union(javascript)
print(uni) #{"Python", "Django", "FastAPI","JavaScript", "React"}


"""
# Mini Project -Unique technology analyzer.

Your program should:

Print all students.
Create a set containing unique programming languages.
Print how many unique languages there are.
Check whether "Python" is present.
Create a set containing only languages whose name has more than 5 characters.

"""
students = [
    ("Ritesh", "Python"),
    ("Amit", "Java"),
    ("Rahul", "Python"),
    ("Priya", "JavaScript"),
    ("Neha", "Python"),
    ("Aman", "JavaScript")
]

unique = set()
long_language = set()
for name , language in students:
    print(name, language)
    unique.add(language)
    if len(language) > 5:
        long_language.add(language)

# for language in unique:
    
    
print("Unique programming language: ",unique)
print("Number of unique language is: ",len(unique))
print("Python" in unique)
print("language whose char is above 5 char: ",long_language)



