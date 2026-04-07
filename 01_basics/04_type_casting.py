
# ======= 1. IMPLICIT COERCION (The Safe Automatic Conversion)
base_score = 100    # <class 'int'>
multiplier = 1.5    # <class 'float'>
# Python safely promotes the integer to a float (100.0) before multiplying.
total = base_score * multiplier  # Result is a float
print(total)  # 150.0

# ======= 2. EXPLICIT CASTING TO STRING (str)
# Required when concatenating numbers with text.
player_lives = 3
# WRONG: print("Lives left: " + player_lives) -> TypeError
print("Lives left: " + str(player_lives))

# ======= 3. EXPLICIT CASTING TO INTEGER (int)
# Extracts the whole number. Can convert from floats (truncating the decimal) or numeric strings.
string_number = "42"
clean_int = int(string_number)
float_string = "3.14"
# WRONG: int(float_string) -> ValueError (can't directly convert a float string to integer)
# Must first convert to float, then to int.
int_from_float = int(float(float_string))

# ARCHITECTURAL NOTE: Casting a float to an int DOES NOT ROUND. It Truncates (chops off the decimal).
gravity = 9.81
truncated_gravity = int(gravity) 
print(truncated_gravity) # Outputs: 9 (Notice it did not round up to 10!)

# ======= 4. EXPLICIT CASTING TO FLOAT (float)
# Converts integers or numeric strings to floats.
score = 85
score_float = float(score)  # Converts to 85.0
score_str = "99.9"
score = float(score_str)  # Converts to 99.9

# ======= # 5. EXPLICIT CASTING TO BOOLEAN (bool) and TRUTHY/FALSY
# Every object in Python evaluates to True or False. 
# Zero, None, and completely empty sequences ("") evaluate to False. 
# EVERYTHING ELSE evaluates to True.
print(bool(0))        # False
print(bool(1))        # True
print(bool(""))       # False (Empty string)
print(bool(" "))      # True (Contains a space, not empty!)
print(bool("False"))  # True (It is a non-empty string, Python doesn't care what it spells)
print(bool(None))     # False


# a = input("Enter a No.") # this will take input as String
a = float(input("Enter a No."))
b = float(input("Enter a No."))
print(a+b)

print("Square of a No. is: ", 5**2)