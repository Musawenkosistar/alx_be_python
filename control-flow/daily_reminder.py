# Personal Daily Reminder Program

# Prompt the user for input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Handle priority
if priority == "high":
    reminder_message = f"'{task}' is a high priority task"
elif priority == "medium":
    reminder_message = f"'{task}' is a medium priority task"
elif priority == "low":
    reminder_message = f"'{task}' is a low priority task"
else:
    reminder_message = f"'{task}' has an unknown priority level"

# Modify reminder based on time sensitivity
if time_bound == "yes":
    reminder_message += " that requires immediate attention today!"
else:
    reminder_message += ". Consider completing it when you have free time."

# Print the customized reminder (always starts with 'Reminder:')
print(f"Reminder: {reminder_message}")

