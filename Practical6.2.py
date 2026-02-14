def capitalize_lines(lines):
    for line in lines:
        print(line.upper())

# Input multiple lines from user until empty line entered
print("Enter lines (press Enter on empty line to stop):")
lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

capitalize_lines(lines)