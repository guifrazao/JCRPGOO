from M5Lex09 import Invoice

def main():

    while True:
        item_number = input("Informe o número do item (4 a 8 dígitos): ")
        print("--"*30)
        description = input("Informe a descrição do item: ")
        print("--"*30)
        
        try:
            quantity = int(input("Informe a quantidade comprada: "))
            print("--"*30)
            price_per_item = float(input("Informe o preço unitário: R$"))
            invoice = Invoice(item_number=item_number, description=description, quantity=quantity, price_per_item=price_per_item)
            break  
        except ValueError as e:
            print(e)
            print("Por favor, insira informações válidas.")

    print(f"\nItem Number: {invoice.get_item_number()}")
    print()
    print(f"Description: {invoice.get_description()}")
    print("--"*30)
    print(f"Quantity: {invoice.get_quantity()}")
    print("--"*30)
    print(f"Price per Item: R${invoice.get_price_per_item():.2f}")
    print("--"*30)
    print(f"Total Invoice Amount: R${invoice.calculate_total():.2f}")

main()