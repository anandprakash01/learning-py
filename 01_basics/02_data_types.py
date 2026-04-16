# Primitive data types
# int: In Python 3, integers have arbitrary precision. They are not limited to 32 or 64 bits; they can be as large as your computer's RAM allows.(Integers are immutable)

# float: Python floats are implemented using C's double in the background (IEEE 754 standard). They offer 53 bits of precision. Because computers operate in base-2 (binary), they cannot perfectly represent certain base-10 fractions, leading to microscopic rounding anomalies.

# complex: Python natively supports complex numbers, utilizing j for the imaginary unit (standard in electrical engineering) rather than i (standard in mathematics).

# bool: Booleans (True / False) are actually a subclass of integers. True is structurally evaluated as 1, and False is evaluated as 0.

# None: None is Python's "null". It is a Singleton, meaning only one instance of None ever exists in memory at any given time.

# 1. INTEGERS (int)
small_integer = 3
massive_integer = 10**100  # 1 followed by 100 zeros. Python handles this natively.
print(type(massive_integer))  # <class 'int'>

# 2. FLOATING POINT (float) AND THE IEEE 754 PITFALL
mass_of_electron = 9.109e-31  # Equivalent to 9.109 * 10^-31
fractional_value = 3.14159
print(type(fractional_value))  # <class 'float'>

# EDGE CASE: Binary representation error
precision_error = 0.1 + 0.2
print(precision_error)  # Outputs: 0.30000000000000004 (Not exactly 0.3!)
# Never use == for floats. Later, we will use the math.isclose() function to compare floats with a microscopic tolerance margin.

# 3. COMPLEX NUMBERS (complex)
# Written as (real + imag j)
imaginary_num = 3 + 4j
print(type(imaginary_num))  # <class 'complex'>
print(imaginary_num.real)  # Outputs: 3.0 (stored as float)
print(imaginary_num.imag)  # Outputs: 4.0 (stored as float)

# 4. BOOLEANS (bool)
is_active = True
print(type(is_active))  # <class 'bool'>
# EDGE CASE: Because bools are integers, math works on them.
# Do NOT do this in production, but understand that it is possible:
bool_sum = is_active + 5
print(bool_sum)  # Outputs: 6 (1 + 5)

# 5. THE NoneType SINGLETON
# Used to define a variable without giving it a value yet.
user_profile = None
database_connection = None
# Proof that they are the exact same object in memory:
print(id(user_profile) == id(database_connection))  # Outputs: True

# 6. STRINGS (str)
# Strings are immutable sequences of Unicode characters. They can be defined with single, double, or triple quotes.
greeting = "Hello, World!"
print(type(greeting))  # <class 'str'>
multi_line = """This is a multi-line string.
It can span multiple lines without needing escape characters."""


userName = "anandPrakash"  # String
age = 29  # Integer
bank_Balance = 150.75  # Floating Point Number
is_active = True  # Boolean
married = None  # None

USER_AGE_LIMIT = 100  # UPPER_SNAKE_CASE indicates this should be treated as a constant
