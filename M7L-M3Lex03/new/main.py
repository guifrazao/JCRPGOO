from account import Account
from account_verifications import *

def create_account():
    bank_balance = float(input("Enter the initial bank balance: "))
    account_type = input("Enter account type ('checking' or 'savings'): ").strip().lower()
    if account_type == 'checking':
        verification_policy = CheckingAccountVerification()
    elif account_type == 'savings':
        verification_policy = SavingsAccountVerification()
    else:
        print("Invalid account type. Defaulting to 'checking'.")
        verification_policy = CheckingAccountVerification()
    return Account(bank_balance, verification_policy)

def main():
    account = None

    while True:
        print("\nMenu:")
        print("1. Create Account")
        print("2. Show Bank Balance")
        print("3. Debit")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            account = create_account()
            print("Account created successfully!")
        elif choice == '2':
            if account is not None:
                print(account.get_bank_balance())
            else:
                print("No account created yet.")
        elif choice == '3':
            if account is not None:
                amount = float(input("Enter the amount to debit: "))
                print(account.debit(amount))
            else:
                print("No account created yet.")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

main()