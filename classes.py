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
        self.product = product
        self.quantity = quantity

class Order:
    def __init__(self):
        self.__total = 0.0
        self.__items = []
    
    def addItem(self, item: ItemOrder):
        self.__items.append(item)
    
    def getTotal(self):
        self.__total = sum(item.product.value * item.quantity for item in self.__items)
        return self.__total



