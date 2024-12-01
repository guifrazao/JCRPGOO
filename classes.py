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



