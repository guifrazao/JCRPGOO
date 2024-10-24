from modules import *
def main():
    account = None
    person = None

    while True:
        print("\nMenu:")
        print("1. Create Account")
        print("2. Create Person")
        print("3. Associate Account and Person")
        print("4. Show Account and Person Info")
        print("5. Display Account Balance")
        print("6. Debit Account")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            bank_balance = float(input("Enter the initial bank balance: "))
            account = Account(bank_balance)
            print("Account created successfully.")
        elif choice == '2':
            name = input("Enter the person's name: ")
            person = Person(name)
            print("Person created successfully.")
        elif choice == '3':
            if account and person:
                person.set_account(account)
                account.set_owner(person)
                print("Account and Person associated successfully.")
            else:
                print("You need to create both an account and a person first.")
        elif choice == '4':
            if account and person:
                print("\nAccount Info:")
                account_owner = account.get_owner()
                if account_owner:
                    print(f"Account Owner: {account_owner.get_name()}")
                else:
                    print("No owner associated with the account.")
                print(f"Bank Balance: {account.get_bank_balance()}")

                print("\nPerson Info:")
                person_account = person.get_account()
                if person_account:
                    print(f"Person's Account Balance: {person_account.get_bank_balance()}")
                else:
                    print("No account associated with the person.")
            else:
                print("You need to create and associate both an account and a person first.")
        elif choice == '5':
            if person:
                person.display_balance()
            else:
                print("You need to create and associate both an account and a person first.")
        elif choice == '6':
            if account:
                amount = float(input("Enter the amount to debit: "))
                result = account.debit(amount)
                if result:
                    print(result)
                else:
                    print("Debit successful.")
            else:
                print("You need to create an account first.")
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

main()
