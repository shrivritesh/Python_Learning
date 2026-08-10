# 🔀 Conditionals

This is **Topic 5** of my Python learning journey.

Conditional statements allow a Python program to **make decisions based on whether a condition is `True` or `False`**.

---

## 📌 What I Learned

* What conditional statements are
* `if` statement
* `else` statement
* `elif` statement
* Conditions and Boolean values
* Comparison operators with conditionals
* Multiple conditions
* Indentation in Python
* Conditional statements with user input
* Building an Age Category Checker

---

# 🔹 1. What is a Conditional?

A **conditional statement** allows a program to make a decision based on a condition.

A condition produces either:

```text
True
```

or:

```text
False
```

### Example

```python
age = 20

if age >= 18:
    print("Adult")
```

Python checks:

```text
20 >= 18 → True
```

Because the condition is `True`, Python executes the `print()` statement.

Output:

```text
Adult
```

---

# 🔹 2. The `if` Statement

The `if` statement executes a block of code **only when its condition is `True`**.

### Syntax

```python
if condition:
    # code to execute
```

### Example

```python
marks = 75

if marks >= 40:
    print("Pass")
```

Output:

```text
Pass
```

---

# 🔹 3. The `else` Statement

`else` executes when the `if` condition is `False`.

### Example

```python
age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Output:

```text
Minor
```

### Memory Trick

```text
if   → If the condition is True
else → Otherwise
```

---

# 🔹 4. The `elif` Statement

`elif` means **"else if"**.

It is used when there are **multiple possible conditions**.

### Example

```python
marks = 75

if marks >= 80:
    print("Excellent")
elif marks >= 60:
    print("Good")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")
```

Output:

```text
Good
```

Python checks conditions from **top to bottom**.

Once it finds a `True` condition, it executes that block and skips the remaining conditions.

---

# 🔹 5. Conditional Structure

A conditional can have:

```python
if condition:
    # code

elif another_condition:
    # code

else:
    # code
```

### Meaning

```text
if    → Check the first condition
elif  → Check another condition
else  → Run if all conditions are False
```

---

# 🔹 6. Conditions and Comparison Operators

Conditionals commonly use comparison operators.

| Operator | Meaning                  |
| -------- | ------------------------ |
| `==`     | Equal to                 |
| `!=`     | Not equal to             |
| `>`      | Greater than             |
| `<`      | Less than                |
| `>=`     | Greater than or equal to |
| `<=`     | Less than or equal to    |

### Example

```python
age = 20

if age >= 18:
    print("Adult")
```

Here:

```python
age >= 18
```

is the condition.

The comparison produces:

```text
True
```

or:

```text
False
```

---

# 🔹 7. Conditionals with User Input

We can combine `input()` with conditionals.

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
```

If the user enters:

```text
16
```

Output:

```text
You are a minor
```

If the user enters:

```text
24
```

Output:

```text
You are an adult
```

---

# ⚠️ 8. Indentation

Python uses indentation to determine which code belongs to a conditional block.

### Correct

```python
if age >= 18:
    print("Adult")
```

### Incorrect

```python
if age >= 18:
print("Adult")
```

The code inside `if`, `elif`, or `else` should normally be indented by **4 spaces**.

---

# 🔹 9. How Python Makes a Decision

Example:

```python
age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Python follows this process:

```text
age = 16
   ↓
16 >= 18
   ↓
False
   ↓
Skip if block
   ↓
Run else block
   ↓
"Minor"
```

---

# 🧠 10. Important Concept

Remember the connection:

```text
Comparison Operator
        ↓
True / False
        ↓
Conditional
        ↓
Decision
```

Example:

```python
age >= 18
```

produces:

```text
True / False
```

Then:

```python
if age >= 18:
```

uses that result to make a decision.

---

# 🛠️ 11. Mini Project — Age Category Checker

### File

```text
age_checker.py
```

The program asks the user for their age and categorizes them.

### Rules

| Age     | Category |
| ------- | -------- |
| `0–12`  | Child    |
| `13–17` | Teenager |
| `18+`   | Adult    |

### Example

```text
Enter your age: 16
You are a Teenager.
```

### Concepts Used

```text
input()
int()
variables
if
elif
else
comparison operators
print()
```


```

### File Purpose

| File             | Purpose                                           |
| ---------------- | ------------------------------------------------- |
| `README.md`      | Topic overview, definitions, examples and project |
| `notes.md`       | Detailed learning notes and active recall         |
| `practice.py`    | Practice questions and experiments                |
| `age_checker.py` | Age Category Checker mini-project                 |

---

# 📊 13. Topic Progress

* [x] Conditional concept
* [x] `if`
* [x] `else`
* [x] `elif`
* [x] Conditions
* [x] Comparison operators with conditions
* [x] Indentation
* [x] User input with conditions
* [ ] Age Category Checker
* [ ] Challenge
* [ ] Final Quiz

## 🔄 Topic 5 — Conditionals

**Currently learning**

---

# 🐍 Python Learning Journey

### Previous Topics

**Topic 1 — Setup** ✅

**Topic 2 — Variables & Data Types** ✅

**Topic 3 — Operators** ✅

**Topic 4 — Input & Output** ✅

### Current Topic

**Topic 5 — Conditionals** 🔄

### Next Topic

**Topic 6 — Loops**
