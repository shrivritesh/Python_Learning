# Python Dictionaries

## 1. What is a Dictionary?

A dictionary is a mutable collection of key-value pairs in Python.

Each key is unique and is used to access its corresponding value.

we can think of it like a regular dictionary we lookup at word(key) and get its defination(the value).

syntax:
{"key":"value"}


### Example

```python
student = {
    "name": "Ritesh",
    "age": 25,
    "language": "Python"
}
```

Here:

```text
key       → value
"name"    → "Ritesh"
"age"     → 25
"language"→ "Python"
```

### Important Properties

- **Mutable** → dictionary values can be added, changed, or removed.
- **Key-value pairs** → data is stored as `key: value`.
- **Keys are unique** → duplicate keys are not stored separately.
- **Accessed by keys** → values are accessed using their keys.
- **Values can be duplicated** → different keys can have the same value.

### Accessing a Value

```python
student = {
    "name": "Ritesh",
    "age": 25
}

print(student["name"]) # Using key
# Ritesh

print(student["age"]) # using value
# 25
```

### 🧠 Remember

```text
Dictionary → key : value

student["name"]
→ get the value associated with "name"
```

### Dictionary vs List vs Tuple vs Set

| Feature | List | Tuple | Set | Dictionary |
|---|---|---|---|---|
| Mutable | Yes | No | Yes | Yes |
| Duplicates | Yes | Yes | No | Keys: No |
| Access | Index | Index | No index | Key |
| Syntax | `[]` | `()` | `{}` | `{key: value}` |

## Section 2
## 2. Creating a Dictionary

A dictionary is created using curly braces `{}` with key-value pairs.

### Syntax

```python
dictionary = {
    key: value,
    key: value
}
```
### 🧠 Remember

```text
Dictionary → key : value

dictionary[key]
→ returns the value associated with that key
```

### ⚠️ Important

If you try to access a key that doesn't exist:

```python
print(student["city"])
```

Python raises:

```text
KeyError
```

## 3. Adding and Updating Items

Dictionaries are mutable, so we can add new key-value pairs and change existing values.

### Adding a New Item

Use:

```python
dictionary[key] = value
```

Example:

```python
student = {
    "name": "Ritesh",
    "age": 25
}

student["language"] = "Python"

print(student)
```

Result:

```python
{
    "name": "Ritesh",
    "age": 25,
    "language": "Python"
}
```

### Updating an Existing Item

If the key already exists, its value is changed.

```python
student["age"] = 26

print(student)
```

Result:

```python
{
    "name": "Ritesh",
    "age": 26,
    "language": "Python"
}
```

### 🧠 Remember

```text
new key    → adds a new item
existing key → updates its value
```
## 4. `get()`

`get()` is used to safely access a value using its key.

### Example

```python
student = {
    "name": "Ritesh",
    "age": 25
}

print(student.get("name"))
# Ritesh
## 5. `keys()`

`keys()` returns a view containing all the keys of a dictionary.

### Example

```python
student = {
    "name": "Ritesh",
    "age": 25,
    "language": "Python"
}

print(student.keys())
# dict_keys(['name', 'age', 'language'])
```

## 6. `values()`

`values()` returns a view containing all the values of a dictionary.

### Example

```python
student = {
    "name": "Ritesh",
    "age": 25,
    "language": "Python"
}

print(student.values())
# dict_values(['Ritesh', 25, 'Python'])

```
## 
## 7. `items()`

`items()` returns a view containing all key-value pairs of a dictionary.

### Example

```python
student = {
    "name": "Ritesh",
    "age": 25,
    "language": "Python"
}

print(student.items())
# dict_items([
#     ('name', 'Ritesh'),
#     ('age', 25),
#     ('language', 'Python')
# ])

## 8. `update()`

`update()` is used to add new key-value pairs or update existing key-value pairs in a dictionary.

### Adding New Items

```python
student = {
    "name": "Ritesh",
    "age": 25
}

student.update({
    "language": "Python",
    "city": "Delhi"
})

print(student)
```

Output:

```python
{
    "name": "Ritesh",
    "age": 25,
    "language": "Python",
    "city": "Delhi"
}
```

### Updating Existing Items

If the key already exists, its value is updated.

```python
student.update({
    "age": 26
})

print(student)
```

`age` changes from `25` to `26`.

### 🧠 Remember

```text
update()
→ new key → adds it
→ existing key → updates its value
```

## 9. `pop()`

`pop()` removes a specific key-value pair from a dictionary and returns the removed value.

### Example

```python
student = {
    "name": "Ritesh",
    "age": 25,
    "language": "Python"
}

removed = student.pop("age")

print(removed)
# 25

print(student)
# {'name': 'Ritesh', 'language': 'Python'}
```

### Important

Dictionary `pop()` uses a **key**, not an index.

```python
student.pop("age")
# ✅

student.pop(1)
# ❌
```

If the key does not exist, `pop()` raises a `KeyError`.

```python
student.pop("city")
# KeyError
```

You can provide a default value:

```python
print(student.pop("city", "Not Found"))
# Not Found
```

### 🧠 Remember

```text
dict.pop(key)
→ removes the key-value pair
→ returns the removed value
```

## 10. `popitem()`

`popitem()` removes and returns the **last inserted key-value pair** from a dictionary.

### Example

```python
student = {
    "name": "Ritesh",
    "age": 25,
    "language": "Python"
}

result = student.popitem()

print(result)
# ('language', 'Python')

popitem() returns the removed key-value pair as a tuple.

print(student)
# {'name': 'Ritesh', 'age': 25}
```

## 11. `clear()`

`clear()` removes all key-value pairs from a dictionary.

### Example

```python
student = {
    "name": "Ritesh",
    "age": 25,
    "language": "Python"
}

student.clear()

print(student)
# {}
```

The dictionary still exists, but it is now empty.

### Return Value

`clear()` returns `None`.

```python id="k8v4p2"
result = student.clear()

print(result)
# None
```

### 🧠 Remember

```text
clear()
→ removes all items
→ dictionary becomes {}
→ returns None
```

## 12. Dictionary Membership

The `in` and `not in` operators check whether a key exists in a dictionary.

### `in`

```python
student = {
    "name": "Ritesh",
    "age": 25
}

print("name" in student)
# True

print("city" in student)
# False

print("Location", not in student)