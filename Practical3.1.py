# PRACTICAL 3 - ALL PATTERNS USING LOOPS

# 1. Increasing Number Pattern
print("Pattern 1:")
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end="")
    print()


# 2. Same Number Pattern
print("\nPattern 2:")
for i in range(1, 6):
    for j in range(i):
        print(i, end="")
    print()


# 3. Reverse Number Pattern
print("\nPattern 3:")
for i in range(1, 6):
    for j in range(i, 0, -1):
        print(j, end="")
    print()


# 4. Binary Pattern
print("\nPattern 4:")
for i in range(1, 6):
    for j in range(1, i+1):
        print(j % 2, end="")
    print()


# 5. Special Even Number Pattern
print("\nPattern 5:")
num = 2
for i in range(1, 5):
    for j in range(i):
        print(num, end=" ")
        num += 2
    print()


# 6. Star Pattern
print("\nPattern 6:")
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()