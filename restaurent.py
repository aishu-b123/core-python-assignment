def add(menu, item):
    menu.append(item)
    return menu

def remove_item(menu, item):
    if item in menu:
        menu.remove(item)
        return menu
    else:
        return f"Item '{item}' not found in the menu."

def check(menu, item):
    if item.lower() in menu:
        return f"'{item}' is available."
    else:
        return f"'{item}' is not available."

def display_menu():
    print("\nMenu Options:")
    print("1.Add item")
    print("2.Remove item")
    print("3.Check item availability")
    print("4.Exit")

def main():
    menu = ["pizza", "burger", "pasta", "salad"]
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            item = input("Enter the item to add to the menu: ")
            menu = add(menu, item)
            print(f"'{item}' has been added to the menu.")
        elif choice == '2':
            item = input("Enter the item to remove from the menu: ")
            result = remove_item(menu, item)
            if isinstance(result, list):
                print(f"'{item}' has been removed from the menu.")
            else:
                print(result)
        elif choice == '3':
            item = input("Enter the item to check availability: ")
            availability = check(menu, item)
            print(availability)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
