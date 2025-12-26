# Employee details input
name = input("Enter Employee Name: ")
emp_id = input("Enter Employee ID: ")
department = input("Enter Department: ")
basic_salary = float(input("Enter Basic Salary: "))

# Calculations
da = 0.92 * basic_salary
hra = 0.58 * basic_salary
ta = 0.30 * basic_salary
lic = 500

gross_salary = basic_salary + da + hra + ta
net_salary = gross_salary - lic

# Display
print("Name:", name)
print("Employee ID:", emp_id)
print("Department:", department)
print("Basic Salary:", basic_salary)
print("DA:", da)
print("HRA:", hra)
print("TA:", ta)
print("Gross Salary:", gross_salary)
print("LIC Deduction:", lic)
print("Net Salary:", net_salary)