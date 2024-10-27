'''
M5L-ex02. Implemente uma classe chamada Schedule que represente uma agenda telefônica. 
Essa classe deve permitir adicionar, editar e remover contatos, além de buscar por 
contatos a partir de um nome ou número de telefone. 
'''

from contact import Contact

class Schedule:
    def __init__(self):
        self.phone_book = [] 

    def add_contact(self, contact: Contact):
        self.phone_book.append(contact)
    
    def remove_contact(self, name):
        contact = self.search_by_name(name)
        self.phone_book.remove(contact)
        print("Phone contact successfully deleted.")

    def edit_contact(self, name):
        contact = self.search_by_name(name)
        if not self.__verify_contact_exists(contact):
            print("Contact does not exist")
        else:
            self.__edition_menu(contact)

    def search_by_name(self, name):
        for contact in self.phone_book:
            if self.__verify_contact_exists(contact) and contact.get_name() == name:
                return contact
        return None
   
    def search_by_phone_number(self, phone_number):
        for contact in self.phone_book:
            if contact.get_phone_number() == phone_number:
                return contact
        return None
  
    def display_schedule(self):
        print(f"\n{'Nome':10}|{'Número':12}")
        for contact in self.phone_book:
            print(contact)
    
    def __verify_contact_exists(self, contact):
        if contact in self.phone_book:
            return True
        return False
    
    def __edition_menu(self, contact):
        edit_what = int(input("\nWould you like to change the contact's name, phone number or both?\n[1] - name\n[2] - phone number\n[3] - name and phone number\n"))
        if edit_what == 1:
            contact.set_name(str(input("\nEnter a new contact name: ")))
        elif edit_what == 2:
            contact.set_phone_number(str(input("\nEnter a new contact phone number: ")))
        else:
            contact.set_name(str(input("\nEnter a new contact name: ")))
            contact.set_phone_number(str(input("Enter a new contact phone number: ")))
