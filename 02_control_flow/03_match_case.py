# ===== 1. THE BASIC MATCH
# The match-case statement is a powerful control flow structure that allows you to compare a value against multiple patterns and execute code based on which pattern matches. It is similar to switch-case statements in other languages but with more advanced pattern matching capabilities.

command = "start"

match command:
    case "start":
        print("Engine starting...")
    case "stop":
        print("Engine stopping...")
    case "pause":
        print("Engine paused.")
    case _:
        # The underscore (_) is a wildcard pattern that matches anything. It serves as a default case if no other patterns match. exactly like an 'else' block.
        print("Unknown command.")

# ===== 2. MATCHING MULTIPLE VALUES (The OR operator in cases)
# You can use the pipe (|) to group multiple values into a single case. This is useful when you want to execute the same code for multiple patterns.
status = "error"
match status:
    case "success" | "completed":
        print("Operation successful.")
    case "error" | "failed":
        print("Operation failed.")
    case _:
        print("Unknown status.")

# 3. GUARD CLAUSES (If statements inside cases)
# You can attach an 'if' statement to a case to add Boolean logic to further refine the pattern matching. This is called a guard clause and allows you to execute code only if certain conditions are met.
# This makes Python's match-case vastly superior to a standard 'switch' statement.

curr_temp = 105
match curr_temp:
    # We create a temporary variable 'temp' to represent current_temperature,then immediately check a mathematical condition against it.
    case temp if temp > 100:
        print("CRITICAL: Core overheating!")
    case temp if temp < 0:
        print("CRITICAL: Core freezing!")
    case _:
        print("Temperature nominal.")


# ==================
curr_temp = 105

match curr_temp:
    # Match anything (_), but only proceed if curr_temp > 100
    case _ if curr_temp > 100:
        print("CRITICAL: Core overheating!")
    case _ if curr_temp < 0:
        print("CRITICAL: Core freezing!")
    case _:
        print("Temperature nominal.")


# ==================
# This feature is incredibly useful when you are extracting data out of a complex structure.
data = {"status": "active", "temperature": 105}
match data:
    # This extracts the 105 and names it 'temp'
    case {"temperature": temp} if temp > 100:
        print(f"Overheating at {temp} degrees!")


# ==================
command = ["move", "player_1", "north"]
match command:
    case ["move", player, direction]:
        # It automatically unpacks "player_1" into the 'player' variable!
        print(f"Moving {player} to the {direction}.")
    case ["attack", target]:
        print(f"Attacking {target}.")
    case _:
        print("Unknown command.")
