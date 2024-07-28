import os
import json

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        return {
            'name': self.name,
            'phone': self.phone,
            'email': self.email
        }

class ContactManager:
    def __init__(self, filename):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return [Contact(**data) for data in json.load(file)]
        return []

    def save_contacts(self):
        with open(self.filename, 'w') as file:
            json.dump([contact.to_dict() for contact in self.contacts], file, indent=4)

    def add_contact(self, contact):
        self.contacts.append(contact)
        self.save_contacts()

    def delete_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact.name != name]
        self.save_contacts()

    def view_contacts(self):
        return self.contacts

def main():
    manager = ContactManager('contacts.json')
    while True:
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. View Contacts")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            contact = Contact(name, phone, email)
            manager.add_contact(contact)
        elif choice == '2':
            name = input("Enter name to delete: ")
            manager.delete_contact(name)
        elif choice == '3':
            contacts = manager.view_contacts()
            for contact in contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")
        elif choice == '4':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
