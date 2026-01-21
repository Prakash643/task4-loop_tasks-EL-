"""
TASK 4: Loops & Iterations
Demonstrates for loops, while loops, break, continue,
string iteration, tables, range with steps, and conditions.
"""

print("===== TASK 4: LOOPS & ITERATIONS =====\n")

# ---------------------------------------------------
# 1. FOR LOOP: Print numbers from 1 to 100
# Real-world example: Printing roll numbers of students
# ---------------------------------------------------
print("1. Numbers from 1 to 100:")
for i in range(1, 101):
    print(i, end=" ")
print("\n")

# ---------------------------------------------------
# 2. WHILE LOOP: Countdown timer
# Real-world example: Countdown before launching a rocket
# ---------------------------------------------------
print("2. Countdown Timer:")
count = 5
while count > 0:
    print("Countdown:", count)
    count -= 1
print("🚀 Launch!\n")

# ---------------------------------------------------
# 3. BREAK STATEMENT
# Real-world example: Stop searching once item is found
# ---------------------------------------------------
print("3. Break Example:")
for number in range(1, 11):
    if number == 6:
        print("Number found! Stopping loop.")
        break
    print(number)
print()

# ---------------------------------------------------
# 4. CONTINUE STATEMENT
# Real-world example: Skip unavailable products
# ---------------------------------------------------
print("4. Continue Example (Skip even numbers):")
for number in range(1, 11):
    if number % 2 == 0:
        continue
    print(number)
print()

# ---------------------------------------------------
# 5. ITERATE OVER STRING CHARACTERS
# Real-world example: Checking each character in a password
# ---------------------------------------------------
print("5. Iterating over string characters:")
name = "Python"
for char in name:
    print(char)
print()

# ---------------------------------------------------
# 6. MULTIPLICATION TABLE
# Real-world example: Learning math tables
# ---------------------------------------------------
print("6. Multiplication Table of 5:")
num = 5
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
print()

# ---------------------------------------------------
# 7. RANGE WITH STEPS
# Real-world example: Printing alternate days
# ---------------------------------------------------
print("7. Range with steps (Even numbers from 2 to 20):")
for i in range(2, 21, 2):
    print(i, end=" ")
print("\n")

# ---------------------------------------------------
# 8. LOOP WITH CONDITIONS
# Real-world example: Checking pass/fail status
# ---------------------------------------------------
print("8. Loop with conditions (Pass/Fail):")
marks = [35, 78, 90, 42, 20]
for mark in marks:
    if mark >= 40:
        print(mark, "- Pass")
    else:
        print(mark, "- Fail")
print()

# ---------------------------------------------------
# 9. REAL-WORLD AUTOMATION EXAMPLE
# Real-world example: Sending notifications
# ---------------------------------------------------
print("9. Real-world Automation Example:")
users = ["Admin", "Manager", "Intern", "Guest"]

for user in users:
    if user == "Guest":
        print("Skipping guest user")
        continue
    print(f"Sending notification to {user}")

print("\n===== END OF LOOP TASKS =====")
