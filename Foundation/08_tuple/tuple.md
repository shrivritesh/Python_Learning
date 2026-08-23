# Python Tuples

## 1. What is a Tuple?

Tuple :
A tuple in Python is a built-in, ordered, immutable collection used to store multiple elements,
including elements of different data types.
It is commonly created using parentheses (), with elements separated by commas

## 2. Creating a Tuple
It is commonly created using parentheses (), with elements separated by commas

### Example

```python
languages = ("Python", "Django", "FastAPI")
numbers = (10, 20, 30)
```
## 3. Tuple Indexing
Tuple indexing means accessing a specific element from a tuple using its index.

Python uses zero-based indexing, so the first element has index `0`.

### Positive Indexing
Positive indexing accesses elements from the beginning of the tuple.

language =( "Python","JavaScript","Golang","C++")

print(language[0]) # Python
print(language[1]) #javascript


### Negative Indexing
Positive indexing accesses elements from the end of the tuple.

print("=================Negative Indexing=====================")
print(language[-1]) # C++

## 4. Tuple Immutability

A tuple is immutable, which means we cannot change, add, or remove its elements after creating the tuple.

### Example

```python
languages = ("Python", "Django", "FastAPI")

languages[1] = "Flask"
```

This gives:

```text
TypeError: 'tuple' object does not support item assignment
```

### 🧠 Remember

```text
Tuple → immutable → cannot modify elements
List  → mutable   → can modify elements
```
## 5. Tuple Slicing

Tuple slicing is the process of extracting a portion (sub-tuple) of a tuple.

### Syntax
tuple[start:stop:step]
start - includes
stop - exludes
step - how many jump to each step

## 6. Tuple Methods
tuple has two important methods 
### count()
```
number of occurence of elements in tuple.
numbers = (10, 20, 10, 30, 10)
print(numbers.count(10))
# 3
```
### index()
Returns the index of the first occurrence of a value.
```
numbers = (10, 20, 10, 30, 10)
print(numbers.index(10))
# 1
```
## 7. Tuple Packing

## 8. Tuple Unpacking

## 9. Extended Unpacking

## 10. Looping Through Tuples
### for loop
### enumerate()

## 11. Membership Operators
### in
### not in

## 12. Tuple Concatenation
### + operator

## 13. Tuple Repetition
### * operator

## 14. Tuple Comparison

## 15. Built-in Functions
### len()
### min()
### max()
### sum()

## 16. List ↔ Tuple Conversion

## 17. Functions vs Methods

## 18. Important Differences
### List vs Tuple
### Tuple Method vs Built-in Function

## 19. Mini Project
Student Marks Tuple Analyzer

## 20. Quick Revision