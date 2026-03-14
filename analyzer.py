# Open the log file and read all lines
with open("sample_logs.txt", "r") as file:
    lines = file.readlines()

print("Total log entries:", len(lines))
print()

# Loop through each line
for line in lines:
    clean_line = line.strip()

    # Check if line contains a failed login
    if "LOGIN_FAILURE" in clean_line:
        print("ALERT: Failed login detected!")
        print(clean_line)
        print()
