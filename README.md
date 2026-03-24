# Security Log Analyzer (Python)

This project is a simple Python-based log analyzer that detects failed login attempts and identifies potential brute force attacks.

## Features
- Parses authentication logs
- Detects failed login attempts
- Tracks failed attempts per user
- Alerts when a user exceeds 3 failed login attempts (brute force detection)

## How It Works
The script reads a log file line by line, extracts usernames, and counts failed login attempts. If a user exceeds 3 failed attempts, a brute force alert is triggered.

## How to Run
1. Make sure Python is installed
2. Place your log file in the same directory
3. Run:

## Future Improvements
- Detect brute force attempts by IP address
- Add time-based detection (e.g., 3 attempts within 1 minute)
- Export alerts to a file
- Use regex for more robust parsing
