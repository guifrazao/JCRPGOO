from modules import *

def main():
    schedule = Schedule()
    smartphone = None

    while True:
        print("\nMenu:")
        print("1. Create Smartphone and Associate Schedule")
        print("2. Add Contact")
        print("3. Remove Contact")
        print("4. Edit Contact")
        print("5. Search by Name")
        print("6. Search by Phone Number")
        print("7. Display Schedule")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            model = input("Enter smartphone model: ")
            smartphone = Smartphone(model)
            smartphone.set_schedule(schedule)
            schedule.set_smartphone(smartphone)
            print("Smartphone created and schedule associated successfully.")
        elif choice == '2':
            name = input("Enter contact name: ")
            phone_number = input("Enter contact phone number: ")
            schedule.add_contact(name, phone_number)
            print("Contact added successfully.")
        elif choice == '3':
            name = input("Enter contact name to remove: ")
            schedule.remove_contact(name)
        elif choice == '4':
            name = input("Enter contact name to edit: ")
            schedule.edit_contact(name)
        elif choice == '5':
            name = input("Enter contact name to search: ")
            result = schedule.search_by_name(name)
            print(result)
        elif choice == '6':
            phone_number = input("Enter phone number to search: ")
            result = schedule.search_by_phone_number(phone_number)
            print(result)
        elif choice == '7':
            schedule.display_schedule()
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please try again.")

main()
