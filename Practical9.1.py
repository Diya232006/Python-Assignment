class Employee:
    def get_input(self):
        self.name = input("Enter Name: ")
        self.age = input("Enter Age: ")
        self.salary = input("Enter Salary: ")
        self.address = input("Enter Address: ")

    def display_info(self):
        print(f"Name: {self.name} | Age: {self.age} | Salary: {self.salary} | Address: {self.address}")

class Manager(Employee):
    # Inherits all methods and attributes from Employee
    pass

# List to store 10 managers
managers_list = []

print("--- Enter Details for 10 Managers ---")
for i in range(1, 11):
    print(f"\nManager {i}:")
    m = Manager()
    m.get_input()
    managers_list.append(m)

print("\n--- Displaying Manager Information ---")
for m in managers_list:
    m.display_info()
