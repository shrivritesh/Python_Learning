"""
Project 6 — Driving Eligibility Checker

Ask the user's age.

18+ → Eligible to drive
Below 18 → Not eligible

"""
age_for_driving = int(input("Enter your age :"))

if age_for_driving >= 18:
    print("Eligible to drive")
else:
    print("Not eligible")