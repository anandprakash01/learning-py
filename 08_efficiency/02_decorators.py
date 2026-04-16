# In an enterprise application, you will often have hundreds of functions that all need the exact same check before they run. For example, checking if a user is logged in, measuring how long a database query takes, or writing a system log.

# Instead of pasting if not logged_in: return False inside all 500 functions (violating the DRY principle), we use Decorators.

# A decorator is a function that wraps around another function, intercepting the execution, doing something beforehand, and doing something afterward.

import time


# ===== 1. THE DECORATOR ARCHITECTURE
# A decorator is just a function that takes ANOTHER function as its argument.
def execution_timer(func):
    # We build a 'wrapper' inside. We use *args and **kwargs so this wrapper can protect ANY function, regardless of how many parameters it has.
    def wrapper(*args, **kwargs):
        # 1. PRE-EXECUTION LOGIC
        start_time = time.time()
        print("Start.....")
        # 2. THE ACTUAL EXECUTION
        # We trigger the original function and save whatever it spits out.
        result = func(*args, **kwargs)

        # 3. POST-EXECUTION LOGIC
        end_time = time.time()
        print(f"[METRICS] {func.__name__} took {end_time-start_time:.4f} seconds.")

        # 4. RETURN THE ORIGINAL RESULT
        return result

    return wrapper


# ===== 2. DEPLOYING THE DECORATOR (@)
# We use the "@" symbol (Syntactic Sugar) to attach the wrapper to a target.
# Python silently passes 'process_payments' into 'execution_timer'.


@execution_timer
def process_payments(batch_size):
    print(f"Processing {batch_size} payments...")
    time.sleep(1)  # Simulating a 1-second database operation
    return "Success"


# ===== 3. TRIGGERING THE ENGINE
# When you call this, you aren't actually calling process_payments anymore. You are calling the wrapper!
status = process_payments(500)
print(status)


user_role = "guest"


def admin_only(func):
    def wrapper(*args, **kwargs):
        print("start...////")
        if user_role == "admin":
            return func(*args, **kwargs)  #
        else:
            return "Unauthorized Access"

    return wrapper


@admin_only
def delete_database():
    return "Database Wiped"


print(delete_database())
user_role = "admin"
print(delete_database())
