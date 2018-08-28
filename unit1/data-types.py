"""
Project:     Data Types Notes
Author:      Mr. Buckley
Last update: 8/25/2018
Description: Goes over comments, int, float, str, and type casting  
"""

# *** COMMENTS ***
# This is a comment (with a "#")
# Comments are only for the user's eyes, the program doesn't read them.
# Describe what sections of code do with a comment.

"""
This is a
multiline comment
"""

# *** DATA TYPE: INTEGER ***
# TODO: An integer number (no decimal)
integer = 5
print(integer)
print(type(integer))

# *** DATA TYPE: FLOAT ***
# TODO: A decimal number
decimal = 5.5
print(decimal)
print(type(decimal))


# *** DATA TYPE: STRING ***
# TODO: A string of characters enclosed in quotes
word = "hi people"
print(word)
print(type(word))


# *** TYPE CASTING ***
# This converts one type to another

# TODO: Cast float to int
decimal = 5.5
dec_to_int = int(decimal)
print(type(dec_to_int))
print(dec_to_int)

# TODO: Cast int to string

# TODO: Cast number string to int
number = "6"
print(int(number) + 2)

# TODO: Input demo (str to float)
print("name?")
number = float(input())


