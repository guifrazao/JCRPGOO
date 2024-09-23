"""
Crie uma classe chamada Invoice que possa ser utilizado por uma loja de
suprimentos de informática para representar uma fatura de um item vendido na loja.
Uma fatura deve incluir as seguintes informações como atributos:
• o número do item faturado,
• a descrição do item,
• a quantidade comprada do item e
• o preço unitário do item.
Sua classe deve ter um construtor que inicialize os quatro atributos. Se a quantidade
não for positiva, ela deve ser configurada como 0. Se o preço por item não for
positivo ele deve ser configurado como 0.0. Forneça um método set e um método get
para cada variável de instância. Além disso, forneça um método chamado que calcula
o valor da fatura (isso é, multiplica a quantidade pelo preço por item) e depois retorna
o valor real. Escreva um aplicativo de teste que demonstra as capacidades da classe
Invoice.
""" 

from Invoice import Invoice

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