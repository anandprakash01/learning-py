# The absolute most important concept here is Immutability. Once a string is allocated in memory, its contents cannot be changed. Any operation that seems to modify a string actually creates a new string object in memory.

# ======= 1. STRING CREATION
word1 = 'Hello'  # Single quotes
word2 = "World"  # Double quotes
multi_line = """Line 1
Line 2
Line 3
""" # Triple quotes
print(word1)
print(word2)
print(multi_line)
print(type(word1)) # <class 'str'>

# String concatenation and repetition
greeting = word1 + ", " + word2 + "!"  # Concatenation
echo = "Echo! " * 3  # Repetition
print(greeting) # Hello, World!
print(echo)     # Echo! Echo! Echo!
# String Membership
text = "anand Prakash"
isIn = "anand" in text
print("'anand' in text?:", isIn)
isNotIn = "xyz" not in text
print("'xyz' not in text?:", isNotIn)

# String Comparisons (lexicographical order based on Unicode code points)
print("apple" < "banana")  # True (a comes before b)
print("Apple" < "apple")  # True (uppercase letters have lower code points than lowercase)
print("cat" == "cat")     # True (exact match)
print("cat" == "Cat")     # False (case-sensitive)
print("cat" != "dog")     # True (different words)
print("cat" < "catalog")  # True (shorter string comes first if the prefix matches)
print("cat" >= "cat")    # True (equal strings are considered greater than or equal)

# ======= 2. INDEXING (Zero-Based)
text = "Python"
print(len(text))   # 6 (Length of the string)
print(text[0])    # 'P'
print(text[-1])   # 'n' (Last character via negative indexing)
print(text[-2])   # 'o' (Second to last)
# print(text[10])  # This will raise an IndexError (out of range)
# text[0] = 'J'   # This will raise an error because strings are immutable.

# ======= 3. SLICING [start:stop:step]
  # Remember: 'start' and 'stop' are indices, 'start' is inclusive and 'stop' is EXCLUSIVE.
alpha = "012345"

print(alpha[0:3])  # '012' substring from index 0 to 2 (3 is exclusive)
print(alpha[2:5])  # '234' substring from index 2 to 4
print(alpha[2:6])  # '2345' substring from index 2 to 5
print(alpha[2:99])  # '2345' substring from index 2 to end last (99 is out of range but it doesn't raise an error, it just goes to the end)
print(alpha[2:])   # '2345' (From index 2 to end)
print(alpha[:4])   # '0123' (From start to index 3)
print(alpha[::2])  # '024' (Every 2nd character)
print(alpha[1::2]) # '135' (Every 2nd character starting from index 1)
print(alpha[-3:])  # '456' (Last 3 characters)
print(alpha[:-2])  # '01234' (All but skip last 2 characters)
print(alpha[::-1])  # '543210' (Reversed string)
print(alpha[5:2:-1])# '543' (Indices 5,4,3 in reverse)

print(alpha[-4:-1]) # '234' (From index -4 to -2, -1 is exclusive)


# ======= 4. ESCAPE CHARACTERS AND RAW STRINGS
  # The backslash (\) escapes special characters.
path1 = "c:\\new_folder\\test.txt" # \\ creates a single \
tabbed = "A\tB\tc" # \t creates a tab space
newline = "Hi\nThere" # \n creates a new line

# RAW STRINGS (Prefix with 'r'): Instructs the interpreter to ignore escape characters.
  # Vital for Windows paths and Regular Expressions.
raw_path = r"c:\new_folder\test.txt"

print(path1)
print(tabbed)
print(newline)
print(raw_path)

# ======= 5. STRING FORMATTING (f-strings)
  # Industry standard (Python 3.6+). Prefix with 'f' and inject variables in {}.

user = "Anand"
age = 35
greeting = f"My name is {user} and I am {age} years old."
print(greeting)

  # String Formatting with %
  # Older style, still widely used in legacy code. Uses %s for strings, %d for integers, and %f for floats.
formatted = "My name is %s and I am %d years old." % (user, age)
print(formatted)
  # String Formatting with format()
  # More powerful and flexible than % formatting. Uses {} as placeholders.
formatted2 = "My name is {} and I am {} years old.".format(user,age)
print(formatted2)

text = "   python PROGRAMMING is fun!   \n"

# ======= 6. CLEANING METHODS (Whitespace Management)
print(text.strip())    # Removes leading and trailing whitespace (spaces, tabs, newlines)
print(text.lstrip())   # Removes only left (leading) whitespace
print(text.rstrip())   # Removes right (trailing) whitespace

# ======= 7. CASING METHODS
text = text.strip()
print(text.upper())    # Converts to uppercase
print(text.lower())    # Converts to lowercase
print(text.title())    # Converts to title case
print(text.capitalize()) # Converts first character to uppercase and the rest to lowercase
print(text.swapcase()) # Swaps case of each character


# ======= 8. SEARCHING & REPLACING
# .replace(old, new, [count]) -> Count is optional, limits how many to replace.
sentence = "The cat sat on the mat."
print(sentence.replace("cat", "dog")) # Replaces all occurrences
print(sentence.replace(" ", "_", 3)) # Replaces first 3 spaces with underscores

# .find(substring) -> Returns the starting INDEX of the substring. Returns -1 if not found.
print(sentence.find("cat")) # Outputs: 4
print(sentence.find("dog")) # Outputs: -1 (not found)

# .count(substring) -> Returns how many times the substring appears.
print(sentence.count("t")) # t appears 4 times


# ======= 9. SPLITTING AND JOINING (Bridge to Data Structures)
# .split(delimiter) breaks a string into a List of strings.
words = sentence.split(" ")
print(words)  # Outputs: ['The', 'cat', 'sat', 'on', 'the', 'mat.']

# .join(iterable) combines a list of strings into a single string.
joined = "_".join(words)
print(joined)  # Outputs: The_cat_sat_on_the_mat.

# ======= 10. BOOLEAN/VALIDATION METHODS (Returns True/False)
# These are crucial for sanitizing user input before casting.
print("123".isdigit())   # True (All characters are digits)
print("abc".isalpha())   # True (All characters are alphabetic)
print("abc123".isalnum())  # True (All characters are alphanumeric)
print("   ".isspace())   # True (All characters are whitespace)
print("Hello".isupper())  # False (Not all characters are uppercase)
print("Hello".islower())  # False (Not all characters are lowercase)
print("Hello".istitle())  # True (First character uppercase, rest lowercase)

# .startswith() and .endswith()
url = "https://secure-server"
print(url.startswith("https")) # True
print(url.endswith(".org"))    # False

# ======= 11. MEMORY PROOF OF IMMUTABILITY
name = "cat"
print(id(name)) # Memory address A
# We cannot change the 'c' to 'b'. We must reassign the variable.
name = "bat"
print(id(name)) # Memory address B (Completely new object in memory)