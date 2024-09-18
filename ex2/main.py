from schedule import Schedule

schedule = Schedule()

def main():
    while True:
        print("\n=== Phone Schedule Menu ===")
        print("1. Add Contact") 
        print("2. Edit Contact")
        print("3. Remove Contact")
        print("4. Search by Name")
        print("5. Search by Phone")
        print("6. Display All Contacts")
        print("7. Exit")

        option = 0
        while option < 1 or option > 7:
            option = int(input("Choose an option: "))
            if option >= 1 or option <= 7:
                break 
        if option == 1:
            name = str(input("\nContact's name: "))
            phone = int(input("Contact's phone: "))
            schedule.add_contact(name, phone)
        elif option == 2:
            name = str(input("\nContact's name: "))
            schedule.edit_contact(name)
        elif option == 3:
            name = str(input("\nContact's name: "))
            schedule.remove_contact(name)
        elif option == 4:
            name = str(input("\nContact's name: "))
            print(schedule.search_by_name(name))
        elif option == 5:
            phone_number = int(input("\nPhone number: "))
            print(schedule.search_by_phone_number(phone_number))
        elif option == 6:
            schedule.display_schedule()
        else:
            print("Exiting phone schedule...")
            print("See you later!" )
            break

main()