from client import Client
from account import Account

def get_client_data():
    try:
        name = input("\nEnter the name: ")
        cpf = input("Enter the CPF: ")
        phone_number = input("Enter the phone number: ")
        cep = input("Enter the CEP: ")
        return Client(name, cpf, phone_number, cep)
    except Exception as err:
        print(err)
        get_client_data()

def get_account_data(client):
    try:
        bank_balance = float(input("\nEnter the initial balance: "))
        return Account(bank_balance, client)
    except Exception as err:
        print(err)
        get_account_data(client)
    
def main():
    client = get_client_data()
    account = get_account_data(client)

    while True:
        print("\nMenu:")
        print("1. Deposit")
        print("2. Withdraw") # Withdraw = Sacar
        print("3. Show Balance")
        print("4. Show Client Information")
        print("5. Exit")
        option = int(input("Choose an option: "))

        if option == 1:
            amount = float(input("\nEnter the deposit amount: "))
            account.deposit(amount)

        elif option == 2:
            amount = float(input("\nEnter the withdrawal amount: "))
            account.debit(amount)

        elif option == 3:
            print(f"\n${account.get_bank_balance()}")

        elif option == 4:
            print(client)

        elif option == 5:
            print("\nExit program")
            exit()

        else:
            print("Invalid option.")

main()