"""
for loop:
for loop is used to repeat a block of code for each item is a sequence or iterable.
like list,str, range..

Syntax:
for variable in range(start,stop):
    print(var_name)


"""
# 🟢 Practice 1 — Print 1 to 5
print("Print 1 to 5: ")
for i in range(1,6):
    print("range =",i)


# Print 1 to 10 
print("Print 1 to 10")
for i in range(1,10+1):
    print(i)

# 🟢 Practice 2 — Counting Down
print("print 5 to 1 :")
for n in range(5,0,-1):
    print(n)

# Couting down 10 - 1
print("Counting Down From 10 to 1 :")
for i in range(10, 0, -1): 
    print(i)

# 🟢 Practice 3 — Even Numbers
print("Print Even numbers: ")
for n in range(2,21,2):
    print("Even numbers :",n)

# Even number between 20:
print("EVen numbers b/w 1 to 20 :")
for i in range(2,21, 2): 
    print(i)


# 🟢 Practice 3 — Odd Numbers
print("Odd Numbers: ")
for n in range(1,21,2):
    print("Odd numbers:- ", n)

# print odd numbers between 1 to 20
print("Odd numbers between 1 t 20")
for n in range(1,21,2):
    print(n)

# 🟢 Practice 5 — Sum 1 to 10
print("Sum of num from  1 to 10 :")
total = 0
for i in range(1,11):
    total += i
print(total)

# 🟢 Practice 6 — Multiplication Table
print("Multiplication Table: ")
num = int(input("Enter any num : "))
for i in range(1,11):
    print(num * i )

# 🟢 Practice 7 — User Limit + Even Numbers

print("Even number using limit>> ")
limit = int(input("Enter limit :"))
for i in range(2,limit + 1,2):
    print(i)

# 🟢 Practice 8 — User Limit + Odd Numbers

print("Odd numbers using limit: ")
limit = int(input("Enter limit :"))
for i in range(1,limit + 1,2):
    print(i)

# 🟢 Q5 — Step Practice
print("multiples of 5 from 5 to 30:")
for i in range(5,35,5):
    print(i)


# 🟢 Q6 — Reverse Step
print("Reverse step :")
for i in range(20,8,-2):
    print(i)

"""
1 → 10       range(1, 11)
10 → 1       range(10, 0, -1)
Even 2–20    range(2, 21, 2)
Odd 1–19     range(1, 21, 2)


# Sum
total += i

# Count
count += 1

# Product / factorial
factorial *= i
"""

"""
🟢 Q7 — Multiples of 3
Print multiples of 3 from 3 to 30
"""
# With multiplication
num = 3
for i in range(1,11): 
    print(num * i)

# with step
for i in range(3,31,3):
    print(i)

# 🟢 Q8 — Sum 1 to 10
print("sum of total number b/w  1 to 10: ")
total = 0
for i in range(1, 11):
    total += i

print(total)


# 🟢 Q9 — Sum of Even Numbers

# Now calculate the sum of all even numbers from 2 to 20.
total = 0
print("Sum of all even numbers from 2 to 20:")
for i in range(2,21,2):
    total += i

print(total)

# 🟢 Q10 — Sum of Odd Numbers

# sum of all odd numbers from 1 to 19:

print("Sum of all Odd numbers from 1 to 19 >>")
total = 0
for i in range(1,21,2):
    total +=i
    # print(i)
print(total)

# Odd and Even using limit given by user

print("*****************Odd numbers using user_input:*****************")
limit = int(input("Enter limit :"))

for n in range(1,limit+1,2):
    print("odd :->",n)


# Print even numbers
print("*******************Even numbers using user_input:*******************")
limit = int(input("Enter limit :"))

for n in range(2,limit+1,2):
    print("Even :->",n)




# 🟢 Q13 — Count Even Numbers
print("****************Count even numbers:->****************")
limit = int(input("Enter limit: "))

count = 0

for i in range(2, limit + 1, 2):
    print("Even numbers :",i)
    count += 1
print(f"Number of even numbers up to {limit}: {count}")

# 🟢 Q14 — Count Odd Numbers
print("******************Count odd numbers :******************")
limit = int(input("Enter limit: "))

count = 0

for i in range(1, limit + 1, 2):
    print("Odd numbers :",i)
    count += 1

print(f"Number of odd numbers up to {limit}: {count}")

# 🟢 Q15 — Count Multiples of 3
print("****************Count multiples of 3 :******************")
limit = int(input("Enter limit to count multiples of 3 :->"))
count = 0

for n in range(3,limit+1,3):
    print(n)
    count += 1

print(f"Number of multiples of 3: {count}")


# 🟢 Q16 — Sum of Multiples of 3

print("***********Sum of multiples of 3 :**************")
limit = int(input("Enter limit: "))

total = 0
for i in range(3,limit+1,3):
    total+=i

print(total)



# 🟢 Q17 — Sum of Multiples of 5

print("****************Sum of multiples of 5 :****************")
limit = int(input("Enter limit: "))

total = 0
for i in range(5,limit+1,5):
    total+=i

print(total)

# 🟢 Q18 — Count Multiples of 5

print("****************Count multiple of 5:****************")
limit=int(input("Enter limit:"))
count = 0
for i in range(5,limit+1,5):
    count += 1
print(count)


# 🟢 Q19 — Sum of Multiples of 2
print("**********sum of multiple **********:")
limit=int(input("Enter limit:"))
total = 0

for i in range(2,limit+1,2):
    total += i

print(total)

# 🟢 Q20 — Sum of Odd Numbers Using User Limit
print("************Sum of odd numbers:************ ")
limit=int(input("Enter limit :"))
total = 0
for i in range(1,limit+1,2):
    total += i
print(total)


