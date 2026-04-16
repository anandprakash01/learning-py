# When you open a file, the operating system locks it. If your program crashes before you explicitly call .close(), that file remains locked in memory, eventually causing a catastrophic memory leak or data corruption. To prevent this, modern Python relies entirely on Context Managers.

# ===== 1. THE OLD WAY (Dangerous)
# If an error happens between open() and close(), the file stays locked forever.

path = "./06_resilience/files/"

# f = open("server_log.txt", "w")  # this will add at base directory
f = open(path + "server_log.txt", "w")  # default mode is "r"
f.write("System booted")
f.close()

# ===== 2. THE ENTERPRISE STANDARD (Context Managers)
# The 'with' keyword creates a safe context. The exact millisecond the block ends (or if the program crashes inside the block), Python automatically closes the file.

# Access Modes:
# 'r' = Read (Default. Crashes if file doesn't exist)
# 'w' = Write (Overwrites the entire file. Creates it if missing)
# 'a' = Append (Adds to the bottom of the file. Creates it if missing)

with open(path + "system_log.txt", "w") as file:
    file.write("Initialization complete.\n")
    file.write("Awaiting commands...\n")
# The file is safely closed here automatically.

# ===== 3. READING DATA
with open(path + "system_log.txt", "r") as file:
    # .read() loads the ENTIRE file into a single string. (Dangerous for massive files)
    content = file.read()
    print(content)

with open(path + "system_log.txt", "r") as file:
    # .readlines() loads each line as a string inside a List.
    lines = file.readlines()
    print(lines)  # ['Initialization complete.\n', 'Awaiting commands...\n']

# ===== 4. ITERATING LARGE FILES (Memory Safe)
# If a log file is 50GB, .read() will instantly crash your server's RAM.
# The safest way is to stream it line-by-line using a standard 'for' loop.

with open(path + "system_log.txt") as file:
    for line in file:
        # .strip() removes the invisible '\n' newline characters
        print(f"Log entry: {line.strip()}")
