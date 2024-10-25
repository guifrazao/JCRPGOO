class Product:
    def __init__(self, name, price, amount):
        if not self.__verifyData(name, price, amount):
            raise Exception(self.__invalidDataMsg())
        else:
            self.__name = name
            self.__price = price
            self.__amount = amount

    def __repr__(self):
        return f"\nProduct name: {self.__name}\nPrice: ${self.__price:.2f}\nAmount: {self.__amount}\n"
    
    def getName(self):
        return self.__name    
    
    def setName(self, name):
        self.__name = name

    def getPrice(self):
        return self.__price   
     
    def setPrice(self, price):
        self.__price = price

    def getAmount(self):
        return self.__amount   
     
    def setAmount(self, amount):
        self.__amount = amount
    
    def __invalidDataMsg(self):
        return "Invalid data"

    @staticmethod
    def __verifyData(name, price, amount):
        return isinstance(name, str) and len(name) >= 3 and isinstance(price, float) and price > 0 and isinstance(amount, int) and amount >= 0
    