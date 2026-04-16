# There are two main bottlenecks in software:

# CPU Bound: Heavy math. The processor is working at 100% capacity.

# I/O Bound: Input/Output. The processor is doing nothing. It is just sitting there waiting for a network request, a database query, or a file download to finish.

# Multithreading solves I/O Bound bottlenecks. It allows Python to say: "While I am waiting for this file to download, I am going to switch to another thread and do some other work."

import threading
import time


# ===== 1. THE BOTTLENECK (Synchronous)
def download_file(filename):
    print(f"[START] Downloading {filename}...")
    time.sleep(3)  # Simulates waiting 3 seconds for a server response
    print(f"[DONE] {filename} complete.")


# If we run these normally, it takes 6 seconds total.
start_time = time.time()
download_file("Data_A.csv")
download_file("Data_B.csv")
end_time = time.time()

print(f"Total Execution Time:: {end_time - start_time:.4f} seconds")

# ===== 2. THE SOLUTION (Multithreading)
# We create "Threads" (mini sub-programs).
# Notice we pass the function name WITHOUT parentheses to the 'target',and the arguments as a Tuple.
thread_1 = threading.Thread(target=download_file, args=("Data_A.csv",))
thread_2 = threading.Thread(target=download_file, args=("Data_b.csv",))

start_time = time.time()

# .start() kicks off the thread in the background.
# The main Python program instantly moves to the next line without waiting!
thread_1.start()
thread_2.start()

# ===== 3. THE ARCHITECT'S LOCK (.join)
# If we do not use .join(), the main program will hit the end of the file and shut down BEFORE the background threads finish!
# .join() says: "Main program, pause right here until this thread finishes."
thread_1.join()
thread_2.join()

end_time = time.time()
print(f"Total Execution Time:: {end_time-start_time:.4f} seconds")
# Output: ~3.00 seconds (We did 6 seconds of work in 3 seconds!)
