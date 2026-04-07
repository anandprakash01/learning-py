# A set is an unordered collection of unique elements with no indexing.
# Under the hood, a Set is basically a Dictionary that only has Keys (no Values).
# Because it uses a Hash Table, looking up whether an item exists in a Set takes exactly the same amount of time whether the Set has 10 items or 10 million items ( O(1) time complexity).

# Sets are used for two primary architectural reasons:
# 1.Instant Deduplication: Stripping duplicate values out of a list.
# 2.Venn Diagram Mathematics: Comparing massive datasets (Intersections, Unions, Differences).

# ===== 1. CREATION & ALLOCATION
# Sets use curly braces {}, just like dictionaries, but without key-value pairs.

d = {}  # <class 'dict'>
t = ()  # <class 'tuple'>

s = set()  # <class 'set'> (The ONLY way to make an empty set)

my_set = {"Apple", "Banana", "Cherry", "Apple"}

# The Hashing Collision (1 == 1.0 == True)
# Python evaluates 1, 1.0, and True as the exact same mathematical value.
# A set will only keep the VERY FIRST one it sees.

quirk_set = set()
quirk_set.add(1)
quirk_set.add(1.0)
quirk_set.add("1")
quirk_set.add(2)
quirk_set.add(2.0)

print(quirk_set)
print(len(quirk_set))  # number of unique elements

# Casting form other iterables
mySet2 = set([3, 4, 4, 5])  # From List: {3, 4, 5}
mySet3 = set(("apple", "banana", "apple"))  # From Tuple: {'apple', 'banana'}
mySet4 = set("hello")  # From String: {'h', 'e', 'l', 'o'}


# ===== 2. MODIFYING & REMOVING
mySet = {1, 2, 3}

mySet.add(6)  # Adds 6. Returns None.

# Remove vs Discard
mySet.remove(2)  # Deletes 2. Raises KeyError if 2 doesn't exist.
mySet.discard(10)  # Attempts to delete 10. Does NOT raise an error if missing.

# Pop, Clear, and Delete
popped = mySet.pop()  # Removes and returns a completely RANDOM element.
mySet.clear()  # Wipes the set completely clean: set()
del mySet  # Deletes the variable entirely from memory (raises NameError if called again)

# ===== 3. ITERATION & INSPECTION
active_set = {10, 5, 20}
print(10 in active_set)  # True ($O(1)$ instant lookup time)

# Iteration
for el in active_set:
    print(f"Elements: {el}")

# Sorting a Set (Returns a LIST, because Sets inherently cannot hold an order)
print(sorted(active_set))  # [5, 10, 20]

# ===== 4. MATHEMATICAL SET OPERATIONS
setA = {11, 22, 33, 44}
setB = {33, 44, 55, 66}

# Union (Combine both, drop duplicates)
print(setA.union(setB))  # {33, 66, 22, 55, 11, 44}

# Intersection (What is in BOTH?)
print(setA.intersection(setB))  # {33, 44}

# Difference (What is in A, but not B?)
print(setA.difference(setB))  # {11, 22}

# Symmetric Difference (What is in exactly ONE set, but not both?)
print(setA.symmetric_difference(setB))  # {66, 22, 55, 11}

# Subsets
print(setA.issubset(setB))  # False


# ===== 5. THE UNHASHABLE TRAP
# set in Python require all their elements to be immutable (hashable) types.
# You can put Tuples in a Set, because Tuples are locked (hashable).
# You CANNOT put Lists or Dictionaries in a Set.
valid_set = {1, 2, (3, 4)}

# invalid_set = {1, 2, [3, 4]}  <-- TypeError: unhashable type: 'list'

print("Copy of set:", valid_set.copy())
