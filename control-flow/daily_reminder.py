task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Handle priority with if-elif-else
if priority == "high":
    reminder = f"'{task}' is a {priority} priority task"
elif priority == "medium":
    reminder = f"'{task}' is a {priority} priority task"
elif priority == "low":
    reminder = f"'{task}' is a {priority} priority task"
else:
    reminder = None
    print("Enter a valid task!")

# Print the reminder if valid
if reminder:
    if time_bound == "yes":
        print(f"Reminder: {reminder} that requires immediate attention today!")
    else:
        print(f"Note: {reminder}. Consider completing it when you have free time.")
