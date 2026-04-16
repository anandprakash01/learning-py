# ===== 1. CREATION & ALLOCATION
# Dictionary same as object in JavaScript or HashMap in Java
# Key-Value pairs, unordered, mutable, indexed by keys, keys must be unique and immutable types
dictionary = {
    "id": 101,
    "user": "Isha",
    "active": True,
    "lists": ["hey", "hi"],
}

empty_dict = {}  # Empty dictionary literal

dict_via_constructor = dict(id=101, user="Isha")  # Notice keys do not need quotes here!

# Nested dictionary
user_nested = {
    "person1": {"name": "anand", "age": 28},
    "person2": {"name": "isha", "age": 20},
}
print("Nested dictionary:", user_nested)

# ===== 2. ACCESSING DATA
print(dictionary["user"])  # "Isha" (Access value by key)
# print(dictionary["email"])  # KeyError! Using brackets crashes the program if the key is missing.

# The Pythonic Way: .get()
print(dictionary.get("user"))  # "Isha"
print(dictionary.get("email"))  # None
print(dictionary.get("email", "Not Found"))  # "Not Found" (Provides a fallback value)

# ===== 3. ADDING & MODIFYING (IN-PLACE)
dictionary["user"] = "Anand"  # If the key DOES exist, it overwrites the value.
dictionary["email"] = "email@example.com"  # If the key doesn't exist, it adds it.

# .update() merges another dictionary into this one. It overwrites matching keys.
dictionary.update({"id": 1, "role": "admin"})
print(dictionary)

# Copying dictionary
dict_copy = dictionary.copy()
print("Copied dictionary:", dict_copy)

# ===== 4. REMOVING DATA
# .pop(key) deletes the key-value pair and RETURNS the value so you can save it.
print(dictionary.pop("lists"))

# .popitem() removes the LAST inserted key-value pair and returns as a Tuple.
print(dictionary)
print(dictionary.popitem())

# 'del' keyword wipes the key from memory entirely without returning anything.
del dictionary["id"]

# ===== 5. ITERATION THROUGH DICTIONARY
config = {"host": "localhost", "port": 8080}

print(config.keys())  # dict_keys(['host', 'port'])
print(config.values())  # dict_values(['localhost', 8080])
print(config.items())  # dict_items([('host', 'localhost'), ('port', 8080)])

print(type(config.keys()))  # <class 'dict_keys'>

# Unpacking dictionary items in a loop (The Industry Standard)
for key in config:
    print(f"{key}: {config[key]}")

for k, v in config.items():
    print(f"key: {k} | value: {v}")

# ===== 6. ADVANCED DICTIONARY MECHANICS
# The 'in' operator ONLY checks Keys, it never checks values.
print("host" in config)  # True
print("localhost" in config)  # False

# .setdefault(key, default)
# Checks if a key exists. If it does, returns the value. If not, creates it with the default.
config.setdefault("timeout", 20)  # Adds "timeout": 30 to the dictionary

# ===== 7. DICTIONARY UNPACKING (PEP 448)
# The double asterisk (**) unpacks dictionaries (just like * unpacks lists).
base_cfg = {"theme": "dark", "lang": "en"}
user_cfg = {"lang": "hindi", "notify": True}

# Merges them into a brand new dictionary in memory. Overrides overwrite base keys.
final_cfg = {**base_cfg, **user_cfg}
print(final_cfg)

# ===== 8. CLEARING/DELETING DICTIONARY
# Clearing Dictionary
final_cfg.clear()  # Empties the dictionary
print("Cleared dictionary:", final_cfg)

# Deleting Dictionary
del final_cfg
# print(final_cfg) # This will raise NameError as final_cfg is deleted
