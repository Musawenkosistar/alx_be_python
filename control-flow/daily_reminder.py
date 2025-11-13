# Personal Daily Reminder Program

# Prompt the user for input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Handle priority (replaces Match Case)
if priority == "high":
    reminder = f"'{task}' is a high priority task"
elif priority == "medium":
    reminder = f"'{task}' is a medium priority task"
elif priority == "low":
    reminder = f"'{task}' is a low priority task"
else:
    reminder = None
    print("Enter a valid task!")

# Modify the reminder if the task is time-bound
if reminder:
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    else:
        reminder = "Note: " + reminder + ". Consider completing it when you have free time."

# Print the customized reminder
if reminder:
    print("\nReminder:", reminder)
