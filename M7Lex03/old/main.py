"""
3. Crie uma classe chamada VendingMachine que simule uma máquina de venda de
produtos. Essa classe deve permitir cadastrar produtos, selecionar um produto para
compra, inserir dinheiro, retornar o troco e exibir o estoque disponível.
"""
from VendingMachine import VendingMachine
from Product import Product


def main():
    machine = VendingMachine()
    selected_product = None
    while True:
        print("[1] - Add product\n[2] - Select product\n[3] - Buy product\n[4] - Show stock\n[5] - Exit")
        option = 0
        try:
            while option < 1 or option > 5:
                option = int(input())

            if option == 1:
                name = input("Name: ")
                price = float(input("Price: $"))
                amount = int(input("Amount: "))
                machine.addProduct(Product(name, price, amount))

            elif option == 2:
                selected_product = machine.selectProduct(input("Enter the product's name: "))
                print(f"{selected_product.getName()} selected")

            elif option == 3:
                if selected_product is None:
                    raise Exception("No product selected")
                payment = float(input("Insert money: $"))
                amount = int(input("Enter the amount to be purchased: "))
                machine.buyProduct(selected_product, payment, amount)

            elif option == 4:
                print(machine.showStock())
      
            else:
                print("EXITING")
                break
              
        except Exception as err:
            print(err)

main()
    



        
        

        

