"""
=================================================
PASSWORD STRENGTH CHECKER
=================================================

Problem Statement:
Write a Python program to check password strength.

-------------------------------------------------
Conditions:
A password is strong if:
1. Length is at least 8
2. Contains at least one digit
3. Contains at least one uppercase letter

-------------------------------------------------
Instructions:
1. Take password input from user.
2. Use loops and conditional statements.
3. Print:
   - "Strong Password"
   - "Weak Password"

-------------------------------------------------
Input Example:
Python123

Output Example:
Strong Password

-------------------------------------------------
Hints:
Use:
isdigit()
isupper()

-------------------------------------------------
Expected Concepts:
- loops
- string functions
- operators
- conditional statements

=================================================
"""

# Write your code below this line
password = input("Enter password: ")

upper = 0
lower = 0
digit = 0

for i in password:
    if i.isupper():
        upper = upper + 1
    elif i.islower():
        lower = lower + 1
    elif i.isdigit():
        digit = digit + 1

if len(password) >= 8 and upper > 0 and lower > 0 and digit > 0:
    print("Strong Password")
else:
    print("Weak Password")