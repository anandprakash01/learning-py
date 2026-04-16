# ===== LISTS (Mutable)
# Defined by square brackets [].

myList = ["Apple", 5, 3.9, True, 5]

# ===== 1 INSPECTION & SLICING
print(type(myList))  # <class 'list'>
print(len(myList))  # 5 (Total number of items)

print(myList[0])  # "Apple" (First element)
print(myList[-1])  # 5 (Last element via negative indexing)
# print(myList[10])  # IndexError: list index out of range

# List Slicing [start:stop]
# Remember: 'start' and 'stop' are indices, 'start' is inclusive and 'stop' is EXCLUSIVE.
print(myList[1:3])  # ['5', 3.9] (Slice from index 1 up to 2, NOT including, 3)
print(myList[2:])  # [3.9, True, 5] (Start from index 2 to the end)
print(myList[:2])  # ['Apple', 5] (from 0 up to index 1)
print(myList[:])  # ['Apple', 5, 3.9, True, 5] (Copy of the whole list)
print(myList[:-3])  # ['Apple', 5] (All but the last three elements)
print(myList[-3:])  # [3.9, True, 5] (Last three elements)
print(myList[3:1])  # [] (Empty list, because start index is greater than stop index)

# List Slicing with Steps [start:stop:step]
# he default step for a slice is +1
print(myList[::2])  # ["Apple", 3.9, 5] (Every second element)
print(myList[::-1])  # [5, True, 3.9, 5, "Apple"] (Creates a reversed copy)
print(myList[::-3])  # [5, 5] (Every third element in reverse)
print(myList[1::2])  # [5, True] (Every second element starting from index 1)
print(myList[2:0:-1])  # [3.9, 5] (Reverse slice from index 2 down to index 1)

# ===== 2. MODIFYING & INSERTING (IN-PLACE)
myList[0] = "Banana"  # Direct index mutation

myList[2:2] = ["Mango"]  # Inserts "Mango" at index 2 without replacing
myList[3:2] = [
    "Anand",
    "Prakash",
]  # Fallback quirk: Inserts both items at index 3 (bad practice, but it works)
print(myList)  # ['Banana', 5, 3.9, 'Anand', 'Prakash', True, 5]

# The Zero-Length Slice ([2:2] or [3:3])
# When you tell Python to slice a list, you are actually pointing to the spaces between the items, not the items themselves.

# If you request myList[3:3], Python does this calculation:

# Start at index: 3
# Stop at index: 3
# Total items selected: 0

# Because you selected 0 items, Python does not delete anything. However, because you used the assignment operator (= ["Anand", "Prakash"]), Python is forced to place those new items into the list. Since the slice has a length of 0 at index 3, the memory manager simply pushes the existing data to the right and inserts the new data exactly at the start index.

# The Backward Slice Anomaly ([3:1])
# Now, why does [3:1] and [3:2] do the exact same thing?

# Start Index: 3
# Stop Index: 1
# Step: +1

# The Interpreter's Math: "I am at index 3. I need to move forward (+1) until I hit index 1."

# The Conclusion: It is mathematically impossible to reach index 1 by moving forward from index 3.

# In lower-level languages like C or Java, this logical paradox would instantly crash the program with a Fatal Error. But Python is designed to be highly fault-tolerant.

# When Python realizes a slice's start is mathematically past its stop, it doesn't crash. It quietly evaluates the length of that slice as 0.

# Because the length is 0, the interpreter defaults to the exact same insertion behavior we saw above: It ignores the invalid stop index, and simply inserts the new data at the start index (3).


# ===== 3. ADDING ELEMENTS
# append,insert returns None
# If index is out of range, insert() will simply append to the end.
myList.append("Raj")  # Appends a single item to the very end.
myList.insert(3, "Isha")  # Pushes "Isha" into index 1, shifting everything right.
myList.insert(20, "Jyoti")  # index in greater than length so this will add at last
print(f"After added : ,{myList}")

myList = ["Anand"]
myList2 = ["Isha", "Anisha"]
myList.append(myList2)  # Adds myList2 as a single item (nested list).
print(myList)  # ['Anand', 'Isha', 'Anisha', ['Isha', 'Anisha']]


# Extending vs Appending
# append adds as a single item (nested list).
# extend Unpacks and adds individually..
myList = ["Anand"]
myList2 = ["Isha", "Anisha"]
myList.extend(myList2)  # Unpacks myList2 and adds individually.
print(myList)  # ['Anand', 'Isha', 'Anisha']

# ===== 4. REMOVING ELEMENTS
# If index is out of range, it raises an IndexError
# If value is not found, it raises a ValueError
# if empty list, it raises an IndexError
# If value is not found, it raises a ValueError

print(myList.pop())  # Remove last element and returns it
print(myList.pop(1))  # Remove element at index 1 and returns it
myList.remove("Anand")  # Remove first occurrence of value, returns None

# ===== 5. UTILITY METHODS
# if not found via index(), it raises a ValueError
# if not found via count(), it returns 0

myList = ["Anand", "Isha", "Anisha"]
print(len(myList))  # Length of list
print(myList.count("Isha"))  # Counts how many times "Isha" appears
print(myList.index("Isha"))  # Returns the index of the first occurrence of "Isha"

print(myList.index("Isha", 1))  # Start searching for "Isha" from index 2

num_list = [5, 2, 9, 1, 5, 6]
num_list.sort()  # Sorts the list permanently in ascending order.
num_list.sort(reverse=True)  # Sorts the list permanently in descending order.
print(num_list)
num_list.reverse()  # Reverses the physical memory order of the list.
print(num_list)

# ===== 6. ALGEBRAIC LIST OPERATIONS
# Concatenation (+) creates a brand new list in a new memory address.
list3 = [1, 2] + [3, 4]  # [1, 2, 3, 4]
# Repetition (*) duplicates the sequence.
list4 = ["A", "B"] * 2  # ["A", "B", "A", "B"]


# ===== 7. LIST UNPACKING (PEP 3132)
# You can assign list items directly to variables.
# The asterisk (*) gathers all remaining, unassigned items into a new sub-list.
pack = ["Sword", 100, 50.5, "Poison", "Map", "Key"]
weapon, damage, weight, *inventory = pack

print(weapon)  # "Sword"
print(inventory)  # ["Poison", "Map", "Key"]


# ===== 8. NESTED LISTS (Multidimensional Arrays)
# Lists can hold other lists. You access them by chaining brackets.
nestedList = [1, 2, ["A", "B"], [5, [6, 7]]]

print(nestedList[2])  # ["A", "B"]
print(nestedList[2][1])  # "B" (Goes to index 2, then index 1 inside that)
print(nestedList[3][1][0])  # 6 (Traverses three levels deep)

# ===== List comprehension
myList = [1, 3, 5, 6]
squaredList = []
# for item in myList:
#     squaredList.append(item * item)

squaredList = [i * i for i in myList]
print(squaredList)
