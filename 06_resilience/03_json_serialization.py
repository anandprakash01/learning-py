# You cannot save a Python Dictionary directly to a text file, nor can you send a Python Dictionary over the internet to a JavaScript server. The data must be converted into a universal string format. That format is JSON (JavaScript Object Notation).

# Serialization (Dumping): Converting a Python object into a JSON string.

# Deserialization (Loading): Parsing a JSON string back into a Python object.

import json

# ===== 1. IN-MEMORY CONVERSION (Strings)
user_dict = {"name": "Admin", "level": 99, "active": True}
# .dumps() (Dump String) - Converts Python dict to JSON formatted string
json_string = json.dumps(user_dict)
print(type(json_string))  # <class 'str'>
print(json_string)
# Output: '{"name": "Admin", "level": 99, "active": true}' (Notice 'true' is lowercase!)

# .loads() (Load String) - Parses JSON string back into Python dict
parsed_dict = json.loads(json_string)
print(type(parsed_dict))  # <class 'dict'>
print(parsed_dict)
# Output: {'name': 'Admin', 'level': 99, 'active': True}

path = "./06_resilience/files/"
# ===== 2. FILE CONVERSION (Reading and Writing JSON Files)
config_data = {"host": "10.0.0.1", "ports": [80, 443], "secure": True}
# .dump() (No 's') - Writes the dictionary directly into a file
with open(path + "config.json", "w") as file:
    # indent=4 formats the file to be highly readable for humans
    json.dump(config_data, file, indent=4)

# .load() (No 's') - Reads the file and instantly parses it into a dictionary
with open(path + "config.json", "r") as file:
    loaded_config = json.load(file)
    print(loaded_config.get("ports"))
