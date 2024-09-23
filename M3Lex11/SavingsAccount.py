class SavingsAccount(object):
    RATE = 0.02 
    
    def __init__(self, name, pin, balance=0.0):
        self.name = name
        self.pin = pin
        self.balance = balance

    def __str__(self):
        result = "Nome: " + self.name + "\n"
        result += "PIN: " + str(self.pin) + "\n"  
        result += "Balance: " + str(self.balance) + "\n"  
        return result
    
    def getBalance(self):
        return self.balance 
    
    def getName(self):
        return self.name
    
    def getPin(self):
        return self.pin
    
    def deposit(self, amount):
        if amount < 0:
            return "Amount must be >= 0"
        self.balance += amount
        return None
    
    def withdraw(self, amount):
        if amount < 0:
            return "Amount must be >= 0"
        elif self.balance < amount:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return None
        
    def computeInterest(self):
        interest = self.balance * SavingsAccount.RATE
        self.deposit(interest)
        return interest

