# 🐍 Python Strings

## 📍 Current Progress

- Stage: Stage 1
- Topic: Strings
- Status: Done
- Current Subtopic: Definition & Creation
- Next: String Indexing

---

# 📖 Definition

A **string in Python is an ordered and immutable sequence of Unicode characters used to represent and store textual data.**

Strings are objects of Python's built-in `str` class and are typically created using single (`' '`), double (`" "`), or triple (`''' '''` / `""" """`) quotes.

### Simple Definition

> **A string is an ordered, immutable sequence of characters used to store text.**
>
> String = Ordered + Immutable + Unicode + Text = OIUT.
### Example

```python
name = "Ritesh"
message = "Hello Python"

# 🔢 3. String Indexing

String indexing is used to access individual characters from a string.

Python uses **zero-based indexing**, which means the first character has index `0`.

### Example

```python
word = "Python"

print(word[0])  # P
print(word[1])  # y
print(word[5])  # n

Character:   P    y    t    h    o    n
Positive:    0    1    2    3    4    5


# 🔄 4. Negative String Indexing

Python allows us to access characters from the **end of a string** using negative indexes.

Negative indexing starts from `-1`.

### Example

```python
word = "Python"

print(word[-1])  # n
print(word[-2])  # o
print(word[-3])  # h
```

### Index Table

```text
Character:   P    y    t    h    o    n
Positive:    0    1    2    3    4    5
Negative:   -6   -5   -4   -3   -2   -1
```

### 🧠 Remember

> Positive indexing starts from the left at `0`.
>
> Negative indexing starts from the right at `-1`.

```text
First character → 0
Last character  → -1
```
"""

# ✂️ 5. String Slicing

String slicing is the process of extracting a portion (substring) of a string by specifying a range of indexes.

### Syntax

```python
string[start:stop]
```

- `start` → included
- `stop` → excluded

### Example

```python
word = "Python"

print(word[0:3])  # Pyt
print(word[1:5])  # ytho
```

### 🧠 Important Rule

> **Start is included, stop is excluded.**

For:

```python
word[1:5]
```

Python takes indexes:

```text
1 → 2 → 3 → 4
```

but does **not** include index `5`.

### Example

```text
Character:   P    y    t    h    o    n
Index:       0    1    2    3    4    5

word[1:5] → y t h o
```"""
# Example
word = "Python"
print(word[0:6:2]) # Output -> Pto


# 🔢 6. Slicing with Step

Slicing can also use a `step` value to control how many positions Python jumps while extracting characters.

### Syntax

```python
string[start:stop:step]
```

- `start` → where to begin
- `stop` → where to stop (excluded)
- `step` → how many positions to jump

### Example

```python
word = "Python"

print(word[0:6:2])
# Pto
```

Indexes used:

```text
0 → 2 → 4

P → t → o
```

### 🧠 Remember

```text
start → included
stop  → excluded
step  → jump size
```

### More Examples

```python
word = "Python"

print(word[::1])   # Python
print(word[::2])   # Pto
print(word[1::2])  # yhn
```

# ✂️ 7. Omitting Start and Stop in Slicing

Python allows us to omit the `start` or `stop` value when slicing.

**Omit** means to leave something out or not specify it.

When a value is omitted, Python automatically uses the beginning or end of the string.

### Syntax

```python
string[:stop]
string[start:]
string[:]
```

### 1. Omitting Start

If `start` is omitted, slicing starts from the beginning.

```python
word = "Python"

print(word[:3])
# Pyt
```

This is equivalent to:

```python
word[0:3]
```

### 2. Omitting Stop

If `stop` is omitted, slicing continues until the end.

```python
print(word[2:])
# thon
```

### 3. Omitting Both

If both `start` and `stop` are omitted:

```python
print(word[:])
# Python
```

### 🧠 Remember

```text
[:stop]  → start omitted → beginning to stop
[start:] → stop omitted  → start to end
[:]      → both omitted  → entire string
```
# 🔄 8. Reverse a String

A string can be reversed using slicing with a negative step.

### Syntax

```python
string[::-1]
```

### Example

```python
word = "Python"

print(word[::-1])
# nohtyP
```

### 🧠 How it works

```text
[::-1]

start → omitted
stop  → omitted
step  → -1
```

Because the step is `-1`, Python moves from **right to left**.

```text
Python
  ↓
nohtyP
```

### Another Example

```python
text = "Hello"

print(text[::-1])
# olleH
```

### 🧠 Remember

> `[::-1]` is a common way to reverse a string.



# 🔗 9. String Concatenation

**Concatenation** means joining two or more strings together.

Python uses the `+` operator to concatenate strings.

### Example

```python
first_name = "Ritesh"
last_name = "Srivastav"

full_name = first_name + " " + last_name

print(full_name)
# Ritesh Srivastav
```

The `" "` adds a space between the two strings.

### More Examples

```python
first = "Py"
second = "thon"

word = first + second

print(word)
# Python
```

### 🧠 Remember

```text
+ → joins strings
```

### ⚠️ Important

You cannot directly concatenate a string with an integer.

```python
age = 25

# This causes an error:
# print("Age: " + age)
```

Convert the integer to a string first:

```python
print("Age: " + str(age))
# Age: 25
```

# 🔁 10. String Repetition

String repetition means repeating a string multiple times.

Python uses the `*` operator to repeat a string.

### Syntax

```python
string * number
```

### Example

```python
print("Hi" * 3)
# HiHiHi

print("A" * 5)
# AAAAA
```

### Repeating Zero Times

If a string is multiplied by `0`, the result is an empty string.

```python
print("Python" * 0)
# ""
```

### Combining `*` and `+`

```python
print("Python" * 2 + "!")
# PythonPython!
```

### 🧠 Remember

```text
+ → concatenate/join strings
* → repeat a string
```

### ⚠️ Important

The `*` operator repeats a string only when the other operand is an integer.

```python
print("Hi" * 3)  # HiHiHi
```


# 🧰 11. String Methods

A **string method** is a function that belongs to a string object and performs an operation on that string.

String methods are called using:

```python
string.method()
```

For example:

```python
text.upper()
```

---

## 🔠 `.upper()`

`.upper()` converts all alphabetic characters in a string to uppercase.

### Example

```python
word = "Ritesh"

result = word.upper()

print(result)
# RITESH
```

### 🧠 Important

`.upper()` does **not** modify the original string because strings are immutable.

```python
word = "python"

word.upper()

print(word)
# python
```

# 🔡 12. `.lower()`

`.lower()` converts all alphabetic characters in a string to lowercase.

### Syntax

```python
string.lower()
```

### Example

```python
word = "PyThOn"

result = word.lower()

print(result)
# python
```

### 🧠 Important

`.lower()` does **not** modify the original string because strings are immutable.

```python
word = "PYTHON"

word.lower()

print(word)
# PYTHON
```

To store the result:

```python
word = word.lower()

print(word)
# python
```

### 🆚 `.upper()` vs `.lower()`

```text
.upper() → converts letters to uppercase
.lower() → converts letters to lowercase
```
# 🔤 13. `.capitalize()`

`.capitalize()` converts the **first character** of a string to uppercase and converts the remaining characters to lowercase.

### Syntax

```python
string.capitalize()
```

### Example

```python
text = "PYTHON PROGRAMMING"

result = text.capitalize()

print(result)
# Python programming
```

### 🧠 Remember

```text
.upper()       → ALL letters uppercase
.lower()       → ALL letters lowercase
.capitalize()  → First character uppercase, rest lowercase
```

### Important

`.capitalize()` does **not** modify the original string because strings are immutable.

```python
text = "hello WORLD"

result = text.capitalize()

print(result)
# Hello world

print(text)
# hello WORLD
```

# 🔤 14. `.title()`

`.title()` converts the first character of **each word** to uppercase and the remaining characters of each word to lowercase.

### Syntax

```python
string.title()
```

### Example

```python
text = "welcome to python world"

result = text.title()

print(result)
# Welcome To Python World
```

### 🆚 `.capitalize()` vs `.title()`

```text
.capitalize() → first character of the string uppercase
.title()      → first character of each word uppercase
```

Example:

```python
text = "hello python world"

print(text.capitalize())
# Hello python world

print(text.title())
# Hello Python World
```

### 🧠 Remember

> `capitalize()` → one beginning  
> `title()` → every word

# ✂️ 15. `.strip()`

`.strip()` removes whitespace from the **beginning and end** of a string.

It does not remove spaces between words.

### Syntax

```python
string.strip()
```

### Example

```python
text = "   Python Programming   "

result = text.strip()

print(result)
# Python Programming
```

### What does `.strip()` remove?

```text
"   Python   "
^^^       ^^^
spaces    spaces
```

Result:

```text
"Python"
```

But:

```python
text = "Python   Programming"

print(text.strip())
```

Result:

```text
"Python   Programming"
```

The spaces between words remain.

### 🧠 Remember

```text
strip() → removes whitespace from both ends
```

`.strip()` does **not** modify the original string because strings are immutable.


# ✂️ 16. `.lstrip()` and `.rstrip()`

These methods remove whitespace from only one side of a string.

## `.lstrip()`

`.lstrip()` removes whitespace from the **left side** (beginning) of a string.

### Example

```python
text = "   Python   "

result = text.lstrip()

print(result)
# Python   
```

### Remember

```text
lstrip() → left side
```

---

## `.rstrip()`

`.rstrip()` removes whitespace from the **right side** (end) of a string.

### Example

```python
text = "   Python   "

result = text.rstrip()

print(result)
#    Python
```

### 🆚 Difference

```text
strip()  → both sides
lstrip() → left side
rstrip() → right side
```

### 🧠 Memory Trick

```text
L → Left
R → Right
```

These methods do **not** modify the original string because strings are immutable.

# 🔄 17. `.replace()`

`.replace()` is used to replace one part of a string with another string.

### Syntax

```python
string.replace(old, new)
```

- `old` → text to replace
- `new` → replacement text

### Example

```python
text = "I love Django"

result = text.replace("Django", "Python")

print(result)
# I love Python
```

### Replacing Multiple Occurrences

```python
text = "Python is easy. I love Python."

result = text.replace("Python", "Java")

print(result)
# Java is easy. I love Java.
```

By default, `.replace()` replaces **all matching occurrences**.

### Using the `count` Argument

Syntax:

```python
string.replace(old, new, count)
```

The third argument controls the **maximum number of replacements**.

Example:

```python
text = "Python Python Python"

result = text.replace("Python", "Java", 2)

print(result)
# Java Java Python
```

### 🧠 Important

`.replace()` does not modify the original string because strings are immutable.

```python
text = "Hello"

text.replace("Hello", "Hi")

print(text)
# Hello
```

To store the result:

```python
text = text.replace("Hello", "Hi")
```
# ✂️ 18. `.split()`

`.split()` breaks a string into multiple parts and returns those parts as a **list**.

### Syntax

```python
string.split(separator)
```

### Example

```python
text = "I love Python"

words = text.split()

print(words)
# ['I', 'love', 'Python']
```

### 🧠 Return Type

`.split()` returns a **list**, not a string.

```python
result = "Python is easy".split()

print(type(result))
# <class 'list'>
```

### Without a Separator

When no separator is provided, `.split()` separates the string using **whitespace** by default.

```python
text = "Python is very easy"

print(text.split())
# ['Python', 'is', 'very', 'easy']
```

### Using a Separator

You can specify a separator:

```python
text = "apple,banana,mango"

print(text.split(","))
# ['apple', 'banana', 'mango']
```

### 🧠 Remember

```text
String
   ↓
.split()
   ↓
List
```

# 🔗 19. `.join()`

`.join()` is used to combine multiple strings into a single string using a separator.

### Syntax

```python
separator.join(iterable)
```

### Example

```python
words = ["I", "love", "Python"]

result = " ".join(words)

print(result)
# I love Python
```

Here:

```text
" " → separator
```

The space is placed between each string.

### More Examples

Using a hyphen:

```python
words = ["Python", "is", "easy"]

result = "-".join(words)

print(result)
# Python-is-easy
```

Using no separator:

```python
letters = ["P", "y", "t", "h", "o", "n"]

result = "".join(letters)

print(result)
# Python
```

### 🆚 `.split()` vs `.join()`

```text
.split() → String → List
.join()  → List/iterable of strings → String
```

Example:

```python
text = "I love Python"

words = text.split()
# ['I', 'love', 'Python']

result = " ".join(words)
# "I love Python"
```

### 🧠 Remember


> `.split()` breaks a string apart.
>
> `.join()` puts strings back together.
>
> # 🔍 20. `.find()`

`.find()` searches for a substring inside a string and returns the **index (position) of its first occurrence**.

### Syntax

```python
string.find(substring)
```

### Example

```python
text = "Python is easy"

print(text.find("Python"))
# 0

print(text.find("is"))
# 7
```

### If the Substring Is Not Found

`.find()` returns `-1` if the substring is not found.

```python
text = "Python is easy"

print(text.find("Java"))
# -1
```

### 🧠 Remember

```text
.find() → WHERE is it?
```

It returns the position/index, not `True` or `False`.

### Example

```python
text = "banana"

print(text.find("a"))
# 1
```

The first `"a"` is at index `1`.

### ⚠️ Important

`.find()` returns the position of the **first occurrence** only.

```python
text = "banana"

print(text.find("na"))
# 2
```

# 🔢 21. `.count()`

`.count()` counts how many times a character or substring appears in a string.

### Syntax

```python
string.count(substring)
```

### Example

```python
text = "banana"

print(text.count("a"))
# 3

print(text.count("na"))
# 2

print(text.count("z"))
# 0
```

### 🧠 Remember

```text
.find()  → WHERE? → returns index
.count() → HOW MANY? → returns number
```

### Example

```python
text = "Python is easy. Python is powerful."

print(text.count("Python"))
# 2

print(text.count("is"))
# 2
```

If the substring does not exist, `.count()` returns `0`.

```python
text.count("Java")
# 0
```
# 🔍 22. `.startswith()`

`.startswith()` checks whether a string starts with a specific substring.

It returns a Boolean value:

```text
True
False
```

### Syntax

```python
string.startswith(value)
```

### Example

```python
text = "Python Programming"

print(text.startswith("Python"))
# True

print(text.startswith("Programming"))
# False
```

### Another Example

```python
filename = "python.py"

print(filename.startswith("python"))
# True
```

### 🧠 Remember

```text
.startswith() → checks the beginning of a string
```

It does **not** return the index.

It returns:

```text
True / False
```

# 🔍 23. `.endswith()`

`.endswith()` checks whether a string ends with a specific substring.

It returns a Boolean value:

```text
True
False
```

### Syntax

```python
string.endswith(value)
```

### Example

```python
text = "Python Programming"

print(text.endswith("Programming"))
# True

print(text.endswith("Python"))
# False
```

### Practical Example

Checking a file extension:

```python
filename = "notes.py"

print(filename.endswith(".py"))
# True
```

### 🧠 Remember

```text
.startswith() → checks the beginning
.endswith()   → checks the ending
```

Both return:

```text
True / False
```
# 🔢 24. `.isdigit()`

`.isdigit()` checks whether **all characters in a string are digits**.

It returns a Boolean value:

```text
True
False
```

### Syntax

```python
string.isdigit()
```

### Examples

```python
print("12345".isdigit())
# True

print("123a".isdigit())
# False

print("hello".isdigit())
# False
```

### Important Examples

```python
print("12.5".isdigit())
# False
```

Because `.` is not a digit.

```python
print("-123".isdigit())
# False
```

Because `-` is not a digit.

```python
print("123 45".isdigit())
# False
```

Because the space is not a digit.

### 🧠 Important

Even though `"123"` is a string:

```python
value = "123"

print(type(value))
# <class 'str'>
```

`.isdigit()` checks the **characters inside the string**, not the data type.

```python
value.isdigit()
# True
```

### Practical Example

```python
age = input("Enter your age: ")

if age.isdigit():
    print("Valid number")
else:
    print("Please enter digits only.")
```

### 🧠 Remember

> `.isdigit()` → Are all characters digits?
>
> # 🔄 25. String Looping

A string is an **iterable**, which means Python can go through its characters one by one.

### Definition

> **String looping is the process of iterating through a string character by character using a loop.**

### Example

```python
word = "Python"

for char in word:
    print(char)
```

Output:

```text
P
y
t
h
o
n
```

### 🧠 How It Works

Python takes one character at a time:

```text
char = "P"
char = "y"
char = "t"
char = "h"
char = "o"
char = "n"
```

### Important

`char` is just a variable name. You can use any valid variable name:

```python
word = "Python"

for letter in word:
    print(letter)
```

The result is the same.

### General Pattern

```python
for char in string:
    # perform an operation
```

### 🧠 Remember

```text
String → for loop → character by character
```

# 🔢 26. Counting Characters with a Loop

We can count the number of characters in a string by looping through each character and increasing a counter.

### Example

```python
word = "python"

count = 0

for char in word:
    count += 1

print(count)
# 6
```

### 🧠 How It Works

```text
p → count = 1
y → count = 2
t → count = 3
h → count = 4
o → count = 5
n → count = 6
```

### Important

We can also use:

```python
len(word)
```

But using a loop helps us understand how loops process each character individually.

### 🧠 Remember

```text
count = 0
     ↓
loop through characters
     ↓
count += 1
     ↓
final character count
```

# 🔢 27. Count a Specific Character

We can count how many times a specific character appears in a string using a `for` loop and an `if` condition.

### Example

```python
word = "Banana"

count = 0

for char in word:
    if char == "a":
        count += 1

print(count)
# 3
```

### 🧠 How It Works

The loop checks each character:

```text
B → not "a"
a → count = 1
n → not "a"
a → count = 2
n → not "a"
a → count = 3
```

### General Pattern

```python
count = 0

for char in word:
    if char == target:
        count += 1
```

### 🧠 Remember

```text
for      → checks every character
if       → checks whether it matches
count += 1 → increases the count
```

# 🔤 28. Count Vowels

We can count vowels in a string by checking whether each character exists inside `"aeiou"`.

### Example

```python
word = "programming"

count = 0

for char in word:
    if char in "aeiou":
        count += 1

print("Number of vowels:", count)
# Number of vowels: 3
```

### 🧠 How It Works

For `"programming"`:

```text
p → consonant
r → consonant
o → vowel → count = 1
g → consonant
r → consonant
a → vowel → count = 2
m → consonant
m → consonant
i → vowel → count = 3
n → consonant
g → consonant
```

### `in` Operator

```python
if char in "aeiou":
```

checks whether the current character exists inside `"aeiou"`.

### 🧠 Remember

```text
"a" → vowel
"e" → vowel
"i" → vowel
"o" → vowel
"u" → vowel
```

# 🔤 29. Count Vowels and Consonants

We can count vowels and consonants using two counters and an `if-else` condition.

### Example

```python
word = "programming"

vowels = 0
consonants = 0

for char in word:
    if char in "aeiou":
        vowels += 1
    else:
        consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
```

Output:

```text
Vowels: 3
Consonants: 8
```

### 🧠 How It Works

```text
if char in "aeiou"
        ↓
      vowel
        ↓
   vowels += 1

otherwise
        ↓
   consonant
        ↓
 consonants += 1
```

### Important

This simple version assumes the string contains only alphabetic characters.

For example, spaces, numbers, or punctuation would also go into the `else` block.

Later, we can improve this using methods such as `.isalpha()`.

### 🧠 Remember

```text
if    → vowel
else  → consonant
```  
# 🔠 30. Count Uppercase and Lowercase

We can count uppercase and lowercase characters by checking each character with `.isupper()` and `.islower()`.

### Example

```python
text = "PyThOn Programming"

uppercase = 0
lowercase = 0

for char in text:
    if char.isupper():
        uppercase += 1
    elif char.islower():
        lowercase += 1

print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
```

Output:

```text
Uppercase: 4
Lowercase: 13
```

Spaces are neither uppercase nor lowercase, so they are not counted.

### 🧠 Important

Check the **current character**:

```python
char.isupper()
char.islower()
```

Not the entire string:

```python
word.isupper()
word.islower()
```

Inside a loop, `char` represents the current character.

### Example

For:

```text
PyThOn
```

```text
P → uppercase
y → lowercase
T → uppercase
h → lowercase
O → uppercase
n → lowercase
```

### 🧠 Remember

```text
.isupper() → checks if the current character is uppercase
.islower() → checks if the current character is lowercase
```
