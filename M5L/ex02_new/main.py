from contact import Contact
from schedule import Schedule

def main():
    def get_contacts_from_user():
        contacts_list = []
        while True:
            name = input("\nEnter contact name (or '0' to finish): ")
            if name == '0':
                break
            phone_number = input("Enter contact phone number: ")
            contact = Contact(name, phone_number)
            contacts_list.append(contact)
        return contacts_list
    
    while True:
        print("\nMenu:")
        print("1. Get Contacts from User")
        print("2. Add Contact")
        print("3. Remove Contact")
        print("4. Edit Contact")
        print("5. Search by Name")
        print("6. Search by Phone Number")
        print("7. Display Schedule")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            contacts_list = get_contacts_from_user()
            schedule = Schedule(phone_book=contacts_list) 
            print("Contacts list created successfully.")
        elif choice == '2':
            name = input("\nEnter contact name: ")
            phone_number = input("Enter contact phone number: ")
            contact = Contact(name, phone_number)
            schedule.add_contact(contact)
            print("Contact added successfully.")
        elif choice == '3':
            name = input("\nEnter contact name to remove: ")
            schedule.remove_contact(name)
        elif choice == '4':
            name = input("\nEnter contact name to edit: ")
            schedule.edit_contact(name)
        elif choice == '5':
            name = input("\nEnter contact name to search: ")
            result = schedule.search_by_name(name)
            print(result)
        elif choice == '6':
            phone_number = input("\nEnter phone number to search: ")
            result = schedule.search_by_phone_number(phone_number)
            print(result)
        elif choice == '7':
            schedule.display_schedule()
        elif choice == '8':
            print("\nExiting...")
            break
        else:
            print("Invalid choice. Please try again.")

main()


