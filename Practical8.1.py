# Open the source file to read
file1 = open("input.txt", "r")
data = file1.read()
file1.close()

# Convert data to uppercase
upper_data = data.upper()

# Open the destination file to write
file2 = open("output.txt", "w")
file2.write(upper_data)
file2.close()

print("File successfully copied in uppercase!")
