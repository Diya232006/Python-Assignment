# Input validation for start number
while True:
    start = input("Enter starting number: ")
    if start.isdigit() and int(start) >= 2:
        start = int(start)
        break
    else:
        print("Please enter a valid number >= 2")

# Input validation for end number
while True:
    end = input("Enter ending number: ")
    if end.isdigit() and int(end) >= start:
        end = int(end)
        break
    else:
        print(f"Please enter a valid number >= {start}")

print(f"Prime numbers between {start} and {end} are:")

for num in range(start, end + 1):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")