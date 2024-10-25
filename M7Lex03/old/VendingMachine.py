from Product import Product
"""
3. Crie uma classe chamada VendingMachine que simule uma máquina de venda de
produtos. Essa classe deve permitir cadastrar produtos, selecionar um produto para
compra, inserir dinheiro, retornar o troco e exibir o estoque disponível.
"""
class VendingMachine:
    def __init__(self):
        self.__stock = []
        self.__balance = 0.00

    """Adds product to __stock, which is a list of Product objects."""
    def addProduct(self, product):
        self.__stock.append(product)

    """Does the purchase process and informs if the purchase was successful or not"""
    def buyProduct(self, product: Product, payment, amount_purchased):
        self.insertMoney(payment)
        price = product.getPrice()

        if not self.__validadeTransaction(payment, product, amount_purchased):
            raise Exception(self.__invalidTransactionMsg())

        product.setAmount(product.getAmount()-amount_purchased)
        change = self.__returnChange(payment, price*amount_purchased)
        self.__purchaseSuccessfulMsg(product, change)

    """Selects the product by its name, returns the product in case __checkStock() says the product is in stock"""
    def selectProduct(self, name):
        product = self.__getProductByName(name)
        if not self.__checkStock(product):
            raise Exception(self.__productNotInStockMsg())
        return product

    """Concats all products in stock to a string and returns said string"""
    def showStock(self):
        products = ""
        for product in self.__stock:
            products += f"{product}"
        return products

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
    
    def getStock(self):
        return self.__stock
    
    def getBalance(self):
        return self.__balance
    
    def setBalance(self, balance):
        if self.__verifyBalance(balance):
            self.__balance = balance

    @staticmethod
    def __checkStock(product):
        return product is not None or product.getAmount() > 0
              
    """Checks if the amount paid by the user is enough to afford the purchase and if theres enough products in stock"""
    @staticmethod
    def __validadeTransaction(payment, product, amount_purchased):
        return payment >= product.getPrice()*amount_purchased and product.getAmount()-amount_purchased >= 0

    @staticmethod
    def __purchaseSuccessfulMsg(product, change):
        print(f"Purchase of product {product.getName()} successful, change: ${change:.2f}")

    @staticmethod
    def __invalidTransactionMsg():
        return "Invalid transaction"

    @staticmethod
    def __productNotInStockMsg():
        return "This product is not in stock"

    @staticmethod
    def __verifyBalance(balance):
        return balance >= 0
