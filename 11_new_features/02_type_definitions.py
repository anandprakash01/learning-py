# Python is famously a dynamically typed language, meaning you usually don't have to declare whether a variable is a string, an integer, or a list. Python just figures it out on the fly.

# However, as projects grow larger, this flexibility can lead to confusing bugs. To fix this, Python introduced Type Hints (or type annotations). They allow you to explicitly state what type of data a variable, function argument, or return value should be.


n: int = 5
name: str = "Anand"
# Helpful for empty structures
users: list[str] = []


# 🚨 The Golden Rule: They are just "Hints"
# you must understand one critical concept: Python does not enforce type hints at runtime.
# If you say a variable should be an integer, but you pass it a string, Python will still try to run the code. Type hints are primarily for you, your IDE (like VS Code or PyCharm), and static analysis tools (like mypy) to catch errors before you run the code.
def sum(a: int, b: int) -> tuple:  # tuple is return type
    # return a, b
    return f"{a} and {b}"


print(sum(2.1, "3"))


# Working with Collections (Lists, Dicts, Tuples)
# In modern Python (version 3.9 and newer), you can use standard collection names to define what goes inside them.

# A list where every item must be an integer
scores: list[int] = [25, 50, 75, 100]

# A dictionary where keys are strings, and values are floats
prices: dict[str, float] = {"apple": 120, "Banana": 50}

# A tuple containing exactly a string, an integer, and a boolean
user_info: tuple[str, int, bool] = ("Anand", 35, True)


# Advanced Types: Unions and Optionals
# Sometimes a variable might be one of several types, or it might be None. Python 3.10 introduced a very clean syntax using the pipe | (meaning "or").


# Multiple Acceptable Types (Union):
# The ID can be an integer OR a string
def process_id(user_id: int | str) -> None | str:
    print(f"Processing ID: {user_id}")


# Why should you use Type Hints?
# Incredible IDE Autocomplete: If VS Code knows a variable is a string, typing variable. will instantly show you all string methods (like .upper() or .split()).
# Acts as Documentation: You no longer need to read through a function's code to guess what data it expects. The signature tells you everything.
# Catches Bugs Early: By running a tool like mypy against your code, it will scan your files and flag type mismatches before your code ever hits production.
