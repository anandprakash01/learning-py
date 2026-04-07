
# 1. Defining Variables

# Industry Standard (PEP 8) Naming Rules:
  # Variables & Functions: snake_case (all lowercase, words separated by underscores).

  # Constants: UPPER_SNAKE_CASE (Python doesn't have strict constants, but we use uppercase to tell other developers "do not change this").

  # Allowed characters: Letters, numbers, and underscores.

  # Absolute Rule: A variable name cannot start with a number.


# We do not declare the type (e.g., int, string). Python infers it at runtime.
user_age = 30           # Valid snake_case
USER_AGE_LIMIT = 100    # UPPER_SNAKE_CASE indicates this should be treated as a constant
_private_var = "Secret" # A single leading underscore suggests internal use only (convention)

# 2. MEMORY POINTERS AND THE id() FUNCTION
# id() returns the exact memory address (in base-10) where the object lives.
player_score = 100
print("Memory address: ", id(player_score)) # E.g., 140732824946632 (Will vary on your machine)

# Multiple variables can point to the EXACT SAME object in memory.
# Python optimizes memory by reusing small integers (between -5 and 256). 
# this behavior is known as "Integer Caching" or "Integer Interning".
  # Small Integer Caching: Happens at runtime. It’s always active for -5 to 256.

  # Constant Folding or Peephole Optimization: Happens at compile-time. Python sees two identical "constants" in your script and merges them into one to be efficient.

enemy_score = 100
print("Are they the same object?", id(player_score) == id(enemy_score)) # True! They are the same object in memory.
print(id(player_score) is id(enemy_score)) # True! 'is' checks if both variables point to the same object in memory.

# 3. REASSIGNMENT AND THE "NAME TAG" CONCEPT
# We are moving the label, not changing the integer 100. (Integers are immutable).
player_score = 200 
print("Memory address: ", id(player_score)) # This is now a completely DIFFERENT memory address.

# 4. MULTIPLE ASSIGNMENT
# You can assign multiple variables on a single line (useful for unpacking later).
x, y, z = 1, 2, 3
same_x = same_y = same_z = 0 # All point to the integer 0









userName = "anandPrakash"   # String
age = 29                    # Integer
bank_Balance = 150.75       # Floating Point Number
is_active = True            # Boolean
married = None              # None

USER_AGE_LIMIT = 100        # UPPER_SNAKE_CASE indicates this should be treated as a constant

# 2. Printing (Using 'f-strings')
  # F-strings (formatted strings) are the modern, professional way to inject variables into text.
  # Just put an 'f' before the quotes and wrap variables in curly braces {}.
print(f"bank_Balance: {bank_Balance:.3f}") # This will print bank_Balance with 3 decimal places."
print(f"User {userName} will be {age + 1} next year.")

# print("I am " + age + " years old.") 
# the above line will throw an error because we cannot concatenate string and integer directly.
print("I am " + str(age) + " years old.")
# This is the correct way to concatenate string and integer by converting integer to string using str() function.

# 3. Basic Operators

  # Arithmetic Operators
a = 10
b = 5
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)

# Comparison Operators
print("Equal to:", a == b)
print("Not equal to:", a != b)
print("Greater than:", a > b)
print("Less than:", a < b)
print("Greater than or equal to:", a >= b)
print("Less than or equal to:", a <= b)

# Logical Operators
print("AND:", is_active and married)
print("OR:", is_active or married)
print("NOT:", not is_active)

