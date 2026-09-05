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
tuple has two important built-in methods.
### count()
```
`count()` returns the number of times a specific value occurs in a tuple.
numbers = (10, 20, 10, 30, 10)
print(numbers.count(10))
# 3
```
### index()
Returns the index of the first occurrence of a value.
```
numbers = (10, 20, 10, 30, 10)
print(numbers.index(10))
# 0
```
## 7. Tuple Packing

Tuple packing means putting multiple values together into a single tuple.

### Example

```python
languages = "Python", "Django", "FastAPI"

print(languages)
# ("Python", "Django", "FastAPI")
```

## 8. Tuple Unpacking
## 8. Tuple Unpacking

Tuple unpacking means assigning the elements of a tuple to multiple variables.

### Example

```python
data = ("Python", "Django", "FastAPI")

language, framework, api = data

print(language)
# Python

print(framework)
# Django

print(api)
# FastAPI
```

## 9. Extended Unpacking
one variable to collect multiple values. That's where * is used.
Syntax:
first, *middle, last = data --> *middle always return list of element
The *middle variable collects all remaining values into a list.

Extended unpacking → * collects multiple remaining values into a list.

## 10. Looping Through Tuples

## 10. Looping Through Tuples

A `for` loop can be used to access each element of a tuple one by one.

### Example

```python
languages = ("Python", "Django", "FastAPI", "Docker")

for language in languages:
    print(language)
```

Output:

```text
Python
Django
FastAPI
Docker
```

### Using `enumerate()`

`enumerate()` gives both the index and value while looping.

```python
for index, language in enumerate(languages):
    print(index, language)
```

Output:

```text
0 Python
1 Django
2 FastAPI
3 Docker
```

### 🧠 Remember

```text
for item in tuple
→ value

enumerate(tuple)
→ index + value
```

### for loop
### enumerate()

## 11. Membership Operators

Membership operators are used to check whether a value exists in a tuple.

### `in`

`in` returns `True` if the value exists in the tuple.

```python
languages = ("Python", "Django", "FastAPI")

print("Python" in languages)
# True

print("Java" in languages)
# False
```

## 12. Tuple Concatenation
using + operator 

Tuple concatenation means combining two or more tuples using the `+` operator.

### Example

```python
a = (1, 2, 3)
b = (4, 5, 6)

result = a + b

print(result)
# (1, 2, 3, 4, 5, 6)
```

### + operator
 is used to combine two tuple into a single tuple

## 13. Tuple Repetition

Tuple repetition is used to repeat the elements of a tuple using the `*` operator.

### Example

```python
numbers = (1, 2)

result = numbers * 3

print(result)
# (1, 2, 1, 2, 1, 2)
```
### * operator
to repeat the elements of tuple using * 

## 14. Tuple Comparison

Tuples can be compared using comparison operators such as:

`==`, `!=`, `<`, `>`, `<=`, `>=`

### Equality

Two tuples are equal when they contain the same elements in the same order.

```python
a = (1, 2, 3)
b = (1, 2, 3)

print(a == b)
# True
```
## 15. Built-in Functions with Tuples

Python provides several built-in functions that can be used with tuples.

### `len()`

Returns the number of elements.

```python
marks = (85, 72, 91, 68)

print(len(marks))
# 4
```
### min()
``min``
return smallest number of elements
### max()
return highest number of elements.
### sum()
total of numeric elements

## 16. List ↔ Tuple Conversion

using list(tup)
using tuple(list)
## 16. List ↔ Tuple Conversion

Python provides built-in functions to convert between lists and tuples.

### Tuple → List

Use `list()`:

```python
languages = ("Python", "Django", "FastAPI")

languages_list = list(languages)

print(languages_list)
# ["Python", "Django", "FastAPI"]
```

## 17. Functions vs Methods
### Function

A function is called directly and can operate on data passed to it.

```python
numbers = (10, 20, 30)

print(len(numbers))
print(sum(numbers))
```
### methods
A method is associated with an object/type and is called using dot . notation.
languages = ("Python", "Django", "Python")

print(languages.count("Python"))
print(languages.index("Django"))

###  Tuple vs List

Add:

```markdown
## 18. Tuple vs List

| Feature | List | Tuple |
|---|---|---|
| Syntax | `[]` | `()` |
| Ordered | Yes | Yes |
| Mutable | Yes | No |
| Duplicates | Allowed | Allowed |
| Indexing | Yes | Yes |
| Slicing | Yes | Yes |
| `append()` | Yes | No |
| `remove()` | Yes | No |
| `count()` | Yes | Yes |
| `index()` | Yes | Yes |

### 🧠 Main Difference

List → mutable

Tuple → immutable
### Tuple Method vs Built-in Function

## 19. Mini Project
Student Marks Tuple Analyzer

## 20. Quick Revision