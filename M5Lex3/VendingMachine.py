
class VendingMachine:
    def __init__(self):
        self.__stock = []
        self.__balance = 0.00

    """Adds product to __stock, which is a list of Product objects."""
    def addProduct(self, product):
        self.__stock.append(product)

    """Does the purchase process and informs if the purchase was successful or not"""
    def buyProduct(self, name, payment, amount_purchased):
        self.insertMoney(payment)
        product = self.selectProduct(name)
        price = product.getPrice()

        if not self.__validadeTransaction(payment, product, amount_purchased):
            self.__invalidTransactionMsg()
            exit()

        product.setAmount(product.getAmount()-amount_purchased)
        change = self.__returnChange(payment, price*amount_purchased)
        print(f"Purchase of product {product.getName()} successful, change: ${change:.2f}")

    """Selects the product by its name, returns the product in case __checkStock() says the product is in stock"""
    def selectProduct(self, name):
        product = self.__getProductByName(name)
        if not self.__checkStock(product):
            self.__productNotInStockMsg()
            exit()
        return product

    """Concats all products in stock to a string and returns said string"""
    def showStock(self):
        str = ""
        for product in self.__stock:
            str += f"{product}"
        return str

    def insertMoney(self, payment):
        self.setBalance(self.__balance + payment)

    def __returnChange(self, payment, price):
        change = payment - price
        self.setBalance(self.__balance - change)
        return change

    """Searches the entire stock for the product with the informed name"""
    def __getProductByName(self, name):
        for product in self.__stock:
            if product.getName() == name:
                return product
        return None
    
    def __checkStock(self, product):
        return product is not None or product.getAmount() > 0
              
    """Checks if the amount paid by the user is enough to afford the purchase and if theres enough products in stock"""
    def __validadeTransaction(self, payment, product, amount_purchased):
        return payment >= product.getPrice()*amount_purchased and product.getAmount()-amount_purchased >= 0

    def __invalidTransactionMsg(self):
        print("Invalid transaction")

    def __productNotInStockMsg(self):
        print("This product is not in stock")


    def getStock(self):
        return self.__stock
    def getBalance(self):
        return self.__balance
    def setBalance(self, balance):
        self.__balance = balance
        
