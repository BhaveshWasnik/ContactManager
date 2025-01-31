import json

def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)

def display_contacts(contacts):
    if not contacts:
        print("No contacts available.")
    else:
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("Contact added successfully.")

def delete_contact(contacts):
    display_contacts(contacts)
    try:
        index = int(input("Enter the number of the contact to delete: ")) - 1
        if 0 <= index < len(contacts):
            removed_contact = contacts.pop(index)
            save_contacts(contacts)
            print(f"Deleted contact: {removed_contact['name']}")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    contacts = load_contacts()

    while True:
        print("\nContact Manager")
        print("1. View Contacts")
        print("2. Add Contact")
        print("3. Delete Contact")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            display_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            delete_contact(contacts)
        elif choice == "4":
            print("Exiting Contact Manager. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
