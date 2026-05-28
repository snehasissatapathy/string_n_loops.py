"""
=================================================
CONSECUTIVE CHARACTER COUNTER
=================================================

Problem Statement:
Write a Python program to count the maximum number
of consecutive occurrences of the same character
in a string.

-------------------------------------------------
Instructions:
1. Take a string as input.
2. Use a for loop.
3. Find the longest consecutive repeating character.
4. Print:
   - character
   - count

-------------------------------------------------
Input Example:
aaabbccccdde

Output Example:
Character: c
Count: 4

-------------------------------------------------
Explanation:
a -> 3 times
b -> 2 times
c -> 4 times
d -> 2 times
e -> 1 time

Highest consecutive count:
c -> 4

-------------------------------------------------
Hints:
1. Compare current character with previous character.
2. Keep track of:
   - current count
   - maximum count
3. Update maximum when needed.

-------------------------------------------------
Expected Concepts:
- Don't use dictionary.
- for loops
- string indexing
- operators
- conditional statements
- logical thinking

=================================================
"""

# Write your code below this line
# Program to find the maximum consecutive occurrences


# Taking string input from user
text = input("Enter a string: ")

# Variable to store maximum count
max_count = 0

# Variable to store current consecutive count
current_count = 1

# Variable to store character with maximum repetition
max_character = ""

# Using for loop with string indexing
for i in range(0, len(text) - 1):

    # Comparing current character with next character
    if text[i] == text[i + 1]:

        # Increase current count
        current_count = current_count + 1

    else:

        # Check if current count is greater than max count
        if current_count > max_count:

            max_count = current_count
            max_character = text[i]

        # Reset current count
        current_count = 1

# Checking last sequence
if current_count > max_count:

    max_count = current_count
    max_character = text[len(text) - 1]

# Displaying output
print("Character with maximum consecutive occurrence is :", max_character)
print("Maximum consecutive count is :", max_count)