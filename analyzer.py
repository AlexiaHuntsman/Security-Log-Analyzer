# Open the log file and read all lines
with open("sample_logs.txt", "r") as file:
    lines = file.readlines()

# Print each line
for line in lines:
    print(line.strip())