# 🎯 Q21 — Multiplication Table with User Limit
print("**********Multiplication table**************")
num = int(input("Enter number: "))
limit = int(input("Enter limit: "))

for i in range(1, limit + 1):
    print(i*num)


# # 🟢 Q22 — Sum of Multiplication Table
print("Sum of Multiplication Table")
num = int(input("Enter num :"))
limit= int(input("Enter limit :"))
total = 0

for i in range(1, limit + 1):
    total += i * num

print(total)


# 🟢 Q23 — Factorial
"""
Task
Ask the user for a number and calculate its factorial.

"""
print("********FACTORIAL_NUMBER************")
num = int(input("Enter number: "))

factorial = 1

for i in range(1, num + 1):
    # factorial*=i
    factorial = factorial * i

print(factorial)


# 🟢 Q24 — Reverse Numbers Using User Input
print("**************Reverse number**************")
start = int(input("Enter starting number: "))

for i in range(start, 0, -1):
    print(i)


# 🟢 Q25 — Count Down by 2
print("**************Count down by 2**************")
start = int(input("Enter starting number: "))

for i in range(start, 1, -2):
    print(i)

# 🟢 Q27 — Reverse Even Numbers
print("******************Reverse Even Numbers******************")
start = int(input("Enter starting number: "))

if start % 2 == 0:
    for i in range(start,0,-2):
        print(i)
else:
    print("Please enter an Even number:")



# 🟢 Q28 — Reverse Odd Numbers

print("******************Reverse Odd Numbers******************")
start = int(input("Enter starting number: "))

# if start % 2 == 1:
if start % 2 != 0:
    for i in range(start,0,-2):
        print(i)
else:
    print("Please enter an odd number:")


# 🟢 Q30 — Sum of Even Numbers in Reverse
print("*************Sum of even number in Reverse Order*************")
start = int(input("Enter an Even Number:"))
total = 0
if start % 2==0:
    for i in range(start,0,-2):
        total += i
    print(total)
else:
    print("Please! Enter an Even number.")
# print(total)


# 🟢 Q30 — Sum of Odd Numbers in Reverse
print("****************Sum of odd numbers in reverse order-****************")
start = int(input("Enter an Odd number to start:"))
total = 0
if start % 2 != 0:
    for i in range(start,0,-2):
        total+=i
    print(total)
else:
    print("Enter an Odd number!.")


# 🟢 Q31 — Find the Largest Number
print("*****************Find The Largest Number*****************")

largest = int(input("Enter any largest num: "))
for i in range(4):
    num = int(input("Enter number:"))
    if num > largest:
        largest = num
print("Largest number is :->",largest)

# 🟢 Q32 — Find the Smallest Number
print("*****************Find The Smallest Number*****************")
smallest = int(input("Enter smallest number."))
for i in range(4):
    num = int(input("Enter numbers :"))
    if num <= smallest:
        smallest = num
print("Smallest number is:->",smallest)


# Q33 — Largest & Smallest Together program.
print("*****************Smallest and largest together :*****************")
first = int(input("Enter first number:"))
smallest = first
largest = first
for i in range(4):
    num = int(input("Enter numbers:"))

    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
print(f"Largest number is {largest} and Smallest is {smallest}  ")



# 🟢 Q34 — Count Positive & Negative Numbers

print("Count Positive & Negative Numbers")
positive = 0
negative = 0

for i in range(5):
    num = int(input("Enter number :"))
    if num > 0:
        positive += 1
    if num < 0:
        negative += 1

print(f"Postive numbers are {positive} and negative are {negative}")

# 🟢 Q35 — Count Positive, Negative AND Zero


print("Count Positive , Negative Numbers and Zero")
positive = 0
negative = 0
zero = 0

for i in range(5):
    num = int(input("Enter number :"))
    if num > 0:
        positive += 1
    if num < 0:
        negative += 1
    if num == 0:
        zero += 1
print("Positive number is :",positive)
print("Negative number is :",negative)
print("Zero number is :",zero)


# 🟢 Q36 — Count Even, Odd & Zero Together

print("***************Count Even, Odd & Zero Together***************")
even = 0
odd = 0
zero = 0

for i in range(7):
    num = int(input("Enter number: "))

    if num == 0:
        zero += 1
    elif num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even)
print("Odd:", odd)
print("Zero:", zero)



# 🟢 Q37 — Count Positive/Negative + Even/Odd
# Ask the user for 7 numbers and count:
positive_even = 0
positive_odd = 0
negative_even = 0
negative_odd = 0
zero = 0

for i in range(7):
    num = int(input("Enter numbers :"))
    if num == 0:
        zero += 1
    if num % 2 == 0:
        if num > 0:
            positive_even += 1
        elif num < 0:
            negative_even += 1
    elif num % 2 != 0:
        if num > 0:
            positive_odd += 1
        elif num < 0:
            negative_odd += 1

print("Zero",zero)
print("Positive_even Number :",positive_even)
print("Negative_even Number :",negative_even)
print("Positive_odd Number :",positive_odd)
print("Negative_odd Number :",negative_odd)


# 🟢 Q38 — Find the Sum of Positive Numbers
print("*************Find the Sum of positive Numbers :************************ ")
total = 0
for i in range(5):
    num = int(input("Enter number: "))
    if num > 0:
        total += num
print(total)

# Count positive → positive += 1
# Sum positive   → total += num


# 🟢 Q39 — Sum of Negative Numbers

print("*************Find the Sum of Negative Numbers :************************ ")
total = 0
for i in range(5):
    num = int(input("Enter number: "))
    if num < 0:
        total += num
print(total)

# 🟢 Q40 — Count Numbers Greater Than 10

count = 0

for i in range(7):
    num = int(input("Enter number: "))

    if num > 10:
        # COUNT pattern
        count += 1
print(count)