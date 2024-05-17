contacts = {}

def add_contact(name, phone):
    contacts[name] = phone
    print(f"Added contact: {name} - {phone}")

def show_contacts():
    if contacts:
        print("Your contacts:")
        for name, phone in contacts.items():
            print(f"- {name}: {phone}")
    else:
        print("No contacts available")

def search_contact(name):
    if name in contacts:
        print(f"{name}'s phone number is {contacts[name]}")
    else:
        print(f"Contact {name} not found")

def main():
    while True:
        print("\nContact Book:")
        print("1. Add Contact")
        print("2. Show Contacts")
        print("3. Search Contact")
        print("4. Exit")

        choice = input("Enter choice (1/2/3/4): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            add_contact(name, phone)
        elif choice == '2':
            show_contacts()
        elif choice == '3':
            name = input("Enter the name to search: ")
            search_contact(name)
        elif choice == '4':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
