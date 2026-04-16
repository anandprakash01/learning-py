# operators

# 1. ARITHMETIC OPERATORS
print("======== 1. ARITHMETIC OPERATORS ========")
x, y = 10, 3
print(x + y)  # Addition: 13
print(x - y)  # Subtraction: 7
print(x * y)  # Multiplication: 30
print(x / y)  # True Division: 3.3333333333333335 (ALWAYS returns a float)
print(x % y)  # Modulo (Remainder): 1 (10 divided by 3 leaves a remainder of 1)
print(x**y)  # Exponentiation: 1000 (10 raised to the power of 3)

# ARCHITECTURAL EDGE CASE: Floor Division (//)
# Floor division does NOT just chop off the decimal. It mathematically rounds DOWN to the nearest whole integer.
print(10 // 3)  # Outputs: 3
print(-11 // 3)  # Outputs: -4 (Because -3.66 rounds DOWN to -4, not -3!)

# 2. ASSIGNMENT OPERATORS
# Modifies the variable in-place.
print("======== 2. ASSIGNMENT OPERATORS ========")
score = 50
score += 10  # Equivalent to: score = score + 10 (score is now 60)
score //= 2  # Equivalent to: score = score // 2 (score is now 30)
# (Also available: -=, *=, /=, %=, **=)


# 3. COMPARISON OPERATORS (Always Return Booleans)
print("======== 3. COMPARISON OPERATORS ========")
a, b = 5, 10
print(a == b)  # Equal to: False
print(a != b)  # Not equal to: True
print(a > b)  # Greater than: False
print(a < b)  # Less than: True
print(a >= 5)  # Greater than or equal to: True
print(a <= 10)  # Less than or equal to: True


# 4. LOGICAL OPERATORS (With Short-Circuit Evaluation)
# 'and' : True ONLY if BOTH sides are True.
# 'or'  : True if AT LEAST ONE side is True.
# 'not' : Inverts the Boolean.

# ARCHITECTURAL MECHANIC: Short-Circuiting
# To save processing power, Python stops reading an expression the millisecond it knows the final answer.
# In an 'or' statement, if the left side is True, the whole thing must be True.
# Python skips reading the right side entirely. It short-circuits.
# Or
# if first is True, first is returned
# if first is False, second is returned
# if both are True, first is returned
# if both are False, second is returned
# only see first value to decide
print("======== 4. LOGICAL OPERATORS (With Short-Circuit Evaluation) ========")
x = 1 or 0  # True or False -> True, so 1 is returned, 0 is never evaluated.
print(x)
x = 1 or "anand"  # True or True -> True, so 1 is returned, "anand" is never evaluated.
print(x)
x = 0 or "true"  # False or True -> True, so "true" is returned, 0 is never evaluated.
print(x)
x = 0 or None  # False or False -> False, so None is returned, 0 is never evaluated.
print(x)

# and
# if first is True, second is returned
# if first is False, first is returned
x = a and 0
print(x)
x = 0 and 1
print(x)

y = not (x)
print(y)

# 5. IDENTITY OPERATORS (is, is not)
# == checks VALUES. 'is' checks MEMORY ADDRESSES.
print("======== 5. IDENTITY OPERATORS (is, is not) ========")
list_x = [1, 2]
list_y = [1, 2]
print(list_x == list_y)  # True: The contents are identical.
print(
    list_x is list_y
)  # False: They are two separate objects living in different memory addresses.

# 6. MEMBERSHIP OPERATORS (in, not in)
# Checks if a sequence exists inside another sequence.
print("======== 6. MEMBERSHIP OPERATORS (in, not in) ========")
role = "administrator"
print("admin" in role)  # True
print("z" not in role)  # True

# 7. BITWISE OPERATORS (Operates on the binary bits)
# 5 is 0101 in binary. 3 is 0011 in binary.
print("======== 7. BITWISE OPERATORS (Operates on the binary bits) ========")
p, q = 5, 3
print(p & q)  # Bitwise AND: 1 (0001) - Keeps bits set in BOTH.
print(p | q)  # Bitwise OR: 7 (0111) - Keeps bits set in EITHER.
print(p ^ q)  # Bitwise XOR: 6 (0110) - Keeps bits set in ONE, but not both.
print(p << 1)  # Left Shift: 10 (1010) - Shifts bits left by 1 (multiplies by 2).
print(p >> 1)  # Right Shift: 2 (0010) - Shifts bits right by 1 (divides by 2).
