from account import Account

account = Account(500)
print(account.get_bank_balance()) 
print(account.debit(501))
print(account.get_bank_balance()) 

print(help(Account))