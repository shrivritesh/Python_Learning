# print("Question One counting UP ")
# count = 1
# while count <= 5:
#     print(count)
#     count += 1


# # Q2. 
# print("Question two counting down ")
# count = 5
# while count >= 1:
#     print(count)
#     count -= 1

# #Q3.
# print("Print Even Number using while loop ")

# num = 2
# while num <= 20:
#     print(num)
#     num += 2

# # Q4.
# print("Print odd number :")

# number = 1
# while number <= 20:
#     print(number)
#     number += 2

# # Q5.
# print("Sum Numbers ")
# count = 1
# total = 0

# while count <= 10:
#     total += count
#     count += 1
# print(total)

# # Q6.Multiplication table
# print("Enter a number for the table.")
# num_table = int(input("Enter any number :"))
# count = 1

# while count <= 10:
#     print(num_table * count)
#     count += 1

# # Q7. Even Number.

# limit = int(input("Enter limit for getting Even numbers.: "))
# num_ber = 2

# while num_ber <= limit:
#     print(num_ber)
#     num_ber += 2

# # Q8 - Count Even numbers

# limit = int(input("Enter limit for counting Even numbers : "))
# num_ber = 2
# count = 0

# while num_ber <= limit:
#     count += 1
#     num_ber += 2
# print(count)

# # Practice 9 — Sum of Even Numbers
# limit = int(input("Enter the limit for the Sum of Even Numbers : "))
# num_ber = 2
# total = 0

# while num_ber <= limit:
#     total += num_ber
#     num_ber += 2
# print(total)

# # Practice 10 — Sum of Odd Numbers

# limit = int(input("Enter the limit for the sum of odd numbers: "))
# num_ber = 1
# total = 0

# while num_ber <= limit:
#     total += num_ber
#     num_ber += 2
# print(total)

# # 🟢 Q11 — Count Odd Numbers
# print("Count odd numbers: ")
# limit = int(input("Enter odd number for count :"))
# number = 1
# count = 0

# while number <= limit:
#     count += 1
#     number += 2

# print(count)

# # 🟢 Q12 — Count Multiples of 3
# print("Count multiple of 3 :")
# limit = int(input("Enter limit :"))
# number = 3
# count = 0

# while number <= limit:
#     count += 1
#     number += 3
# print(count)

# # 🟢 Q13 — Sum of Multiples of 3
# print("Sum multiple of 3 :")
# limit = int(input("Enter limit :"))
# number = 3
# total = 0

# while number <= limit:
#     total += number
#     number += 3
    
# print(total)


# # 🟢 Q14 — Count Multiples of 5
# print("Countt multiple of 5 :")
# limit = int(input("Enter limit :"))
# number = 3
# count = 0

# while number <= limit:
#     count  += 1
#     number += 5
    
# print(count)

# # 🟢 Q15 — Sum of Multiples of 5
# print("Sum multiples of 5 :")
# limit = int(input("Enter limit :"))
# number = 5
# total = 0

# while number <= limit:
#     total += number
#     number += 5

# print(total)


# # 🟢 Q16 — Reverse Countdown using while
# count = 10

# while count >= 1:
#     print(count)
#     count -= 1
# # User_input
# start = int(input("Enter number to start :"))

# while start >= 1:
#     print(start)
#     start -= 1


# 🟢 Q17 — Reverse Even Numbers
print("*****************Reverse Even Numbers:***************** ")
start = int(input("Enter an Even number:"))

if start % 2 == 0:
    while start >= 2:
        print(start)
        start -=2
else:
    print("please enter an Even number:")



# 🟢 Q17 — Reverse Odd Numbers
print("*****************Reverse Odd Numbers:***************** ")
start = int(input("Enter an Odd number:"))

if start % 2 != 0:
    while start >= 1:
        print(start)
        start -=2
else:
    print("please enter an Odd number:")


# 🟢 Q19 — Sum of Even Numbers in Reverse
print("*******************Sum of Even Numbers in Reverse*******************")

