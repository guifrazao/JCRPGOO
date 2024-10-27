'''
M5L-ex02. Implemente uma classe chamada Schedule que represente uma agenda telefônica. 
Essa classe deve permitir adicionar, editar e remover contatos, além de buscar por 
contatos a partir de um nome ou número de telefone.
'''

class Schedule:
    def __init__(self):
        self.phone_book = []
        self.__smartphone = None

    def add_contact(self, name, phone_number):
        contact = {"name": name, "phone_number": phone_number}
        self.phone_book.append(contact)

    def remove_contact(self, name):
        for contact in self.phone_book:
            if contact["name"] == name:
                self.phone_book.remove(contact)
                print("Phone contact successfully deleted.")
                break

    def edit_contact(self, name):
        for contact in self.phone_book:
            if contact["name"] == name:
                edit_what = int(input("Would you like to change the contact's name, phone number or both?\n[1] - name\n[2] - phone number\n[3] - name and phone number\n"))
                if edit_what == 1:
                    contact["name"] = str(input("Enter a new contact name: "))
                elif edit_what == 2:
                    contact["phone_number"] = str(input("Enter a new contact phone number: "))
                else:
                    contact["name"] = str(input("Enter a new contact name: "))
                    contact["phone_number"] = str(input("Enter a new contact phone number: "))

    def search_by_name(self, name):
        for contact in self.phone_book:
            if contact["name"] == name:
                return f"{name}'s phone number is {contact['phone_number']}."
        return "The contact doesn't exist."

    def search_by_phone_number(self, phone_number):
        for contact in self.phone_book:
            if contact["phone_number"] == phone_number:
                return f"The phone number {phone_number} belongs to {contact['name']}."
        return "The contact doesn't exist."

    def display_schedule(self):
        print(f"\n{'Nome':10}|{'Número':12}")
        for contact in self.phone_book:
            print(f"{contact['name']:10}| {contact['phone_number']}")

    def set_smartphone(self, smartphone):
        self.__smartphone = smartphone

    def get_smartphone(self):
        return self.__smartphone
