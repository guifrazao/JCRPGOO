from account import Account

account1 = Account("Gustavo", 500)
account2 = Account("Maria", 1000)


print()
print(account1.displayAccount(account1))
print(account1.debit(520))
print(account1.get_bank_balance()) 
print()


print(account2.displayAccount(account2))
print(account2.debit(420))
print(account2.get_bank_balance()) 
print()


# print(help(Account))