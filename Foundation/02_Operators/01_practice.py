# In Python programming, Operators in general are used to perform operations on values and variables.

# Operators: Special symbols like -, + , * , /, etc.
# Operands: Value on which the operator is applied.

"""

**Arithematic Operator :**
> Arithmetic operators are used to perform basic mathematical operations like addition, subtraction, multiplication and division.

In Python, the division operator (/) returns a floating-point result, while floor division (//) returns an integer result.

"""

"""
Q1.
What is:
10 + 5 --> 15

Q2.
What is:
10 - 3 --> 7

Q3.
What is:
5 * 4 --> 20

🟡 Medium Recall
Without using a calculator:
10 / 2
5.0

🔴 Challenge Recall

What is the difference between:
10 / 3 --> it will return output in float
and

10 // 3 --> it will return output integer
"""
# // Calculator
num1,num2 = 8,5

print(f"addition of two num is:{num1 + num2}")
print(f"substraction of two num is:{num1 - num2}")
print(f"multiplication of two num is:{num1 * num2}")
print(f"division of two num is:{num1 / num2}")


"""
Before we learn the remaining arithmetic operators, answer these.

🟢 Easy

What operator is used for:

Addition → for adding two numbers
Multiplication → for multiplying two numbers
Division → for dividing two numbers (numbers are basically operand on which we perform the mathematical operations)


🟡 Medium
Without running the code:
print(8 / 4)

What will be printed?
it will print --> 2.0

🔴 Challenge

Predict the output:
a = 12
b = 5

print(a % b)
output is 2
The % operator returns the remainder

🛠 Mini Challenge
Without running the code, tell me the output.
Q1.

print(2 ** 5) --> 2*2*2*2*2 --> 32

Q2.
print(9 % 4) --> 1 (% return remainder) 

Q3
print(15 // 4) --> 3

Q4
print(15 / 4) --> 3.75



🟢 Easy
Q1.Which operator gives the remainder? 
A1. % modulo operator gives the remainder

Q2.Which operator gives the power?
A2. Exponention ** gives the power

Q3.Which operator always returns a float?
A3./ real division operator always return float (eg : print(8/2)--> 4.0)

🟡 Medium

Without running the code:
print(18 % 7) --> 4

🔴 Challenge

Predict the output:

a = 4

print(a ** 3) - 4*4*4 = 64
print(a % 3) - 4 % 3 = 1
print(a // 3) - 4 // 3 = 1
print(a / 3) - 4 / 3 = 1.333

Write all 4 outputs in order.
64
1
1
1.3333


🧠 Active Recall (Very Important)

Before we move on, answer these without looking.

Q1

Complete the table.

Operator	Meaning
+	        Addition
-           Substraction
*	        Multiplication
/	        division(return float)
//	        floor division
%	        Modulus (Remainder)
**	        Power (Exponentiation)

Q2

Without running the code:

print(20 // 6) --> 3
print(20 % 6) --> 2
What is the output?
3
2

Q3

Explain this in one sentence:

What is the difference between / and //?

/ - Performs normal division and returns a float. eg: 8/2 = 4.0
// - Performs floor division, giving the whole-number part (rounded down for positive numbers).. eg: 8/2 = 4


🧠 Spaced Repetition (Topic 2)
Before we continue, one quick recap:

Q1.Which data type would you use for:

"Ritesh" → String
25 → Integer
6.5 → float
False → bool


🧠 Active Recall (1-Minute Revision)

Without looking at your notes, answer these:

Q1.What is the difference between a variable and a value?
A2.variable is container or labeled box.
Value - Value is data which is stored inside the variable 

Q2.Give one example of each:
str → "Abhishek"
int → 28
float → 3.14
bool → True


Q1.What does % return?
A1.Remainder

Q2.What does ** do?
A2. Exponentiation (return power)


Q3.What's the difference between / and //?
A3./ always return floating numbers
// floor division return integer result. (round down to the floor)

"""
