# ===== 1. Defining Variables

# Industry Standard (PEP 8) Naming Rules:
# Variables & Functions: snake_case (all lowercase, words separated by underscores).

# Constants: UPPER_SNAKE_CASE (Python doesn't have strict constants, but we use uppercase to tell other developers "do not change this").

# Allowed characters: Letters, numbers, and underscores.

# Absolute Rule: A variable name cannot start with a number.


# We do not declare the type (e.g., int, string). Python infers it at runtime.
user_age = 30  # Valid snake_case
USER_AGE_LIMIT = 100  # UPPER_SNAKE_CASE indicates this should be treated as a constant
_private_var = (
    "Secret"  # A single leading underscore suggests internal use only (convention)
)

# ===== 2. MEMORY POINTERS AND THE id() FUNCTION
# id() returns the exact memory address (in base-10) where the object lives.
player_score = 100
print(
    "Memory address: ", id(player_score)
)  # E.g., 140732824946632 (Will vary on your machine)

# Multiple variables can point to the EXACT SAME object in memory.
# Python optimizes memory by reusing small integers (between -5 and 256).
# this behavior is known as "Integer Caching" or "Integer Interning".
# Small Integer Caching: Happens at runtime. It’s always active for -5 to 256.

# Constant Folding or Peephole Optimization: Happens at compile-time. Python sees two identical "constants" in your script and merges them into one to be efficient.

# id(player_score) generates a large integer (the memory address).
# id(enemy_score) generates the exact same large integer (because they both point to the cached integer 100).
player_score = 100
enemy_score = 100
print(
    "Are they the same object?", id(player_score) == id(enemy_score)
)  # True! Checks if the values are the same.
print(
    id(player_score) is id(enemy_score)
)  # False! 'is' checks if they are the exact same object in memory.
# Calculates id(player_score) and creates a brand new integer object in memory to hold the giant number 140732800366480.
# Calculates id(enemy_score) and creates another brand new integer object in memory to hold the giant number 140732800366480.

print(
    player_score is enemy_score
)  # true'is' checks if they are the exact same object in memory.

# ===== 3. REASSIGNMENT AND THE "NAME TAG" CONCEPT
# We are moving the label, not changing the integer 100. (Integers are immutable).
player_score = 200
print(
    "Memory address: ", id(player_score)
)  # This is now a completely DIFFERENT memory address.

# ===== 4. MULTIPLE ASSIGNMENT
# You can assign multiple variables on a single line (useful for unpacking later).
x, y, z = 1, 2, 3
same_x = same_y = same_z = 0  # All point to the integer 0


userName = "anandPrakash"  # String
age = 29  # Integer
bank_Balance = 150.75  # Floating Point Number
is_active = True  # Boolean
married = None  # None

USER_AGE_LIMIT = 100  # UPPER_SNAKE_CASE indicates this should be treated as a constant

# ===== 5. Printing (Using 'f-strings')
# F-strings (formatted strings) are the modern, professional way to inject variables into text.
# Just put an 'f' before the quotes and wrap variables in curly braces {}.
print(
    f"bank_Balance: {bank_Balance:.4f}"
)  # This will print bank_Balance with 4 decimal places."

# The :.3f tells Python to format the number as a float with exactly 3 decimal places.
# The round() function returns a floating-point number (a float). In Python, floats do not store trailing zeros because, mathematically, 10.500 is exactly the same as 10.5.
print(
    f"Bank Balance: {round(bank_Balance,3)}"
)  # this will also print upto 4 decimal places
print(f"User {userName} will be {age + 1} next year.")

# print("I am " + age + " years old.")
# the above line will throw an error because we cannot concatenate string and integer directly.
print("I am " + str(age) + " years old.")
# This is the correct way to concatenate string and integer by converting integer to string using str() function.

# Input Function
a = input("Enter number 1: ")
b = input("Enter number 2: ")

print(a + b)
print(int(a) + int(b))
