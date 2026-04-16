# When you create a variable, Python places it in a specific "Scope" (a temporary or permanent memory namespace). Python resolves variable names using the strict LEGB Rule:

# Local: Inside the current function.
# Enclosing: Inside any enclosing (nested) functions.
# Global: At the top level of the module/script.
# Built-in: Python's pre-allocated keywords (print, len, sum).

# If a variable is born inside a function, it dies the exact millisecond the function returns.

# ===== 1. LOCAL VS GLOBAL SCOPE
server_name = "Alpha"  # GLOBAL Scope (Accessible anywhere)


def reboot_server():
    status = "Rebooting"  # LOCAL Scope (Only accessible inside this block)
    print(f"Server {server_name} is {status}")


reboot_server()
# print(status) <-- NameError: name 'status' is not defined. It is dead.

# ===== 2. THE GLOBAL SHADOWING TRAP
# If you try to change a global variable inside a function without permission, Python assumes you want to create a BRAND NEW local variable with the exact same name.
threat_level = 1


def escalate_threat():
    threat_level = 5
    # This does NOT change the global variable. It "shadows" it locally.
    print(f"Inside function: {threat_level}")  # Prints 5


escalate_threat()
print(f"Outside function: {threat_level}")  # Prints 1 (The global is untouched!)


# ===== 3. THE GLOBAL AND NONLOCAL KEYWORDS
# To actually mutate a global variable from inside a function, you must declare intent.


def force_escalate():
    global threat_level  # "Do not create a new variable. Give me the global pointer."
    threat_level = 5  # Now, this permanently changes the global state.


force_escalate()
print(f"After global mutation: {threat_level}")  # Prints 5

# The Architect's Warning:
# Relying heavily on the `global` keyword is considered a massive architectural "code smell."
# It makes your code unpredictable. Always try to pass data in as arguments and return it instead.


# 'nonlocal' is used for Nested Functions (Enclosing scope)
def outer_func():
    x = "Outer"

    def inner_func():
        nonlocal x  # "Give me the pointer to the variable in the function directly above me."
        x = "Inner"

    inner_func()
    print(x)  # Returns "Inner"


outer_func()


# ===== 4. ANONYMOUS FUNCTIONS (Lambdas)
# Sometimes you need a tiny, single-use function, but you don't want to waste lines
# defining it with 'def'. Lambdas are single-line, nameless functions.
# Syntax: lambda arguments: expression_to_return


# Standard definition
def square(x):
    return x**2


# Lambda equivalent
square_lambda = lambda x: x**2
print(square_lambda(5))  # Outputs: 25

# Why use Lambdas? (Enterprise Use Case)
# They are heavily used as the "key" argument for sorting complex data structures.
users = [
    {"name": "Alice", "level": 10},
    {"name": "Bob", "level": 99},
    {"name": "Charlie", "level": 5},
]
# Sort the dictionaries based strictly on the "level" value.
# The lambda silently iterates through the list, temporarily assigning each dict to 'u'.
users.sort(key=lambda u: u["level"])

print(users)  # Charlie (5), Alice (10), Bob (99)
