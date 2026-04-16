# Manually starting and joining thread_1, thread_2, thread_3 is fine for two files, but what if you have 10,000 files to download? You cannot create 10,000 threads—you will crash the operating system.

# Instead, we use a ThreadPoolExecutor. You give it a pool of workers (e.g., 5 threads), hand it 10,000 tasks, and it automatically assigns tasks to workers as they become available.

import concurrent.futures
import time


def process_user(user_id):
    time.sleep(2)
    return f"User {user_id} processed"


users = [101, 102, 103, 104, 105]

# We use our old friend, the Context Manager (with), to safely handle the threads max_workers=3 means only 3 threads are allowed to run at the exact same time.

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    # .map() automatically feeds the 'users' list into 'process_user',
    # distributes the work across the 3 threads, and gathers the results!
    results = executor.map(process_user, users)
    for res in results:
        print(res)


import threading
import time


def ping_server(ip_address):
    print(f"Pinging {ip_address}...")
    time.sleep(3)
    print(f"{ip_address} is online!")


servers = ["10.0.0.1", "10.0.0.2", "10.0.0.3"]

active_threads = []

for server in servers:
    thread_1 = threading.Thread(target=ping_server, args=(server,))
    active_threads.append(thread_1)
    thread_1.start()

for active in active_threads:
    active.join()

print("All servers scanned.")
