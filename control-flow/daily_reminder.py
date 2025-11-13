# Personal Daily Reminder Program (Python <3.10 compatible)

# Prompt for user inputs
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Handle priority using if-elif-else
if priority == "high":
    message = f"'{task}' is a high priority task"
elif priority == "medium":
    message = f"'{task}' is a medium priority task"
elif priority == "low":
    message = f"'{task}' is a low priority task"
else:
    message = f"'{task}' has an unknown priority level"

# Modify message based on time sensitivity
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    message = "Note: " + message + ". Consider completing it when you have free time."

# Print final reminder
print("\nReminder:", message)

