# Python Sets

## 1. What is a Set?

A set is a built-in, mutable, unordered collection in Python
that is used to store unique elements.

Sets do not allow duplicate elements.

### Example

```python
languages = {"Python", "Django", "FastAPI", "Python"}

print(languages)
# {"Python", "Django", "FastAPI"}
```

## 2. Creating a Set

A set is created using curly braces `{}` with elements separated by commas.

### Example

```python
languages = {"Python", "Django", "FastAPI"}

print(languages)
```

A set automatically removes duplicate values.

```python
languages = {"Python", "Django", "Python", "Docker", "Django"}

print(languages)
```

The result contains only unique values.

### Empty Set

```python
empty = set()
```

`{}` creates an empty dictionary, not an empty set.

```python
empty = {}

print(type(empty))
# <class 'dict'>
```

To create an empty set:

```python
empty = set()

print(type(empty))
# <class 'set'>
```

### 🧠 Remember

```text
{}     → empty dictionary
set()  → empty set
```

## 3. Set Methods

### `add()`

`add()` is used to add one element to a set.

```python
languages = {"Python", "Django"}

languages.add("Docker")
languages.add("FastAPI")

print(languages)

# If the element already exists, add() does not create a duplicate.

### `update()`

`update()` is used to add multiple elements from an iterable to a set.

```python
languages = {"Python", "Django"}

languages.update(["FastAPI", "Docker"])

print(languages)
```

### `pop()`

`pop()` removes and returns an arbitrary element from a set.

```python
numbers = {10, 20, 30}

removed = numbers.pop()

print(removed)
print(numbers)
# ++++++++++++++++++++++++++++++++++++++++++++++
```

### 4.Set Membership
# In
check wheather element is exist in set.
```python'
languages = {"Python", "Django", "FastAPI"}

print("Python" in languages)
# True

print("Java" in languages)
# False

```
## not in 
check wheather elements does not exist.
print("Java" not in languages)
# True

print("Python" not in languages)
# False

## 5. Set Operations
Set union()
union() combines the elements of two or more sets.

Example:
union() combines the elements of two or more sets.

a = {1, 2, 3}
b = {3, 4, 5}

result = a.union(b)
print(result) # {1, 2, 3, 4, 5}

## 9. Set `intersection()`

`intersection()` returns the elements that are common to two or more sets.

### Example

```python
a = {1, 2, 3}
b = {3, 4, 5}

result = a.intersection(b)

print(result)
# {3}

## 10. Set `difference()`

`difference()` returns the elements that are present in the first set but not in the second set.

### Example

```python
a = {1, 2, 3}
b = {3, 4, 5}

result = a.difference(b)

print(result)
# {1, 2}
The - operator can also be used.


---

# 🟢 Section 11 — `symmetric_difference()`

This one is slightly different.

It returns elements that are in **either set, but NOT in both**.

Example:

```python id="1v8q3k"
a = {1, 2, 3}
b = {3, 4, 5}

result = a.symmetric_difference(b)

print(result) # {1, 2, 4, 5}

union               → everything
intersection        → common
difference          → only first
symmetric_difference → everything except common

## Set Comprehension

Set comprehension is a concise way to create a new set using an expression, a loop, and optionally a condition.

### Syntax

```python
{expression for item in iterable}


---

# 🎯 Set Mini-Project

Now we're at the **final major part of Sets**.

## Unique Technology Analyzer

Given:

```python
students = [
    ("Ritesh", "Python"),
    ("Amit", "Java"),
    ("Rahul", "Python"),
    ("Priya", "JavaScript"),
    ("Neha", "Python"),
    ("Aman", "JavaScript")
]