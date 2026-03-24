failed_login_count = {}
# Open the log file and read all lines
with open("sample_logs.txt", "r") as file:
    lines = file.readlines()

print("Total log entries:", len(lines))
print()

# Loop through each line
for line in lines:
    clean_line = line.strip()

    # Check if the line contains a failed login
    if "LOGIN_FAILURE" in clean_line:
        print("ALERT: Failed login detected!")
        print(clean_line)

        #extract username
        if "user=" in clean_line:
            parts = clean_line.split("user=")
            if len(parts) > 1:
                username = parts[1].split()[0]

        if username not in failed_login_count:
            failed_login_count[username] = 0

        failed_login_count[username] += 1

        if failed_login_count[username] >= 3:
            print(f"BRUTE FORCE ALERT: {username}) has {failed_login_count[username]} failed login attempts!")
