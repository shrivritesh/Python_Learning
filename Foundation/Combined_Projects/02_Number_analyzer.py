"""
# 🟢 Combined Project — Number Analyzer

Create a Python program that asks the user how many numbers they want
to enter and then analyzes those numbers.

The program should:

1. Count Positive numbers
2. Count Negative numbers
3. Count Zero
4. Count Even numbers
5. Count Odd numbers
6. Find the Sum of Positive numbers
7. Find the Sum of Negative numbers
8. Find the Largest number
9. Find the Smallest number

Requirements:
- Use a while loop to collect the numbers.
- Use a for loop to analyze the collected numbers.
- Use conditions to classify the numbers.
- Display a final result/report at the end.

WHILE → Collect 🔄
FOR   → Analyze 🔍
"""

print("=========== Number Analyzer Program ===========")
num = int(input("How many numbers do you want: "))

while num <= 0:
    print("Please! Enter a valid number: ")
    num = int(input("How many numbers do you want: "))

values = []
count = 0

while count < num:
    number = int(input("Enter Number:"))
    values.append(number)
    count += 1
# print("Values :",values)
# print("count :",count)

positive = 0
negative = 0
zero = 0
even = 0
odd = 0

positive_sum = 0
negative_sum = 0

largest = values[0]
smallest = values[0]
for number in values:
    
    if number > 0:
        positive += 1
    elif number < 0:
        negative += 1
    else:
        zero += 1

    # if Even /odd check

    if number != 0:
        if number % 2 == 0:
            even += 1
        else:
            odd+=1
    # Sum of Positive / Negative Numbers

    if number > 0:
        positive_sum += number
    elif number < 0:
        negative_sum += number

    # find Largest /smallest:

    if number > largest:
        largest = number
    if number < smallest:
        smallest = number

print("Positive Number: ",positive)
print("Negative Number :",negative)
print("Zero",zero)
print("Even Number :",even)
print("Odd Number :",odd)
print("Total positive number :",positive_sum)
print("Total negative number :",negative_sum)
print("Largest number :",largest)
print("Smallest number :",smallest)
