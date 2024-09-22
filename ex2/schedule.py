'''
Implemente uma classe chamada Schedule que represente uma agenda telefônica.Essa classe deve permitir adicionar, editar e remover contatos, além de buscar por contatos a partir de um nome ou número de telefone.
'''

class Schedule:
    def __init__(self):
        self.phone_book = []

    def add_contact(self, name, phone_number):
        contact = {"name": name, "phone_number": phone_number}
        self.contact = contact
        self.phone_book.append(self.contact)
    
    def remove_contact(self, name):
        for c in range(len(self.phone_book) - 1, -1, -1):
            if self.phone_book[c]["name"] == name:
                del self.phone_book[c]
                print("Phone contact successfully deleted.")

    def edit_contact(self, name):
        for c in range(len(self.phone_book)):
            if self.phone_book[c]["name"] == name:
                edit_what = int(input("Would you like to change the contact's name, phone number or both?\n[1] - name\n[2] - phone number\n[3] - name and phone number\n"))
                if edit_what == 1:
                    self.phone_book[c]["name"] = str(input("Enter a new contact name: "))
                elif edit_what == 2:
                    self.phone_book[c]["phone_numbera"] = int(input("Enter a new contact phone number: "))
                else:
                    self.phone_book[c]["name"] = str(input("Enter a new contact name: "))
                    self.phone_book[c]["phone_number"] = int(input("Enter a new contact phone number: "))

    def search_by_name(self, name):
        for c in range(len(self.phone_book)):
            if self.phone_book[c]["name"] == name:
                return f"{name}'s phone number is {self.phone_book[c]["phone_number"]}."
        return "The contact doesn't exist."
   
    def search_by_phone_number(self, phone_number):
        for c in range(len(self.phone_book)):
            if self.phone_book[c]["phone_number"] == phone_number:
                return f"The phone number {phone_number} belongs to {self.phone_book[c]["name"]}."
        return "The contact doesn't exist."
  
    def display_schedule(self):
        print()
        print(f"{'Nome':10}|{' Número':12}")
        for contact in self.phone_book:
            print(f"{contact["name"]:10}| {contact["phone_number"]}")
    