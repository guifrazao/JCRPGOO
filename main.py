from classes import *

product1 = Product(1, 50.0, "Camiseta")
product2 = Product(2, 120.0, "Calça Jeans")
product3 = Product(3, 30.0, "Tênis")

order = Order()

order.addItem(product1, 2)  
order.addItem(product2, 1)  
order.addItem(product3, 3)

order.finalizePurchase()
