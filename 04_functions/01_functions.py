# Functions are isolated blocks of reusable logic. They do not execute until they are explicitly called.

# Parameter: The variable defined inside the parentheses when creating the function.

# Argument: The actual data you pass into the function when calling it.


# ===== 1. BASIC DEFINITION & DOCSTRINGS
def greet(name):
    """This is a Docstring (PEP 257). It documents what the function does.
    Modern IDEs display this text when you hover over the function name elsewhere."""
    print(f"Welcome,{name}")


greet("Anand")


# ===== 2. POSITIONAL VS KEYWORD ARGUMENTS
def calc_damage(base, multi):
    return base - multi


# Positional: Mapped strictly by order (base=10, dam=2)
res = calc_damage(10, 2)
print(res)

# Keyword: Mapped by explicit name. Order no longer matters.
print(calc_damage(multi=2, base=10))

# ===== 3. DEFAULT PARAMETERS & THE MUTABLE TRAP
# Default parameters MUST come LAST in the parameter list.


def connect(host, port=8080):
    print(f"Connecting  to {host}:{port}")


connect("localhost")
connect("localhost", 3000)

# THE MUTABLE DEFAULT TRAP (Critical Enterprise Warning)
# NEVER use a mutable object (like [] or {}) as a default parameter.
# The list is allocated in memory ONLY ONCE when the function is compiled.
# BAD: def add_item(item, cart=[]):


def add_to_cart(item, cart=[]):
    cart.append(item)
    return cart


print(add_to_cart(5))
print(
    add_to_cart(10)
)  # [5,10],incorrect | this returns both items because list is allocated only once on function compilation


# GOOD (The Industry Standard):
def add_item(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart


print(add_item(5))
print(add_item(10))

# ===== 4. RETURN MECHANICS
# Functions evaluate to whatever they 'return'.
# If you don't write 'return', Python secretly returns 'None' at the end.


def check_status():
    return "Active"  # The function terminates the exact millisecond it hits a return.


# Returning Multiple Values (Implicit Tuple Packing)
def get_coords():
    return 10, -5


x, y = get_coords()  # Instantly unpacking the returned tuple

# ===== 5. ARBITRARY ARGUMENTS (*args and **kwargs)
# Sometimes you don't know how many arguments a user will pass.


# *args: Gathers unlimited POSITIONAL arguments into a TUPLE.
def sum_all(*args):
    print(type(args))  # <class 'tuple'>
    return sum(args)


print(sum_all(1, 2, 3, 4, 5))  # Outputs: 15


# **kwargs: Gathers unlimited KEYWORD arguments into a DICTIONARY.
# Positional argument cannot appear after keyword arguments
def build_profile(**kwargs):
    # build_profile() takes 0 positional arguments
    print(type(kwargs))
    return kwargs


print(build_profile(user="Anand", role="admin"))


# ===== 6. MODERN TYPE HINTING (PEP 484)
# Python is dynamically typed, meaning you can pass anything into a function.
# Type Hints do not stop code from running, but they allow linters and IDEs to warn you if you pass the wrong data type.
def process_data(data: list, is_strict: bool = True):
    """Processes a list and returns an integer representing the status code."""
    if is_strict:
        return len(data)
    return 0


print(process_data([2, 3], False))


# recursion

# factorial


def factorial(num):
    if num == 1 or num == 0:
        return 1
    return num * factorial(num - 1)


print(f"Factorial : {factorial(4)}")
