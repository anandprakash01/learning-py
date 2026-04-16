# ===== 1. THE BASIC TRY-EXCEPT BLOCK
# Put the dangerous code in the 'try' block. If it fails, the 'except' block catches it.

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero. Defaulting to 0")
    result = 0

# ===== 2. THE "NAKED EXCEPT" TRAP
# NEVER write a bare 'except:' without specifying the error type.
# It catches EVERYTHING, including you trying to exit the program with Ctrl+C, making your code impossible to debug.

# BAD:
# except:
#     print("Something went wrong")

# GOOD (Catching exactly what you expect):
# except TypeError:

# ===== 3. CAPTURING THE EXCEPTION OBJECT
# You can catch the actual error object to log its specific system message using 'as e'.

try:
    number = int("Hello")
except ValueError as e:
    print(f"System Log: Invalid conversion. Python says: {e}")


# ===== 4. try / except / else / finally


def process_data(data):
    try:
        # 1. Attempt the dangerous operation
        value = data["status"]
    except KeyError:
        # 2. Runs ONLY if a KeyError occurs
        print("Error: 'status' key is missing.")
    except Exception as e:
        # 3. The Fallback: Catches any other unforeseen errors (Exception is the base class)
        print(f"CRITICAL: Unhandled error: {e}")
    else:
        # 4. Runs ONLY if the 'try' block succeeds WITHOUT errors
        print(f"Success! Status is: {value}")
    finally:
        # 5. Runs ABSOLUTELY ALWAYS, crash or no crash.
        # Crucial for closing database connections or files.
        print("Cleaning up system resources...\n")


process_data({"status": "Active"})  # Triggers try -> else -> finally
process_data({"name": "Admin"})  # Triggers try -> except KeyError -> finally


def check_finally():
    try:
        print("Try Block")
        return "Try ran successfully!"
        # although return is here finally will still run
    except Exception as e:
        print("Exception Block")
        return "Exception ran"
    finally:
        print("Finally Block")
        return "Finally ran successfully!"


print(check_finally())


# ===== 5. RAISING CUSTOM EXCEPTIONS
# Sometimes the system isn't broken, but the logic violates your business rules.
# You can force a crash intentionally using the 'raise' keyword.
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be a negative number")
    print(f"Age set to {age}")


set_age(-5)  # <-- This will halt the program with your custom traceback.
print("last line")
