class Product:
    def __init__(self, name, price, amount):
        if not self.__verifyName(name):
            raise Exception("Invalid product name")
        if not self.__verifyPrice(price):
            raise Exception("Invalid product price")
        if not self.__verifyAmount(amount):
            raise Exception("Invalid product amount")
    
        self.__name = name
        self.__price = price
        self.__amount = amount

    def __repr__(self):
        return f"\nProduct name: {self.__name}\nPrice: ${self.__price:.2f}\nAmount: {self.__amount}\n"
    
    def getName(self):
        return self.__name    
    
    def setName(self, name):
        if self.__verifyName(name):
            self.__name = name
        else:
            self.__invalidDataMsg("product name")

    def getPrice(self):
        return self.__price   
     
    def setPrice(self, price):
        if self.__verifyPrice(price):
            self.__price = price
        else:
            self.__invalidDataMsg("product price")

    def getAmount(self):
        return self.__amount   
     
    def setAmount(self, amount):
        if self.__verifyAmount(amount):
            self.__amount = amount
        else:
            self.__invalidDataMsg("product amount")
    
    def __invalidDataMsg(self, data):
        print(f"Invalid {data}")

    @staticmethod
    def __verifyName(name):
        return isinstance(name, str) and len(name) >= 3  

    @staticmethod
    def __verifyPrice(price):
        return isinstance(price, float) and price > 0
    
    @staticmethod
    def __verifyAmount(amount):
        return isinstance(amount, int) and amount >= 0
    
