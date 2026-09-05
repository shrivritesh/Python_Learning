# Exception Handling in Python

Exception handling in Python allows us to handle runtime problems gracefully instead of allowing the program to terminate unexpectedly.

## 📚 Topics Covered

* Error vs Exception
* Types of Errors

  * Syntax Error
  * Runtime Error / Exception
  * Logical Error
* `try`
* `except`
* Multiple `except` blocks
* `else`
* `finally`
* `raise`
* `except ... as e`
* `Exception` class
* Specific vs Broad Exception Handling
* Basic Exception Hierarchy
* Custom Exceptions — Concept
* Exception Propagation

## 🔹 Basic Exception Handling

```python
try:
    # Risky code
    number = int(input("Enter a number: "))
except ValueError:
    print("Please enter a valid number.")
```

## 🔹 `else`

The `else` block executes only when the `try` block completes successfully without raising an exception.

```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input")
else:
    print("Valid input:", number)
```

## 🔹 `finally`

The `finally` block executes whether an exception occurs or not.

```python
try:
    number = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Program finished")
```

## 🔹 `raise`

`raise` is used to explicitly raise an exception.

```python
age = -5

if age < 0:
    raise ValueError("Age cannot be negative")
```

## 🔹 Exception Object with `as e`

`as e` stores the caught exception object in the variable `e`.

```python
try:
    number = int("hello")
except ValueError as e:
    print(e)
```

## 🔹 Exception Propagation

Exception propagation occurs when an exception is not handled in the current function and moves back through the call stack until a matching exception handler is found.

```python
def calculate():
    return 100 / 0

def process():
    calculate()

try:
    process()
except ZeroDivisionError:
    print("Handled")
```

Flow:

```text
calculate()
    ↓
process()
    ↓
try/except
    ↓
Exception handled
```

## 🧠 Important Exception Hierarchy

```text
BaseException
    ↓
Exception
    ├── ValueError
    ├── TypeError
    ├── IndexError
    ├── KeyError
    └── ZeroDivisionError
```

## 💻 Practice

The `practice.py` file contains hands-on exercises covering:

* Basic `try/except`
* Multiple exceptions
* `else`
* `finally`
* `raise`
* Input validation
* Calculator error handling
* Exception propagation

## 🎯 Interview Preparation

### What is an exception?

An exception is an abnormal event that occurs during program execution and disrupts the normal flow of a program.

### What is exception handling?

Exception handling is the mechanism used to handle runtime exceptions using constructs such as `try`, `except`, `else`, `finally`, and `raise`.

### What is exception propagation?

Exception propagation is the process in which an unhandled exception moves back through the call stack until a matching exception handler is found.

### Why prefer specific exceptions?

Specific exception handling makes code more precise, predictable, easier to debug, and prevents unrelated errors from being hidden.

---

**Status:** ✅ Completed

**Stage:** 2 — Intermediate

**Topic:** 01 — Exception Handling
