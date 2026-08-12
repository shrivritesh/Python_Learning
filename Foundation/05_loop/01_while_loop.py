print("Question One counting UP ")
count = 1
while count <= 5:
    print(count)
    count += 1


# Q2. 
print("Question two counting down ")
count = 5
while count >= 1:
    print(count)
    count -= 1

#Q3.
print("Print Even Number using while loop ")

num = 2
while num <= 20:
    print(num)
    num += 2

# Q4.
print("Print odd number :")

number = 1
while number <= 20:
    print(number)
    number += 2

# Q5.
print("Sum Numbers ")
count = 1
total = 0

while count <= 10:
    total += count
    count += 1
print(total)

# Q6.Multiplication table
print("Enter a number for the table.")
num_table = int(input("Enter any number :"))
count = 1

while count <= 10:
    print(num_table * count)
    count += 1

# Q7. Even Number.

limit = int(input("Enter limit for getting Even numbers.: "))
num_ber = 2

while num_ber <= limit:
    print(num_ber)
    num_ber += 2

# Q8 - Count Even numbers

limit = int(input("Enter limit for counting Even numbers : "))
num_ber = 2
count = 0

while num_ber <= limit:
    count += 1
    num_ber += 2
print(count)

# Practice 9 — Sum of Even Numbers
limit = int(input("Enter the limit for the Sum of Even Numbers : "))
num_ber = 2
total = 0

while num_ber <= limit:
    total += num_ber
    num_ber += 2
print(total)

# Practice 10 — Sum of Odd Numbers

limit = int(input("Enter the limit for the sum of odd numbers: "))
num_ber = 1
total = 0

while num_ber <= limit:
    total += num_ber
    num_ber += 2
print(total)