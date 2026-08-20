# 🐍 Python Strings

## 📍 Current Progress

- Stage: Stage 1
- Topic: Strings
- Status: 🔄 In Progress
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

###🔢 String Indexing

String indexing is used to access individual characters from a string.

Python uses **zero-based indexing**, which means the first character has index `0`.

# ##🔄 Negative String Indexing

Python also allows us to access characters from the end of the string using negative indexes.
"python" 

### Example

```python
word = "Python"
Character:   P    y    t    h    o    n
Positive:    0    1    2    3    4    5
Negative:   -6   -5   -4   -3   -2   -1


"""
# String slicing:
Slicing is the process of extracting a portion (subsring) of string by specifying a range of indices.

# Syntax:
string[start:stop]
python[0:3]
pyt

start = included
stop = excluded

# Slicing with Step 

syntax:
[start:stop:step]

start → where to begin
stop → where to stop (excluded)
step → how many positions to jump

"""
# Example
word = "Python"
print(word[0:6:2]) # Output -> Pto

# ✂️ Omitting Start and Stop in Slicing

Python allows us to omit the `start` or `stop` value when slicing.
# Defination
Omit means to leave something out or not specify it. In Python string slicing, we can omit the start or stop index, and Python uses the beginning or end of the string automatically.

Example:
word = "Python"

word[:3]   # start is omitted → "Pyt"
word[2:]   # stop is omitted → "thon"
word[:]    # both are omitted → "Python"

Omit = not specifying / leaving something out.
## 1. Omitting Start
If the start index is omitted, slicing starts from the beginning of the string.

### Syntax
[:stop]       → start omitted
[start:]      → stop omitted
[:]            → both omitted
omit both
string[:]

```python
string[:stop]

When the step is positive: word[0:5:1] -->Python moves left → right.
When the step is negative: word[::-1] --> Python moves right -> left

# 🔗 String Concatenation

**Concatenation** means joining two or more strings together.

Python uses the `+` operator to concatenate strings.

### Example

```python
first_name = "Ritesh"
last_name = "Srivastav"

full_name = first_name + " " + last_name

print(full_name)

The " " adds a space between the two strings.

🟢String Repetition

# 🔁 String Repetition

String repetition means repeating a string multiple times.

Python uses the `*` operator to repeat a string.

## Syntax

```python
string * number
Repeating Zero Times

If a string is multiplied by 0, the result is an empty string.

🟢 String Method:

A string method is a function that belongs to a string object and can perform an operation on that string.

string.upper() --> converts all alphabetic characters in the string to uppercase.

word = "Ritesh"
print(word.upper())

🟢 String Method: .lower()

.lower() converts all alphabetic characters in a string to lowercase.

Syntax:
string.lower()

.lower() does not modify the original string.

.capitalize():

Makes the first character uppercase and converts the remaining characters to lowercase.

capitalize() = only the beginning gets capitalized.

text = "PYTHON PROGRAMMING"
result = text.capitalize()
print(result)
# Python programming

.upper()       → ALL UPPERCASE
.lower()       → all lowercase
.capitalize()  → First uppercase, rest lowercase

.upper() → converts all alphabetic characters to uppercase. ✅ 

.lower() → converts all alphabetic characters to lowercase. ✅ 

.capitalize() → converts the first character to uppercase and the remaining characters to lowercase. ✅ 

.upper() modifies the original? → No, because strings are immutable. ✅ 

.lower() modifies the original? → No. ✅ 

.capitalize() modifies the original? → No. ✅ 

 Difference: 

.upper() → all letters uppercase 

.capitalize() → first character uppercase, remaining characters lowercase ✅ 


.title() converts the first character of each word to uppercase and the remaining characters of each word to lowercase.

.strip() is used to remove whitespace from the beginning and end of a string.
.replace() is used to replace one part of a string with another string.


# ✂️ `.split()`

`.split()` is used to **break a string into multiple parts** and returns those parts as a **list**.
.split() returns a list, not a string.

## Syntax

```python
string.split(separator)

🔗 .join()

.join() is used to combine multiple strings into a single string.

🆚 .split() vs .join()
.split() → String → List
.join()  → List → String

.split() → breaks a string into multiple parts and returns those parts as a list. ✅
Return type → list ✅
Without a separator → splits the string on whitespace by default. ✅
.join() → combines multiple strings into a single string. ✅
.join() commonly works with → a list/iterable of strings. ✅
" ".join(["I", "love", "Python"]) → "I love Python" ✅

Difference:

split() → String → List
join()  → Strings/List → String

.find() is used to search for a substring inside a string and returns its index (position).
.count() is used to count how many times a character or substring appears in a string.

Syntax:
string.count(substring)

🟢 .startswith()

.startswith() checks whether a string starts with a specific substring.
It returns a Boolean:
Syntax:
string.startswith(value)

example:
text = "Python Programming"
print(text.startswith("Python")) #output : True

🟢 .endswith()
.endswith() checks whether a string ends with a specific substring.
It returns a Boolean:
text = "Python Programming"
print(text.startswith("Programming")) #output : True


.isdigit() it checks wheather the strings contains only digit.