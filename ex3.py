'''Em um frigorífico, cada boi é identificado por um cartão que contém seu número e
seu peso. Faça um programa que leia os números de identificação e o peso de cada
boi e ao final imprima o número de identificação e o peso do boi mais gordo, do boi
mais magro e o total de peso dos bois do frigorífico.'''

def identificacao_boi():
    bois = {}
    count = 1
    
    while True:
        # Lê o número do boi, ou termina o loop se a entrada for vazia
        num_input = input(f"\nInsira o número de identificação do {count}º boi (ou aperte Enter para parar): ")
        if num_input.strip() == "":
            break
        
        # Lê o peso do boi
        peso_input = input(f"Insira o peso do {count}º boi: ")
        try:
            identificacao = int(num_input)
            peso = float(peso_input)

            if identificacao < 0:
                print("\nNúmero de identificação inválido. O número não pode ser negativo. Por favor, insira um número positivo.")
                continue  # Pular para a próxima iteração do loop para permitir nova entrada
            
            elif peso < 0:
                print("\nPeso inválido. Não pode ser negativo. Por favor, insira novamente.")
                continue  # Pular para a próxima iteração do loop para permitir nova entrada
            
            else:
                bois[identificacao] = peso
                count += 1

        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido para o peso.")

    return bois

def calcula_pesos(bois):
    if not bois:
        return None, None, 0  # Caso nenhum boi tenha sido inserido

    total_peso = 0
    boi_mais_gordo = None
    boi_mais_magro = None
    peso_mais_gordo = float('-inf')  # Começa com o menor valor possível
    peso_mais_magro = float('inf')   # Começa com o maior valor possível

    # Loop manual para calcular total de peso, boi mais gordo e mais magro
    for identificacao, peso in bois.items():
        total_peso += peso  # Soma os pesos manualmente

        if peso > peso_mais_gordo:
            boi_mais_gordo = identificacao
            peso_mais_gordo = peso

        if peso < peso_mais_magro:
            boi_mais_magro = identificacao
            peso_mais_magro = peso

    return boi_mais_gordo, peso_mais_gordo, boi_mais_magro, peso_mais_magro, total_peso

def main():
    bois = identificacao_boi()

    if bois:
        boi_mais_gordo, peso_mais_gordo, boi_mais_magro, peso_mais_magro, total_peso = calcula_pesos(bois)

        print("\nResultados:")
        print(f"Boi mais gordo: Número {boi_mais_gordo}, Peso {peso_mais_gordo}")
        print(f"Boi mais magro: Número {boi_mais_magro}, Peso {peso_mais_magro}")
        print(f"Total de peso dos bois: {total_peso}\n")

    else:
        print("\nNenhum boi foi inserido.\n")

main()
