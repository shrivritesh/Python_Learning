# Student Performance Analyzer
"""
Your program should:

Create a function calculate_average(marks) that returns the average.
Loop through the dictionary.
Calculate each student's average.
Determine:
>= 80 → "Excellent"
>= 60 → "Good"
< 60 → "Needs Improvement"
Store the results in a new dictionary.
Create a set containing the unique performance categories.
Find the student with the highest average.
Print a clean report.
"""
print("=======================Student Performance Analyzer=======================")
students = {
    "Ritesh": [85, 92, 78],
    "Amit": [72, 68, 75],
    "Rahul": [91, 88, 95],
    "Priya": [65, 70, 69],
    "Neha": [88, 90, 86]
}
result = {}
categories = set()

highest_average = 0
top_student = ""


# Calculating average.
def calculate_average(marks):
    total = 0
    for number in marks:
        total += number
    return  total / len(marks)


for name, marks in students.items():
    average = calculate_average(marks)
    if average >= 80:
        performance = "Excellent"
    elif average >= 60:
        performance = "Good"
    else:
        performance = "Need Improvement!"

    result[name]={
        "average": average,
        "performance":performance
    }
    categories.add(performance)


for name , data in result.items():
    if data["average"] > highest_average:
        highest_average = data["average"]
        top_student = name
    print(name, data["average"], data["performance"])


# print(name, data["average"], data["performance"])
print("=====================Summary=====================")
print("Top Student:", top_student)
print("Highest Average:", highest_average)
print("Unique Categories:", categories)


    