'''Para fazer o balanço mensal de um armazém, faça um programa que que leia para um
número qualquer de mercadorias diferentes o preço de custo, o preço de venda e a
quantidade vendida. A partir desses dados imprima: o número total de mercadorias
diferentes lidas, o faturamento total e o lucro total do armazém.'''

def dados():
    mercadorias = {}
    count = 1
    
    while True:
        
        custo_input = input(f"\nInsira o preço de custo do {count}º item (ou aperte Enter para parar): ")
        if custo_input.strip() == "":
            break
       
        venda_input = input(f"Insira o preço de venda do {count}º item: ")

        num_input = input(f"Insira a quantidade de vendas do {count}º item: ")


        try:
            preco_custo = float(custo_input)
            preco_venda = float(venda_input)
            num_vendas = int(num_input)

            if preco_custo < 0 or preco_venda < 0 or num_vendas < 0:
                print("Valores não podem ser negativos. Por favor, insira valores válidos.")
                continue

            faturamento = preco_venda * num_vendas
            lucro = faturamento - (preco_custo * num_vendas)

                
            mercadorias[f"Item {count}"] = {
               "Preço de Custo": preco_custo, 
                "Preço de Venda": preco_venda, 
                "Quantidade": num_vendas, 
                "Faturamento": faturamento, 
                "Lucro": lucro }
            
            count += 1

        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

    return mercadorias

def Faturamento_lucro(mercadorias):
    
    total_faturamento = sum(atributos["Faturamento"] for atributos in mercadorias.values())
    total_lucro = sum(atributos["Lucro"] for atributos in mercadorias.values())
    total_quantidade = sum(atributos["Quantidade"] for atributos in mercadorias.values())

    return total_faturamento, total_lucro, total_quantidade

def main():

    mercadorias = dados()
    total_faturamento, total_lucro, total_quantidade = Faturamento_lucro(mercadorias)

    print(f"\nMercadorias")
    print(f"Foram lidas {len(mercadorias)} mercadorias")
    print(f"\nMercadorias Vendidas")
    print(f"Foram vendidas {total_quantidade} mercadorias")
    print(f"\nFATURAMENTO TOTAL")
    print(f"O faturamento total do Armazém é de R${total_faturamento:.2f}")
    print(f"\nLUCRO TOTAL")
    print(f"O lucro total do Armazém é de R${total_lucro:.2f}\n")

main()

  

