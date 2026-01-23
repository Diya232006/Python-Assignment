# TASK-2 ALL PATTERNS

# 1. Alphabet Increasing Pattern
print("Pattern 1:")
for i in range(65, 70):   # A to E
    for j in range(65, i+1):
        print(chr(j), end="")
    print()


# 2. Star with Space Pattern
print("\nPattern 2:")
for i in range(1, 6):
    for j in range(1, 6):
        if j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# 3. Character Changing Pattern
print("\nPattern 3:")
ch_list = ['y', 't', 'b', 'o', 'p']  # similar to image style
for i in range(5):
    print(ch_list[i] * (i+1))


# 4. Python Word Pattern
print("\nPattern 4:")
word = "Python"
for i in range(1, len(word)+1):
    print(word[:i])