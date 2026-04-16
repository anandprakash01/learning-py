# In standard procedural programming, if you need to process 10 million database records, a standard for loop or List Comprehension will attempt to load all 10 million records into your server's RAM at the exact same time. This results in a catastrophic Out Of Memory (OOM) crash.

# To solve this, we use Generators. A generator is a special type of function that does not return a final value and destroy itself. Instead, it uses the yield keyword to hand you one single piece of data, and then it completely freezes its state in memory, waiting for you to ask for the next piece.

# ===== 1. THE RAM CRASH (Standard Lists)
# This creates a massive list in memory instantly.

import sys


def get_list_data():
    results = []
    for i in range(10000):
        results.append(i)
    return results


huge_list = get_list_data()
print(f"List Memory: {sys.getsizeof(huge_list)} bytes")  # ~85,000 bytes

# ===== 2. THE ENTERPRISE SOLUTION (Generators)
# Notice there is no list, and no 'return' keyword.


def get_generator_data():
    for i in range(10000):
        yield i  # "Here is the number. I will pause here until you need the next one."


# When you call a generator, it does NOT run the code. It creates a Generator Object.

tiny_generator = get_generator_data()
print(f"Generator Memory: {sys.getsizeof(tiny_generator)} bytes")
# ~190 bytes (Massive savings!)


# ===== 3. CONSUMING A GENERATOR
# You pull data out of a generator using the built-in next() function, or by looping over it.
def server_status_stream():
    yield "Booting..."
    yield "Connecting to DB..."
    yield "ONLINE."


status = server_status_stream()

print(next(status))  # Outputs: Booting...
print(next(status))  # Outputs: Connecting to DB...
print(next(status))  # Outputs: Online.
# print(next(status)) <-- StopIteration Error! The generator is exhausted and empty.


# ===== 4. GENERATOR EXPRESSIONS
# You can write a generator on a single line, exactly like a List Comprehension,  but using parentheses () instead of square brackets [].

# List Comprehension (Bad for large data)
squares_list = [x**2 for x in range(1000)]
print(type(squares_list))
print(f"Memory: {sys.getsizeof(squares_list)} bytes")  # ~8800 bytes


# Generator Expression (Enterprise standard for large data)
squares_gen = (x**2 for x in range(1000))
print(type(squares_gen))
print(f"Generator Memory: {sys.getsizeof(squares_gen)} bytes")  # ~200 bytes


def reboot_countdown(start_num):
    while start_num > 0:
        yield start_num
        start_num -= 1


timer = reboot_countdown(3)
print(next(timer))
print(next(timer))
print(next(timer))
# print(next(timer))  # StopIteration exception
