from owner import Owner
from account import Account

def create_owner():
    name = input("\nEnter the owner's name: ")
    age = int(input("Enter the owner's age: "))
    cpf = input("Enter the owner's CPF: ")
    return Owner(name, age, cpf)

def create_account(owner):
    bank_balance = float(input("\nEnter the initial bank balance: "))
    return Account(bank_balance, owner)

def main():
    owner = None
    account = None
    while True:
        print("\nMenu:")
        print("1. Create Owner")
        print("2. Create Account")
        print("3. View Owner Data")
        print("4. View Account Data")
        print("5. Debit")
        print("6. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            owner = create_owner()
            print("Owner created successfully.")
        elif choice == 2:
            if owner:
                account = create_account(owner)
                print("Account created successfully.")
            else:
                print("You need to create an owner first.")
        elif choice == 3:
            if owner:
                owner.view_owner_data()
            else:
                print("No owner created yet.")
        elif choice == 4:
            if account:
                account.view_account_data()
            else:
                print("No account created yet.")
        elif choice == 5:
            if account:
                amount = float(input("Enter the amount to debit: "))
                account.debit(amount)
            else:
                print("No account created yet.")
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please try again.")

main()
