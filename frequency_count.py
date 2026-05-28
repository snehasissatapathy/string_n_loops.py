"""
=================================================
CHARACTER FREQUENCY COUNTER
=================================================

Problem Statement:
Write a Python program to count how many times
a character appears in a string.

-------------------------------------------------
Instructions:
1. Take input from the user:
   - a string
   - a character
2. Use loop and conditional statements.
3. Print character count.

-------------------------------------------------
Input Example:
String: programming
Character: g

Output Example:
2
-------------------------------------------------
Expected Concepts:
- loops
- strings
- operators
- logical thinking

=================================================
"""

# Write your code below this line
# Program to count how many times a character appears in a string

# Taking string input
text = input("Enter a string: ")

# Taking character input
ch = input("Enter a character: ")

# Variable to store count
count = 0

# Using loop to check each character
for i in text:
    if i == ch:
        count = count + 1

# Displaying result
print("Character appears", count, "times")