# In Object-Oriented Programming, we group the Data (attributes) and the Behavior (methods) together into a single structural unit called an Object.

# Class: The blueprint. It does not exist in memory as a usable object; it is just the instructions for how to build one.

# Instance: The actual, physical object created from the blueprint.

# Attributes: Variables that live inside an object.

# Methods: Functions that live inside an object.

# self: The most important concept in OOP. It is the literal memory pointer that points to the specific instance currently being used.

# ===== 1. THE CLASS BLUEPRINT
# Class names use PascalCase (Capitalizing Every Word) by strict enterprise convention.


class Server:
    # Class Attribute: Shared across EVERY single server(Instance) we ever create.
    # If we change this, it changes for all servers instantly.
    domain = "internal.net"

    # ===== 2. THE CONSTRUCTOR (__init__)
    # The double-underscore (dunder) init method is called automatically the exact millisecond you create a new instance.
    # 'self' is mandatory. It tells Python: "Attach these variables to THIS specific object(Instance)."

    def __init__(self, hostname, ip_address):
        print("Creating an object")
        # Instance Attributes: Unique to this specific server.
        self.hostname = hostname
        self.ip_address = hostname
        self.is_active = False
        # We can define attributes without requiring them as parameters.

    # ===== 3. INSTANCE METHODS
    # Methods MUST take 'self' as their very first parameter.
    def boot(self):
        self.is_active = True
        print(f"System: {self.hostname} is booting up...")

    def ping(self, target_ip):
        # Methods can take other arguments just like normal functions,
        # but 'self' must always remain first.
        if self.is_active:
            print(f"{self.hostname} is pinging {target_ip}...")
        else:
            print(f"Error: {self.hostname} is currently offline.")


# ===== 4. INSTANTIATION (Building the Objects)
# We call the class name like a function to trigger the __init__ constructor.
# Notice we do NOT pass anything for 'self'. Python handles the pointer automatically.

server_1 = Server("Alpha", "10.0.0.1")
server_2 = Server("Beta", "10.0.0.2")

# ===== 5. ACCESSING DATA & BEHAVIOR
# We use "dot notation" to access attributes and methods.
print(server_1.hostname)  # Outputs: Alpha
print(server_1.is_active)  # Outputs: False

# Triggering behavior
server_1.boot()  # System: Alpha is booting up...
server_1.ping("192.168.1.1")  # Alpha is pinging 192.168.1.1...
server_2.ping("192.168.1.1")  # Error: Beta is currently offline.


# ============STATIC AND CLASS METHODs
class Student:
    roll_no = 21
    language = [
        "cpp",
        "java",
        "py",
        "js",
    ]

    @classmethod
    def show_roll_no(cls):
        print(f"Roll no. :{cls.roll_no}")

    @staticmethod  # Now this do not take self
    def getDetails():
        print("Hey! how are you?")

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    @name.setter
    def name(self, value):
        self.first_name = value.split(" ")[0]
        self.last_name = value.split(" ")[1]

    def get_info(self):
        print(f"The languages are:  {self.language}")


s1 = Student()
print(s1.language)

s2 = Student()
s2.language = "JavaScript"
# Instance attribute take preferences over class attributes during assignment and retrieval.
print(s2.language)  # Instance attribute take preference

# anand.get_info()
Student.get_info(
    s2
)  # under the hood this type is called when calling fun thats why we take self as parameter
s2.getDetails()  # staticmethod

# classmethod
s2.roll_no = 45
s2.show_roll_no()  # because used classmethod this will show the class roll no

# ======Decorators
# property
s2.name = "Anand Prakash"
print(s2.name)
# setter
print(s2.first_name)
print(s2.last_name)

# ====== Operator overloading


class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n

    def __len__(self, num1, num2):
        return "Anything can be done here on len method"


n = Number(10)
m = Number(10)

print(n + m)
