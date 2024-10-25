"""
3. Crie uma classe chamada VendingMachine que simule uma máquina de venda de
produtos. Essa classe deve permitir cadastrar produtos, selecionar um produto para
compra, inserir dinheiro, retornar o troco e exibir o estoque disponível.
"""
from vendingmachine import VendingMachine
from product import Product

def main():
    try:
        machine = VendingMachine()
        banana = Product("banana", 7.50, 50)
        pineapple = Product("abacaxi", 12.32, 30)

        machine.addProduct(banana)
        machine.addProduct(pineapple)

        product = input("Type which fruit you would like to purchase: ").lower()
        payment = float(input("Type the amount of money to pay with: $"))
        amount = int(input("Type the amount of fruit to be purchased: "))
        machine.buyProduct(product, payment, amount)
        print(machine.showStock())
        print(machine.getBalance())

    except Exception as err:
        print(f"Error: {err}")