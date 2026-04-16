# ===== 1. THE WHILE LOOP
# You MUST manually update the condition variable inside the loop,
# otherwise you create an infinite loop that will crash the system.
server_retries = 3
while server_retries > 0:
    print("Attempting to connect to the server...")
    server_retries -= 1  # Crucial: We decrement the counter.
print("Server connection failed.")

# ===== 2. THE FOR LOOP (Iterating over a sequence)
# A string is a sequence of characters. Python automatically grabs one character at a time and temporarily assigns it to the variable 'char'.
target_word = "UPLINK"

for char in target_word:
    # This will print U, P, L, I, N, K on separate lines.
    print(f"Transmitting byte: {char}")

# ===== 3. RANGE() - GENERATING NUMBERS
# range(stop) -> Starts at 0, stops BEFORE the number.
for i in range(5):
    print(f"count: {i}")  # Outputs: 0, 1, 2, 3, 4

# range(start, stop, step) -> Jumps by the step value.
# stop argument is exclusive, so it will stop before reaching the stop value.
for i in range(0, 10, 2):
    print(f"even count: {i}")  # Outputs: 0, 2, 4, 6, 8

# Counting backwards requires a negative step.
for i in range(5, 0, -1):
    print(f"countdown in reverse: {i}")  # Outputs: 5, 4, 3, 2, 1

# ===== 4. Loop Mechanics (break, continue, pass, and else)

# break: Exits the loop immediately.
for i in range(10):
    if i == 5:
        break
    print(f"count: {i}")  # Outputs: 0, 1, 2, 3, 4

# continue: Skips the rest of the current iteration and instantly jumps back to the top of the loop for the next cycle.
for i in range(10):
    if i % 2 == 0:
        continue
    print(f"odd count: {i}")  # Outputs: 1, 3, 5, 7, 9

# pass: A null operation. Does nothing; used as a placeholder when a statement is syntactically required but no action is needed. Python's indentation rules require something to be inside an if or for block, even if you haven't written the code yet.
for i in range(5):
    if i == 3:
        pass  # Placeholder for future code
    print(f"count: {i}")  # Outputs: 0, 1, 2, 3, 4

# The Loop else Clause: This is unique to Python. You can attach an else statement directly to a for or while loop. The else block triggers ONLY IF the loop finishes naturally (i.e., it was never stopped by a break statement). It is heavily used in search algorithms.

for i in range(5):
    print(f"count: {i}")
else:
    print("Loop completed without interruption.")


# ===== enumerate
l = [1, 25, 35, 45]

for index, item in enumerate(l):
    print(f"The item at index {index} is {item}")
