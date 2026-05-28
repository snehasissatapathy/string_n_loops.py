"""
=================================================
REVERSE A STRING
=================================================

Problem Statement:
Write a Python program to reverse a string.

-------------------------------------------------
Instructions:
1. Take string input from the user.
2. Reverse the string using:
   - slicing AND
   - loop
3. Print reversed string.

-------------------------------------------------
Input Example:
Python

Output Example:
nohtyP

-------------------------------------------------
Expected Concepts:
- string slicing
- loops
- indexing

=================================================
"""

# Write your code below this line
# Taking input from user
text = input("Enter a string: ")

# Reversing the string
reverse_text = text[::-1]

# Displaying the reversed string
print("Reversed string is:", reverse_text)