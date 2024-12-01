from classes import *

product1 = Product(1, 10.0, "Caderno")
product2 = Product(2, 5.0, "Caneta")

item1 = ItemOrder(product1, 3)  
item2 = ItemOrder(product2, 2)  

order = Order()
order.addItem(item1)
order.addItem(item2)

print(f"Total do pedido: R$ {order.getTotal():.2f}")