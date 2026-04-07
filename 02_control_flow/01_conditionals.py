player_health = 65
max_health = 100

# 1. THE STANDARD IF / ELIF / ELSE BLOCK
# Notice the colon (:) at the end of every condition. This tells Python a new block is starting.
# Python evaluates top-to-bottom and triggers the FIRST block that evaluates to True.

if player_health <= 0:
    print("Player is dead.")
else:
    print("Player is alive.")

# 'elif' stands for 'else if'. You can have as many elifs as you want.
if player_health <= 0:
    print("Player is dead.")
elif player_health <= 10:
    print("Critical warning! Health is low.")
elif player_health == max_health:
    print("Health is full.")
else:
    print("Player is alive and stable.")

print("Health check complete.")

# 2. NESTED CONDITIONALS
# You can put if-statements inside if-statements.
# You just add another 4 spaces (8 total spaces from the margin).

is_poisoned = True

if player_health > 0:
    print("Player is alive.")
    if is_poisoned:
        print("...but taking poison damage!")
else:
    print("Player is dead.")

# 3. TRUTHY AND FALSY EVALUATION
# You do not need to explicitly write "== True" or "!= 0".
# Python automatically coerces objects into Booleans in an if-statement.
# Remember: 0, None, and empty sequences ("") are Falsy. Everything else is Truthy.

inventory = ""  # Empty string (Falsy)
enemy_count = 5  # Non-zero integer (Truthy)
active_buffs = None  # Singleton (Falsy)

# Bad Practice (Redundant):
# if enemy_count > 0:

# Architectural Standard:
if enemy_count:
    print(f"There are {enemy_count} enemies nearby!")

if not inventory:
    print("Your inventory is empty.")

# Conditional expressions (Ternary Operator)
# A compact way to write simple if-else statements in a single line.
# Syntax: value_if_true if condition else value_if_false

player_status = (
    "Healthy" if player_health > 50 else "Injured"
)  # This will set player_status to "Healthy" if player_health is greater than 50, otherwise it will set it to "Injured".
print(player_status)
