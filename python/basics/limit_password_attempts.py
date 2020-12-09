"""
Give user five attempts to type "your password"
"""

import sys

for attempts_left in range(5, 0, -1):
    password = input("Type your password: ")
    if password == "your password":
        break
    print(f"This isn't your password. Attempts left: {attempts_left - 1}")
else:
    print("SUSPICIOUS ACTIVITY. POLICE ALERTED!")
    sys.exit(8)
print("Yes, this was \"your password\". Have a nice day!")
