# When you import a Python file, Python silently runs every single line of code in that file from top to bottom before returning to your main script. This creates a massive architectural danger: if your module has test prints or function calls at the bottom, they will all execute the moment someone imports it!

# To fix this, we use the Main Guard (if __name__ == "__main__":). This tells Python: "Only run the code in this block if I am running this specific file directly. If I am being imported by someone else, ignore this block."


def connect_db(host):
    return f"Connected to DB at {host}"


def query_users():
    return ["Alice", "Bob", "Charlie"]


print(f"Database module name : {__name__}")

# ===== THE MAIN GUARD (The Enterprise Standard) =====
# Without this, the test below would print every time someone imports this file.
if __name__ == "__main__":
    # this code only executes by running this file directly
    print(f"Database module name : {__name__}")
    print("--- Running Local Database Tests ---")
    print(connect_db("127.0.0.1"))
    print(query_users())


# Under the hood, Python automatically assigns the string "__main__" to the hidden __name__ variable of whichever file you run directly. For any file that gets imported, Python changes that variable to the file's actual name (e.g., "auth"). That simple string check is what protects enterprise systems from executing thousands of lines of test code on startup.
