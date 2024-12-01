'''
2. Implemente as classes descritas no diagrama abaixo, considerando que:
a. Um pedido é composto por um conjunto de itens pedidos.
b. Um item pedido associa-se com um produto.
c. O cálculo do valor total do pedido deverá ser feito mediante a soma do preço de
cada produto incluído nos itens pedidos.
'''

class Product:
    def __init__(self, code: int, value: float, description: str):
        self.code = code
        self.value = value
        self.description = description

class ItemOrder:
    def __init__(self, product: Product, quantity: int):
        self.product = product # agregação
        self.quantity = quantity
    
    def itemInformation(self):
        print(f"Produto {self.product.code}: {self.product.description}, Quantidade: {self.quantity}, Total: {self.product.value * self.quantity:.2f}")

class Order:
    def __init__(self):
        self.__total = 0.0
        self.__items = [] # composição

    def addItem(self, product: Product, quantity: int):
        item = ItemOrder(product, quantity) 
        self.__items.append(item)

    def getTotal(self):
        self.__total = sum(item.product.value * item.quantity for item in self.__items)
        return self.__total

    def finalizePurchase(self):
        print("Compra finalizada.")
        print(f"Total a pagar: {self.getTotal():.2f}")
        for item in self.__items:
            item.itemInformation()
