class Person:
    def __init__(self, name):
        self.__name = name
        self.__account = None

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_account(self):
        return self.__account

    def set_account(self, account:any):
        self.__account = account

    def display_balance(self):
        if self.__account:
            print(self.__account.get_bank_balance())
        else:
            print("No account associated with this person.")
