## 1. What is a Function?

A function is a reusable block of code that performs a specific task.

In Python, a function is defined using the `def` keyword, followed by the function name and parentheses `()`.


### Syntax

```python
def function_name():
    # code
A function is executed by calling its name:
function_name()
```

## 2. Parameters and Arguments

A **parameter** is a variable written inside the function definition.

An **argument** is the actual value passed to the function when it is called.

### Example

```python
def greet(name):
    return f"Hello {name}"

result = greet("Ritesh")

print(result)
# Hello Ritesh
```

Here:
name → parameter
"Ritesh" → argument

### Multiple Parameters

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
# 30
```

Here:

```text
a, b → parameters
10, 20 → arguments
```

### 🧠 Remember

```text
Function definition → Parameters
Function call        → Arguments
```

## 3. Return Values

`return` sends a value back to the caller of a function.

### Example

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
# 30
```

The returned value can be stored in a variable.

### `return` vs `print()`

`print()` displays a value on the screen:

```python
def add(a, b):
    print(a + b)

add(10, 20)
# 30
```

`return` sends the value back to the caller:

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
# 30
```

### 🧠 Remember

```text
print()  → displays a value
return   → sends a value back to the caller
```

## 4. Default Parameters

A default parameter has a default value assigned in the function definition.

A default parameter provides a fallback value when no argument is supplied.
```python
def greet(name="Guest"):
    print("Hello", name)

greet()
# Hello Guest

greet("Ritesh")
# Hello Ritesh
```
## 5. Keyword Arguments

A keyword argument is an argument passed using the parameter name.
during a function call value passed through arguments dont need to be in the order of parameter function definition.

The order of keyword arguments does not matter:
### Example

```python
def introduce(name, age):
    print(name, age)

introduce(name="Ritesh", age=25)

--> all the keyword should match the parameter in the function definition.
if we don't know the sequence - we use keyword argument in which we mentioned the variable name itself.
```

## 6. `*args` — Variable-Length Arguments

`*args` is used when a function needs to accept a variable number of positional arguments.

It allows us to pass any number of positional arguments to the function.

The extra positional arguments are collected into a tuple.

### Example

```python
def show(*args):
    print(args)

show(10, 20, 30)
```

## 7. `**kwargs` — Variable-Length Keyword Arguments

`**kwargs` allows a function to accept a variable number of keyword arguments.

The keyword arguments are stored inside a dictionary.

### Example

```python
def show(**kwargs):
    print(kwargs)

show(name="Ritesh", age=25)

*args   → accepts extra positional arguments → stored as tuple
**kwargs → accepts extra keyword arguments → stored as dictionary
```


## 8. Positional vs Keyword Arguments

### Positional Arguments

Arguments are matched according to their position.

```python
def student(name, age):
    print(name, age)

student("Ritesh", 25)
```

Here:

```text
"Ritesh" → name
25       → age
```

### Keyword Arguments

Arguments are matched using the parameter name.

```python
student(age=25, name="Ritesh")
```

The order does not matter because Python matches the arguments by parameter name.

Output:

```text
Ritesh 25
```

### Comparison

```python
# Positional
student("Ritesh", 25)

# Keyword
student(name="Ritesh", age=25)

# Keyword — order changed
student(age=25, name="Ritesh")
```

All three produce:

```text
Ritesh 25
```

### 🧠 Remember

```text
Positional → matched by position
Keyword    → matched by parameter name
```

## 9. Positional and Keyword Arguments Together

A function can receive both positional and keyword arguments in the same function call.

### Example

```python
def student(name, age, city):
    print(name, age, city)

student("Ritesh", age=25, city="Delhi")
```

Output:

```text
Ritesh 25 Delhi
```

Here:

```text
"Ritesh"     → positional argument
age=25       → keyword argument
city="Delhi" → keyword argument
```

### Positional Arguments Must Come First

This is valid:

```python
student("Ritesh", city="Delhi", age=25)
```

This is invalid:

```python
student(name="Ritesh", 25, "Delhi")
```

A positional argument cannot come after a keyword argument.

### 🧠 Remember

```text
Positional arguments → must come first
Keyword arguments    → come after positional arguments
```

### Example

```python
student("Ritesh", age=25, city="Delhi")
```

The keyword arguments can be in any order:

```python
student("Ritesh", city="Delhi", age=25)
```


## 10. Keyword-Only Arguments

Keyword-only arguments are parameters that must be passed using their parameter names.

A `*` is used before the keyword-only parameters.

### Example

```python
def student(name, *, age, city):
    print(name, age, city)

student("Ritesh", age=25, city="Delhi")