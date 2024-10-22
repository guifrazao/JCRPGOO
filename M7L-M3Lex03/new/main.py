from account import Account
from account_verifications import CheckingAccountVerification, SavingsAccountVerification

# Conta corrente (permite saldo negativo até -500)
checking_account = Account(1000, CheckingAccountVerification())
print(checking_account.debit(1400))
print(checking_account.get_bank_balance())  

# Conta poupança (não permite saldo negativo)
savings_account = Account(1000, SavingsAccountVerification())
print(savings_account.debit(1100))  
print(savings_account.get_bank_balance()) 