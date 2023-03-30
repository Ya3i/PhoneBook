# Define an empty phonebook dictionary
phonebook = {}

# Function to add a contact to the phonebook
def add_contact(name, phone):
    phonebook[name] = phone
    print(f"Contact {name} added with phone number {phone}")

# Function to search for a contact in the phonebook and display the result
def search_contact(name):
    if name in phonebook:
        print(f"The phone number of {name} is {phonebook[name]}")
    else:
        print(f"{name} is not found in the phonebook")

# Function to remove a contact from the phonebook
def remove_contact(name):
    if name in phonebook:
        phonebook.pop(name)
        print(f"Contact {name} removed from the phonebook")
    else:
        print(f"{name} is not found in the phonebook")

# Main program loop
while True:
    print("\nPhonebook Menu:")
    print("1. Add a contact")
    print("2. Search for a contact")
    print("3. Remove a contact")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter the name: ")
        phone = input("Enter the phone number: ")
        add_contact(name, phone)

    elif choice == "2":
        name = input("Enter the name to search: ")
        search_contact(name)

    elif choice == "3":
        name = input("Enter the name to remove: ")
        remove_contact(name)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
