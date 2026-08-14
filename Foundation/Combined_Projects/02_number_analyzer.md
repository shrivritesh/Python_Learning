# 🟢 Combined Project — Number Analyzer

## 🎯 Goal

Build a program that collects multiple numbers from the user
and analyzes them.

## 🧠 Concepts Used

- `while` loop
- `for` loop
- `input()`
- `int()`
- Lists
- `append()`
- `if / elif / else`
- `%` operator
- Counters
- Sum
- Largest / Smallest
- Input validation

## 🔄 Loop Strategy

### While Loop → Collect

The `while` loop repeatedly takes numbers from the user
and stores them in the `values` list.

```python
while count < num:
    number = int(input("Enter Number: "))
    values.append(number)
    count += 1