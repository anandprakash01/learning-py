import sys

# ===== TUPLES (Immutable) =====

# ===== 1. CREATION & PACKING
# Defined by parentheses ().
# ordered, immutable sequences of elements.
# They preserve the order of items, allow duplicates, and cannot be changed once created.
# To make a tuple with only ONE item, you MUST include a trailing comma, otherwise Python thinks it's just an integer.

myTuple = ("Anand", 5, 3.9, True, 5)  # A tuple with multiple items.
emptyTuple = ()  # An empty tuple.
emptyTuple_via_constructor = tuple()  # Another way to create an empty tuple.

# To make a tuple with only ONE item, you MUST include a trailing comma, otherwise Python thinks it's just an integer.
t_fake = 10  # <class 'int'>
t_real = (10,)  # <class 'tuple'>

print(type(t_fake))  # <class 'int'>
print(type(t_real))  # <class 'tuple'>
print("Original Tuple:", myTuple)
print("Empty Tuple:", emptyTuple)
print("length of myTuple:", len(myTuple))

# Implicit Tuple Packing (Parentheses are technically optional)
# If you separate values with commas, Python automatically packs them into a tuple.
t_packed = "a", "b", 5  # This is a tuple with three items, even without parentheses.
print("Packed Tuple:", t_packed)

# ===== 2. INSPECTION & SLICING
# Exactly the same mechanics as Lists and Strings.
myTuple = ("Anand", 5, 3.9, True, 5)
print(myTuple[0])  # "Anand" (First element)
print(myTuple[-1])  # 5 (Last element via negative indexing)
print(myTuple[1:3])  # (5, 3.9) (Slice from index 1 up to 2, NOT including, 3)
print(myTuple[1:])  # (5, 3.9, True, 5) (Start from index 1 to the end)
print(myTuple[:3])  # ("Anand", 5, 3.9) (from 0 up to index 2)
print(myTuple[:])  # ("Anand", 5, 3.9, True, 5) (Copy of the whole tuple)
print(myTuple[-3:])  # (3.9, True, 5) (Last three elements)
print(myTuple[:-3])  # ("Anand", 5) (All but the last three elements)
print(myTuple[3:1])  # () (Empty tuple, because start index is greater than stop index)
print(myTuple[::2])  # ("Anand", 3.9, 5) (Every second element)
print(myTuple[::-1])  # (5, True, 3.9, 5, "Anand") (Creates a reversed copy)
print(myTuple[::-3])  # (5, 5) (Every third element in reverse)
print(myTuple[1::2])  # (5, True) (Every second element starting from index 1)
print(myTuple[2:0:-1])  # (3.9, 5) (Reverse slice from index 2 down to index 1)
# print(myTuple[5])  # IndexError: tuple index out of range


# ===== 3. IMMUTABILITY (The Core Constraint)
# Tuples are immutable, meaning their elements cannot be changed after creation.
# myTuple[0] = "New Value"  # This would raise a TypeError: 'tuple' object does not support item assignment
# You cannot append, insert, remove, or pop. The data is locked.

# ===== 4. TUPLE METHODS & BUILT-INS
# Because they are locked, tuples only have TWO built-in methods.
print(myTuple.count(5))  # Count occurrences of value
print(myTuple.index(3.9))  # Find index of first occurrence of value

# Standard sequence built-ins work normally:
print(len(myTuple))  # Length of tuple
print(sum(myTuple[1:3]))  # Sum of numeric elements (5 + 3.9)

# ===== 5. ALGEBRAIC OPERATIONS
# Like strings, math creates a BRAND NEW tuple in memory.
t_concat = myTuple + ("Banana", "Grapes")  # Concatenation
t_repeat = ("A", "B") * 2  # ("A", "B", "A", "B")


# ===== 6. ADVANCED TUPLE UNPACKING
# Extracting values dynamically into variables.
nums = (10, 20, 30, 40, 50)

# The asterisk (*) absorbs all remaining items into a LIST.
*start, last = nums
print(start)  # [10, 20, 30, 40]
print(last)  # 50

first, *middle, last = nums
print(first)  # 10
print(middle)  # [20, 30, 40]
print(last)  # 50

# The Edge Case: If the asterisk captures nothing, it creates an empty list.
a, *rest = (1,)
print(rest)  # []

# Enterprise Convention: The Throwaway Variable (_)
# We use an underscore for data we are forced to unpack but don't care about.
x, y, *_ = (1, 2, 3, 4, 5)
print(x, y)  # 1 2 (The 3, 4, and 5 are tossed into the void with _)

# ===== 7. MEMBERSHIP & MULTIPLE ASSIGNMENT
print("Apple" in myTuple)  # True
print("Banana" not in myTuple)  # True

# Python uses tuple packing/unpacking to assign multiple variables instantly.
x, y, z = 1, 2, 3

# ===== 8. NESTED TUPLES & TYPE CONVERSION
nestedTuple = (1, 2, (3, 4), (5, (6, 7)))
print(nestedTuple[3][1][0])  # 6 (Accessing deeper nested element)

# Casting between mutable and immutable structures
my_list = ["Apple", "Banana", 4, True]
tuple_from_list = tuple(my_list)  # Convert list to tuple
list_from_tuple = list(myTuple)  # Convert tuple to list

# ===== 9. MEMORY ALLOCATION (The Architect's View)
# Let's prove that Lists are heavier than Tuples.
list_nums = [1, 2, 3]
tuple_nums = (1, 2, 3)

# sys.getsizeof() returns the exact bytes consumed in RAM.
print(sys.getsizeof(list_nums))  # Example: 88 bytes (Extra buffer memory included)
print(sys.getsizeof(tuple_nums))  # Example: 64 bytes (Locked, exact memory)
