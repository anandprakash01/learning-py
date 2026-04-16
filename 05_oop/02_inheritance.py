# Inheritance: A child class automatically gaining all methods and attributes of a parent class.

# super(): A built-in function that acts as a direct bridge from the child class back to the parent class. It is most commonly used inside the child's constructor to ensure the parent's setup logic runs.

# Polymorphism (Method Overriding): If a child class doesn't like how the parent class does something, it can completely overwrite the parent's method with its own version.


# ===== 1. THE PARENT CLASS (Base Blueprint)
class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary
        self.company = "Stark Industries"

    def calculate_pay(self):
        print(self.base_salary)
        return self.base_salary

    def get_details(self):
        print(f"{self.name} works at {self.company}")


# ===== 2. THE CHILD CLASS (Inheritance)


# To inherit, we pass the Parent class name into parentheses after the Child class name.
class Developer(Employee):
    def __init__(self, name, base_salary, language):
        # THE ARCHITECT'S BRIDGE: super()
        # Instead of manually recreating self.name and self.base_salary, we tell the Parent class to handle its own setup.
        super().__init__(name, base_salary)

        # Now we add the attribute unique only to Developers.
        self.language = language

    # ===== 3. POLYMORPHISM (Method Overriding)
    # Developers get bonuses. We completely overwrite the parent's calculate_pay method.
    def calculate_pay(self):
        bonus = 5000
        # We can still use super() inside methods to grab the parent's original math!
        original_pay = super().calculate_pay()
        print(original_pay + bonus)
        return original_pay + bonus


# ===== 4. THE EXECUTION & TYPE CHECKING
generic_worker = Employee("Peter", 50000)
lead_dev = Developer("Anand", 80000, "Python")

# The Child inherited get_details() without us writing a single line of code for it!
lead_dev.get_details()

# Polymorphism in action: They share a method name, but execute different logic.
generic_worker.calculate_pay()  # Outputs: 50000
lead_dev.calculate_pay()  # Outputs: 85000 (80000 + 50000)

# ===== 5. ENTERPRISE TYPE CHECKING
# isinstance() checks if an object is built from a specific class (or its parent).

print(isinstance(lead_dev, Developer))  # True
print(isinstance(lead_dev, Employee))  # True
print(isinstance(generic_worker, Developer))  # False (An Employee is NOT a Developer)

# issubclass() checks the blueprints themselves, not the objects.
print(issubclass(Developer, Employee))  # True
