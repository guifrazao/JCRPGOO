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

'''
product1 = Product(1, 10.0, "Caderno")
product2 = Product(2, 5.0, "Caneta")

item1 = ItemOrder(product1, 3)  
item2 = ItemOrder(product2, 2)  

order = Order()
order.addItem(item1)
order.addItem(item2)

print(f"Total do pedido: R$ {order.getTotal():.2f}")
'''


