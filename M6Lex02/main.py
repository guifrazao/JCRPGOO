'''
Implemente uma classe chamada Schedule que represente uma agenda telefônica.Essa classe deve permitir adicionar, editar e remover contatos, além de buscar por contatos a partir de um nome ou número de telefone.
'''

from schedule import Schedule
from contact import Contact

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

        try:
            option = 0
            while option < 1 or option > 7:
                option = int(input("Choose an option: "))
                if option >= 1 or option <= 7:
                    break 
            if option == 1:
                name = str(input("\nContact's name: "))
                phone_number = input("Contact's phone: ")
                contact = Contact(name, phone_number)
                schedule.add_contact(contact)
            elif option == 2:
                name = str(input("\nContact's name: "))
                schedule.edit_contact(name)
            elif option == 3:
                name = str(input("\nContact's name: "))
                schedule.remove_contact(name)
            elif option == 4:
                name = str(input("\nContact's name: "))
                if schedule.search_by_name(name) == None:
                    print("Contact does not exist")
                else:
                    print(schedule.search_by_phone_number(phone_number))
            elif option == 5:
                phone_number = str(input("\nPhone number: "))
                if schedule.search_by_phone_number(phone_number) == None:
                    print("Contact does not exist")
                else:
                    print(schedule.search_by_phone_number(phone_number))
            elif option == 6:
                schedule.display_schedule()
            else:
                print("\nExiting phone schedule...")
                print("See you later!" )
                break
        except Exception as err:
            print(err)

main()