# The walrus operator (:=), officially known as an assignment expression, is one of the most debated and ultimately beloved features added to Python (introduced in Python 3.8).

# Normally in Python, assigning a variable (using =) is a statement. It does its job, but it doesn't return a value.

# The walrus operator (:=) is an expression. It does two things at the exact same time:
# Assigns a value to a variable.
# Returns that value immediately so it can be used in the same line of code.

# The basic syntax: (variable_name := expression)

# Standard assignment (statement)
x = 5
print(x)  # Output: 5

# Walrus operator (expression)
print(x := 5)  # Assigns 5 to x, AND prints 5 immediately. Output: 5

# Use Case A: Cleaning up while loops
# This is the most common use case. Often, you need to read data (from a file, user input, or a network socket) until a certain condition is met.

# Before (Without Walrus):
# You had to repeat the input() function twice—once before the loop, and once inside it.
# the not-equal operator (!=) has a higher priority than the walrus operator (:=)
user_input = input("Enter a command (or 'quit'): ")
while user_input != "quit":
    print(f"Executing: {user_input}")
    user_input = input("Enter a command (or 'quit'): ")  # Repeated!

# After (With Walrus):
while (user_input := input("Enter a command (or 'quit'): ")) != "quit":
    print(f"Executing: {user_input}")


# Use Case C: List Comprehensions
# Before (Without Walrus):
numbers = [1, 2, 3, 4, 5]


def f(x):
    return x**3


# f(x) runs twice for every item!
results = [f(x) for x in numbers if f(x) > 20]
# Output: [27, 64, 125]

# After (With Walrus):
numbers = [1, 2, 3, 4, 5]


def f(x):
    return x**3


results = [y for x in numbers if (y := f(x)) > 20]
# Output: [27, 64, 125]
