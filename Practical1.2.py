
vendor_name = input("Enter Vendor Name: ")
year_of_association = input("Enter Year of Association: ")
contact_number = input("Enter Contact Number: ")
email_id = input("Enter Email ID: ")

monthly_purchases = []
for month in range(1, 13):
    purchase = float(input(f"Enter purchase amount for month {month}: "))
    monthly_purchases.append(purchase)
total_purchase = sum(monthly_purchases)

print("\n--- Annual Purchase Report ---")
print("Vendor Name:", vendor_name)
print("Year of Association:", year_of_association)
print("Contact Number:", contact_number)
print("Email ID:", email_id)
print("Monthly Purchases:", monthly_purchases)
print("Total Annual Purchase:", total_purchase)