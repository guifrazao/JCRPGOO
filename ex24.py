"""
Para fazer uma pesquisa sobre o consumo de energia elétrica de uma cidade, são
fornecidos os seguintes dados:
• O preço o kWh
• O número de identificação de cada consumidor
• A quantidade de kWh consumido no mês por cada um
• O código do tipo de consumidor (residencial, comercial ou industrial)
A partir desses dados calcule:
a. Para cada consumidor, o total a pagar;
b. O maior consumo verificado;
c. O menor consumo verificado
d. O total de consumo (em kWh) para cada um dos três tipos de consumidores
e. A média de consumo (em kWh) para cada um dos três tipos de consumidores
f. O total arrecadado pela companhia elétrica.
"""

def verificar_float(mensagem, permitir_zero=False):
    while True:
        try:
            valor = float(input(mensagem))
            if valor >= 0 and (permitir_zero or valor > 0):
                return valor
            else:
                print("Valor inválido! Digite um número positivo.")
        except ValueError:
            print("ERROR FATAL! Insira um valor numérico válido.")

def obter_dados_consumidor():
    consumidores = []

    while True:
        print("\nPara encerrar a entrada de dados, digite 0 no ID do consumidor.")
        id_consumidor = verificar_float("Digite o número de identificação do consumidor: ", permitir_zero=True)
        if id_consumidor == 0:
            break

        consumo = verificar_float("Digite a quantidade de kWh consumida no mês: ")
        tipo = input("Digite o código do tipo de consumidor (R-residencial, C-comercial, I-industrial): ").upper()

        if tipo not in ['R', 'C', 'I']:
            print("Código de consumidor inválido. Tente novamente.")
            continue

        consumidores.append({'id': id_consumidor, 'consumo': consumo, 'tipo': tipo})

    return consumidores

def calcular_totais(consumidores, preco_kwh):
    if not consumidores:  # Verifica se a lista está vazia
        return {
            'total_arrecadado': 0,
            'maior_consumo': 0,
            'menor_consumo': 0,
            'consumo_por_tipo': {'R': 0, 'C': 0, 'I': 0},
            'contadores_tipo': {'R': 0, 'C': 0, 'I': 0}
        }
    
    TOTAL_ARRECADADO = 0
    
    # Inicializa maior e menor consumo com o valor do primeiro consumidor
    maior_consumo = consumidores[0]['consumo']
    menor_consumo = consumidores[0]['consumo']
    
    consumo_por_tipo = {'R': 0, 'C': 0, 'I': 0}
    contadores_tipo = {'R': 0, 'C': 0, 'I': 0}

    for consumidor in consumidores:
        total_a_pagar = calcular_total_a_pagar(preco_kwh, consumidor['consumo'])
        total_arrecadado += total_a_pagar

        # Atualiza maior e menor consumo
        if consumidor['consumo'] > maior_consumo:
            maior_consumo = consumidor['consumo']
        if consumidor['consumo'] < menor_consumo:
            menor_consumo = consumidor['consumo']

        # Acumula o consumo por tipo de consumidor
        consumo_por_tipo[consumidor['tipo']] += consumidor['consumo']
        contadores_tipo[consumidor['tipo']] += 1

    return {
        'total_arrecadado': total_arrecadado,
        'maior_consumo': maior_consumo,
        'menor_consumo': menor_consumo,
        'consumo_por_tipo': consumo_por_tipo,
        'contadores_tipo': contadores_tipo
    }


def calcular_total_a_pagar(preco_kwh, consumo):
    return preco_kwh * consumo

def exibir_resultados(preco_kwh, consumidores):
    if not consumidores:
        print("\nNenhum consumidor foi registrado. Não há dados para exibir.")
        return
    
    totais = calcular_totais(consumidores, preco_kwh)
    
    print("\n--- Detalhes de Consumo por Consumidor ---")
    for consumidor in consumidores:
        total_a_pagar = calcular_total_a_pagar(preco_kwh, consumidor['consumo'])
        print(f"\nID do consumidor: {consumidor['id']}")
        print(f"Consumo: {consumidor['consumo']} kWh")
        print(f"Total a pagar: R$ {total_a_pagar:.2f}")

    print("\n--- Resultados Gerais ---")
    print(f"Maior consumo verificado: {totais['maior_consumo']} kWh")
    print(f"Menor consumo verificado: {totais['menor_consumo']} kWh")
    print(f"Total de consumo Residencial: {totais['consumo_por_tipo']['R']} kWh")
    print(f"Total de consumo Comercial: {totais['consumo_por_tipo']['C']} kWh")
    print(f"Total de consumo Industrial: {totais['consumo_por_tipo']['I']} kWh")

    media_residencial = totais['consumo_por_tipo']['R'] / totais['contadores_tipo']['R'] if totais['contadores_tipo']['R'] > 0 else 0
    media_comercial = totais['consumo_por_tipo']['C'] / totais['contadores_tipo']['C'] if totais['contadores_tipo']['C'] > 0 else 0
    media_industrial = totais['consumo_por_tipo']['I'] / totais['contadores_tipo']['I'] if totais['contadores_tipo']['I'] > 0 else 0

    print(f"Média de consumo Residencial: {media_residencial:.2f} kWh")
    print(f"Média de consumo Comercial: {media_comercial:.2f} kWh")
    print(f"Média de consumo Industrial: {media_industrial:.2f} kWh")
    print(f"Total arrecadado pela companhia elétrica: R$ {totais['total_arrecadado']:.2f}")

def main():
    preco_kwh = verificar_float("Digite o preço do kWh: ")
    consumidores = obter_dados_consumidor()
    exibir_resultados(preco_kwh, consumidores)

main()
