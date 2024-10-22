class AddContact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    def execute(self, phone_book):
        contact = {"name": self.name, "phone_number": self.phone_number}
        phone_book.append(contact)

class RemoveContact:
    def __init__(self, name):
        self.name = name

    def execute(self, phone_book):
        phone_book[:] = [c for c in phone_book if c["name"] != self.name]
        print("Phone contact successfully deleted.")

class EditContact:
    def __init__(self, name):
        self.name = name

    def execute(self, phone_book):
        for c in phone_book:
            if c["name"] == self.name:
                edit_what = int(input("Would you like to change the contact's name, phone number or both?\n[1] - name\n[2] - phone number\n[3] - name and phone number\n"))
                if edit_what == 1:
                    c["name"] = str(input("Enter a new contact name: "))
                elif edit_what == 2:
                    c["phone_number"] = int(input("Enter a new contact phone number: "))
                else:
                    c["name"] = str(input("Enter a new contact name: "))
                    c["phone_number"] = int(input("Enter a new contact phone number: "))

class SearchByName:
    def __init__(self, name):
        self.name = name

    def execute(self, phone_book):
        for c in phone_book:
            if c["name"] == self.name:
                return f"{self.name}'s phone number is {c['phone_number']}."
        return "The contact doesn't exist."

class SearchByPhoneNumber:
    def __init__(self, phone_number):
        self.phone_number = phone_number

    def execute(self, phone_book):
        for c in phone_book:
            if c["phone_number"] == self.phone_number:
                return f"The phone number {self.phone_number} belongs to {c['name']}."
        return "The contact doesn't exist."

class DisplaySchedule:
    def execute(self, phone_book):
        print(f"{'Nome':10}|{' Número':12}")
        for contact in phone_book:
            print(f"{contact['name']:10}| {contact['phone_number']}")

class SearchByInitial:
    def __init__(self, initial):
        self.initial = initial

    def execute(self, phone_book):
        results = []
        for c in phone_book:
            if self.initial  == c["name"][0]:
                results.append(f"{c['name']}: {c['phone_number']}")
        return results if results else "No contacts found with that initial."



