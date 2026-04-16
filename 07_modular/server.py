# ===== 1. IMPORTING THE WHOLE MODULE

import database

print(database.connect_db("10.0.0.1"))
print(f"Server module name: {__name__}")  # __main__

# ===== 2. IMPORTING SPECIFIC FUNCTIONS (Cleaner memory footprint)

from database import query_users

print(query_users())

# ===== 3. IMPORTING WITH AN ALIAS
from database import connect_db as start_connection

print(start_connection("192.168.1.50"))
