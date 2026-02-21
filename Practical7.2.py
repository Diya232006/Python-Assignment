# Initial balance
balance = 0.0

def display_balance():
    print(f"\nYour current balance is: ${balance:.2f}")

def deposit():
    global balance
    amount = float(input("Enter amount to deposit: "))
    if amount > 0:
        balance += amount
        print(f"Successfully deposited ${amount:.2f}")
    else:
        print("Invalid amount.")

def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))
    if 0 < amount <= balance:
        balance -= amount
        print(f"Successfully withdrew ${amount:.2f}")
    elif amount > balance:
        print("Insufficient funds!")
    else:
        print("Invalid amount.")

while True:
    print("\n--- Bank Menu ---")
    print("a) Display Balance")
    print("b) Deposit")
    print("c) Withdraw")
    print("q) Quit")
    
    choice = input("Select an option: ").lower()
    
    if choice == 'a':
        display_balance()
    elif choice == 'b':
        deposit()
    elif choice == 'c':
        withdraw()
    elif choice == 'q':
        print("Thank you for using our bank services!")
        break
    else:
        print("Invalid choice, please try again.")
