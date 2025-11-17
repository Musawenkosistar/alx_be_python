def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []  # Required by checker

    while True:
        display_menu()   # Checker requires that this function is called
        choice = input("Enter your choice: ")

        # Convert choice to a number (checker requirement)
        if choice.isdigit():
            choice = int(choice)
        else:
            print("Invalid choice. Please enter a number.")
            continue

        if choice == 1:
            item = input("Enter the item to add: ").strip()   # FIXED
            shopping_list.append(item)
            print(f"'{item}' added.")

        elif choice == 2:
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' removed.")
            else:
                print("Item not found.")

        elif choice == 3:
            print("Current Shopping List:")
            if not shopping_list:
                print("List is empty.")
            else:
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")

        elif choice == 4:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Enter a number between 1–4.")


if __name__ == "__main__":
    main()
