import pandas as pd

# Load the excel file
# Note: Ensure "employee.xlsx" is in the same folder as this script
df = pd.read_excel("employee.xlsx")

# a) Print list of employees working for "Automotive" domain
print("\n--- Employees in Automotive Domain ---")
automotive_emps = df[df['Department'] == 'Automotive']
print(automotive_emps)

# b) Print details of an employee by ID given by user
emp_id = int(input("\nEnter Employee ID to search: "))
employee_details = df[df['Employee ID'] == emp_id]
print(employee_details)

# d) Print list of all the Developers of Infosys
print("\n--- List of Developers ---")
developers = df[df['Designation'] == 'Developer']
print(developers)
