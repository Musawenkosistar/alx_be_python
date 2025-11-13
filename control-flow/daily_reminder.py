# Personal Daily Reminder Program

# Prompt user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Handle priority logic (replaces Match Case for Python <3.10)
if priority == "high":
    reminder_message = f"'{task}' is a high priority task"
elif priority == "medium":
    reminder_message = f"'{task}' is a medium priority task"
elif priority == "low":
    reminder_message = f"'{task}' is a low priority task"
else:
    reminder_message = f"'{task}' has an unknown priority level"

# Modify reminder if the task is time-bound
if time_bound == "yes":
    reminder_message += " that requires immediate attention today!"
else:
    reminder_message += ". Consider completing it when you have free time."

# Print the customized reminder
print(f"Reminder: {reminder_message}")

