"""
O custo de produção de um livro é constituído dos custos por página, mais o custo
de encadernação, além do custo fixo. O custo por página impressa é de R$0,03, o
custo fixo é de R$ 4397,00 e o custo de encadernação depende de cada livro, sendo
utilizada a seguinte tabela:
• Encadernação simples: R$4,30
• Encadernação especial: R$7,80
• Encadernação luxo: R$10,50
Faça um programa que leia para uma lista de livros: o número de páginas, o tipo de
encadernação e o número de vendas previstas (número de cópias) e:
a. Calcule o preço mínimo de cada livro para que cubra os custos de produção e
o preço de venda para que a editora tenha um lucro de 20%.
b. Imprima o total de livros analisados.
c. Imprima o preço médio de venda dos livros (com lucro de 20%).
d. Imprima o preço de venda dos livros mais barato e mais caro.
"""

custo_fixo = 4397.00
paginas = 0.03
custo_encadernacao = {
    1: 4.30,
    2: 7.80,
    3: 10.50
}

def calcular_preço(num_pag,encadernacao,copias_vendidas):
    custo_encad = custo_encadernacao.get(encadernacao,0)
    custo_total = custo_fixo + (num_pag * paginas + custo_encad) * copias_vendidas
    preco_min = custo_total / copias_vendidas
    preco_venda = preco_min * 1.20
    return preco_min,preco_venda

def verificar_inteiro(menssagem):
    while True:
        try:
            valor = int(input(menssagem))
            if valor < 0:
                print("ERROR! o valor inserido é inválido")
            else:
                return valor
        except ValueError:
            print("ERROR FATAL! Insira um valor valído")

def obter_dados_livro():
    print("Para encerrar os lançamentos, digite 0 para o número de páginas")
    print("=-"*30)
    while True:
        num_pag = verificar_inteiro("Digite o número de páginas do livro: ")
        print("---"*30)
        if num_pag == 0:
            break
        else:
            encadernacao = verificar_inteiro("Informe o tipo de encadernação? [1] Simples |  [2] Especial  |  [3] Luxo\n")
            print("---"*30)
            if encadernacao < 1 or encadernacao > 3:
                print("ERROR! Escolha uma opção válida")
            else:
                copias_vendidas = verificar_inteiro("Digite o número de cópias que serão vendidas: ")
                if copias_vendidas == 0:
                    print("ERRO! O número de cópias vendidas não pode ser igual a 0, tente novamente")
                else:
                    print("="*30)
                    yield num_pag,encadernacao,copias_vendidas

def exibir_resultados(total_livros,preco_venda_tot,preco_venda_min,preco_venda_max):
    if total_livros > 0:
        preco_medio = preco_venda_tot / total_livros
    else:
        preco_medio = 0
    
    print(f"Total de livros análisados: {total_livros}")
    print("---"*30)
    print(f"Preço médio de venda dos livros: R${preco_medio:.2f}")
    print("---"*30)
    print(f"Preço de venda do livro mais barato: R${preco_venda_min:.2f}")
    print("---"*30)
    print(f"Preço de venda do livro mais caro: R${preco_venda_max:.2f}")

def main():
    total_livros = preco_venda_tot = 0
    if total_livros == 0:
        preco_venda_max = preco_venda_min = 0
    else:
        preco_venda_max = float("-inf")
        preco_venda_min = float("inf")

    for num_pag,encadernacao,copias_vendidas in obter_dados_livro():
        preco_min,preco_venda = calcular_preço(num_pag,encadernacao,copias_vendidas)

        total_livros += 1
        preco_venda_tot += preco_venda

        if total_livros == 1:
            preco_venda_max = preco_venda_min = preco_venda
        else:
            if preco_venda > preco_venda_max:
                preco_venda_max = preco_venda
            elif preco_venda < preco_venda_min:
                preco_venda_min = preco_venda
            else:
                continue 

    exibir_resultados(total_livros,preco_venda_tot,preco_venda_max,preco_venda_min)

main()
        
