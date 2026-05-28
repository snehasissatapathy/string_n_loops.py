"""
=================================================
PALINDROME CHECKER
=================================================

Problem Statement:
Write a Python program to check whether a string
is palindrome or not.

-------------------------------------------------
Instructions:
1. Take string input.
2. Reverse the string.
3. Compare original and reversed string.
4. Print:
   - "Palindrome"
   - "Not Palindrome"

-------------------------------------------------
Input Example:
madam

Output Example:
Palindrome

-------------------------------------------------
Hints:
Use slicing or loop.

-------------------------------------------------
Expected Concepts:
- operators
- string slicing
- conditional statements

=================================================
"""

# Write your code below this line
# Program to check palindrome using string slicing

# Taking input from the user
value = input("Enter a number or string: ")

# Storing original value
original_value = value

# Reversing the value using string slicing
reverse_value = original_value[::-1]

# Displaying reversed value
print("Reversed value is:", reverse_value)

# Comparing original and reversed value
if original_value == reverse_value:
    print("The entered value is a Palindrome")
else:
    print("The entered value is Not a Palindrome")