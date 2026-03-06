# Get filenames from the user
source = input("Enter the source filename (e.g., script.py): ")
destination = input("Enter the destination filename: ")

# 1. Read from source and write to destination without comments
file_in = open(source, "r")
file_out = open(destination, "w")

for line in file_in:
    # Check if the line is NOT a comment
    if not line.strip().startswith("#"):
        file_out.write(line)

file_in.close()
file_out.close()

# 2. Print content of the Source File
print("\n--- Content of Source File ---")
f1 = open(source, "r")
print(f1.read())
f1.close()

# 3. Print content of the Destination File
print("\n--- Content of Destination File ---")
f2 = open(destination, "r")
print(f2.read())
f2.close()
