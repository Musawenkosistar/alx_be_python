# Pattern Drawing using Nested Loops

# Prompt the user to enter the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer while loop controls the number of rows
while row < size:
    # Inner for loop prints asterisks in one row
    for col in range(size):
        print("*", end="")
    # Move to the next line after each row
    print()
    # Increment row counter
    row += 1

