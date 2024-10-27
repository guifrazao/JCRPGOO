'''
M5L-ex02. Implemente uma classe chamada Schedule que represente uma agenda telefônica. 
Essa classe deve permitir adicionar, editar e remover contatos, além de buscar por 
contatos a partir de um nome ou número de telefone. 
'''

from typing import List
from contact import Contact

class Schedule:
    def __init__(self, phone_book: List[Contact]):  # Lista de contatos injetada de fora
        self.phone_book = phone_book

    def add_contact(self, contact: Contact):
        self.phone_book.append(contact)

    def remove_contact(self, name: str):
        self.phone_book = [contact for contact in self.phone_book if contact.get_name() != name]
        print("Phone contact successfully deleted.")

    def edit_contact(self, name):
        for contact in self.phone_book:
            if contact.get_name() == name:
                edit_what = int(input("Would you like to change the contact's name, phone number or both?\n[1] - name\n[2] - phone number\n[3] - name and phone number\n"))
                if edit_what == 1:
                    contact.set_name(str(input("Enter a new contact name: ")))
                elif edit_what == 2:
                    contact.set_phone_number(int(input("Enter a new contact phone number: ")))
                else:
                    contact.set_name(str(input("Enter a new contact name: ")))
                    contact.set_phone_number(int(input("Enter a new contact phone number: ")))

    def search_by_name(self, name: str):
        for contact in self.phone_book:
            if contact.get_name() == name:
                return f"{name}'s phone number is {contact.get_phone_number()}."
        return "The contact doesn't exist."

    def search_by_phone_number(self, phone_number: int):
        for contact in self.phone_book:
            if contact.get_phone_number() == phone_number:
                return f"The phone number {phone_number} belongs to {contact.get_name()}."
        return "The contact doesn't exist."

    def display_schedule(self):
        print(f"\n{'Name':10}|{'Phone Number':12}")
        for contact in self.phone_book:
            print(f"{contact.get_name():10}| {contact.get_phone_number()}")
