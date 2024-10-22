class Account:
    def __init__(self, bank_balance, verification_policy: any):
        self.__bank_balance = bank_balance
        self.__verification_policy = verification_policy

    def debit(self, amount):
        if self.__verification_policy.verify(self.__bank_balance, amount):
            self.__bank_balance -= amount
            return "Withdrawal successful."
        return "Debit amount exceeds account balance."

    def get_bank_balance(self):
        return "The account balance is R$" + str(self.__bank_balance)