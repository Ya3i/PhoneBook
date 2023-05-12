#Create by : Yasin Allahyari & Abolfazl ostadi :)
#instagram : @i._.ya3in
#E-mail : Yasinallahyari@yahoo.com

book = {"phone"}

def check_book(dict,name):
    return name in book[dict]

# add a contact to the phonebook
def add_contact(name, phone):
    book["phone"].update({name:phone})
    print(f"Contact {name} added with phone number {phone}")

# search for a contact in the phonebook and display the result
def search_contact(name):
    if check_book("phone",name):
        print(f"{'*'*8}  The phone number of {name} is {book['phone'][name]}")
    else:
        print(f"{name} is not found in the phonebook")

# remove a contact from the phonebook
def remove_contact(name):
    if check_book("phone",name):
        book["phone"].pop(name)
        print(f"Contact {name} removed from the phonebook")
    else:
        print(f"{name} is not found in the phonebook")

while True:
    print("""\n*****
Phonebook Menu:
1. Add/edit a contact
2. Search for a contact
3. Remove a contact
4. Quit""")


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