start = int(input("Enter an Even number: "))
total = 0
if start % 2 == 0:
    while start >= 2:
        print(start)
        total += start
        start -= 2
    print(total)
else:
    print("Please Enter an Even Number:->")


# 🟢 Q20 — Sum of Odd Numbers in Reverse
print("*******************Sum of Odd Numbers in Reverse*******************")

start = int(input("Enter an Odd number: "))
total = 0
if start % 2 != 0:
    while start >= 1:
        print(start)
        total += start
        start -= 2
    print(total)
else:
    print("Please Enter an Odd Number:->")


# 🟢 Q21 — Find Largest Number using while
print("*************************Find largest number using while:************************* ")
num = int(input("Enter number:"))
largest = num
count = 1
while count < 5:
    num = int(input("Enter a number:"))
    if num > largest:
        largest = num
    count += 1
print(largest)

# 🟢 Q22 — Find Smallest Number using while

print("*************************Find Smallest number using while: *************************")
num = int(input("Enter number:"))
smallest = num
count = 1
while count < 5:
    num = int(input("Enter a number:"))
    if num < smallest:
        smallest = num
    count += 1
        
print(smallest)


# 🟢 Q23 — Largest & Smallest Together
print("****************Largest and smallest together****************")
num = int(input("Enter number :"))
largest = num
smallest = num
count = 1

while count < 5:
    num = int(input("Enter number:"))
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

    count += 1

print("Largest:",largest)
print("Smallest:",smallest)

# 🟢 Q24 — Count Positive, Negative & Zero
print("**************Count positive , negative and Zero: *****************")

positive = 0
negative = 0
zero = 0
count = 0

while count < 7:
    num = int(input("Enter numbers: "))
    if num == 0:
        zero += 1
    elif num > 0:
        positive += 1
    elif num < 0:
        negative += 1

    count += 1
print("Positive->",positive)
print("Negative->",negative)
print("Zero ->",zero)



# 🟢 Q25 — Count Even, Odd & Zero
print("*****************Count Even ,odd and Zero***************:")
is_even = 0
is_odd = 0
zero = 0
count = 0

while count < 7:
    num = int(input("Enter a numbers :"))
    if num == 0:
        zero += 1
    elif num % 2 == 0:
        is_even += 1
    else:
        is_odd += 1

    count += 1

print("Is Even Number : ",is_even)
print("Is Odd Number",is_odd)
print("Zero :",zero)

# 🟢 Q26 — Count Positive/Negative + Even/Odd
print("Count Positive / Negative + Even/Odd :")

positive_even = 0
positive_odd = 0
negative_even = 0
negative_odd = 0
zero = 0
count = 0

while count < 7:
    num = int(input("Enter numbers :"))

    if num == 0:
        zero +=1
    elif num > 0:
        if num % 2 == 0:
            positive_even += 1
        else:
            positive_odd += 1
    elif num < 0:
        if num % 2 == 0:
            negative_even += 1
        else:
            negative_odd += 1
    count += 1
    

print("Positive Even Number:",positive_even) 
print("Positive Odd Number :",positive_odd) 
print("Negative Even Number :",negative_even) 
print("Negative odd Number :",negative_odd )
print("Zero: ",zero )

# 🟢 Q27 — Sum of Positive Numbers
print("***********************Sum of Positive numbers :***********************")
numbers = int(input("How many numbers do you want to enter: "))
count = 0
total = 0
while count < numbers:
    num = int(input("Enter numbers :"))
    while num <= 0:
        print("Please! enter a valid number:. ")
        num = int(input("Enter positive number:. "))

    count += 1
    total += num


print("Sum of positive numbers :->",total)


# 🟢 Q28 — Sum of Negative Numbers
print("***********************Sum of Negative numbers :***********************")
numbers = int(input("How many numbers do you want to enter: ."))
count = 0
total = 0
while count < numbers:
    num = int(input("Enter numbers :"))
    while num >= 0:
        print("Please! enter a valid number: ")
        num = int(input("Enter Negative number: "))

    count += 1
    total += num


print("Sum of Negative numbers :->",total)
