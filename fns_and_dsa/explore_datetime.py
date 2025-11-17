from datetime import datetime, timedelta


def display_current_datetime():
    # Save current date and time in the required variable
    current_date = datetime.now()

    # Format the output: YYYY-MM-DD HH:MM:SS
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")

    print(f"Current date and time: {formatted_date}")

    # Return current_date so it can be reused if needed
    return current_date


def calculate_future_date(days):
    # Get today's date
    today = datetime.now()

    # Save future date in required variable
    future_date = today + timedelta(days=days)

    # Format output: YYYY-MM-DD
    formatted_future = future_date.strftime("%Y-%m-%d")

    print(f"Future date: {formatted_future}")

    return future_date


def main():
    # Part 1 — Display Current Date and Time
    display_current_datetime()

    # Part 2 — Ask user for number of days
    days_input = input("Enter the number of days to add to the current date: ")

    # Validate input
    if days_input.isdigit():
        days = int(days_input)
        calculate_future_date(days)
    else:
        print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()
