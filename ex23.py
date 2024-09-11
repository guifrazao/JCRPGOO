'''
23. Em um cinema que possui capacidade de 50 lugares foi distribuído um questionário 
aos expectadores, no qual constava a idade e a sua opinião em relação ao filme, 
segundo: ótimo, bom, regular, ruim ou péssimo. Elabore um programa que, lendo 
estes dados, de diversos espectadores (até o limite de capacidade do cinema) calcule 
e imprima: 
a. A quantidade de respostas ótimo, bom, regular, ruim e péssimo. 
b. A percentagem de ótimo, bom, regular, ruim e péssimo. 
c. A idade do mais velho entrevistado. 
d. A idade do mais novo entrevistado. 
'''

def validar_entrada(msg):
    while True:
        try:
            valor_str = input(msg)
            valor_int = int(valor_str)
            return valor_int
        except ValueError:
            print(46*"=")
            print("ERRO! Informe um inteiro válido.")
            print(46*"=")


def opinioes(capacidade):
    otimo = bom = regular = ruim = pessimo = 0
    idades = []
    for c in range(1, capacidade + 1):
        opiniao = -1
        while opiniao < 1 or opiniao > 5:
            opiniao = validar_entrada("Informe sua opção, com base na tabela acima: ")
            if opiniao >= 1 and opiniao <= 5:
                if opiniao == 1:
                    otimo += 1
                elif opiniao == 2:
                    bom += 1
                elif opiniao == 3:
                    regular += 1
                elif opiniao == 4:
                    ruim += 1
                else:
                    pessimo += 1

                idade = -1
                while idade <= 0:
                    idade = validar_entrada("Informe sua idade: ")
                    if idade > 0: 
                        idades.append(idade)
                        break

    maior_idade = menor_idade = idades[0]

    for c in range(len(idades)):
        if idades[c] < menor_idade:
            menor_idade = idades[c]
        if idades[c] > maior_idade:
            maior_idade = idades[c]

    return otimo, bom, regular, ruim, pessimo, maior_idade, menor_idade 


def main():
    print(f"{'OPÇÕES'}".center(12))
    print('[1] - ÓTIMO\n[2] - BOM\n[3] - REGULAR\n[4] - RUIM\n[5] - PÉSSIMO')
    TOT_ESPECT = 5 # Número total de espectadores na sala de cinema
    resultado = opinioes(TOT_ESPECT) # Tupla que contém os returns

    o, b, re, ru, p, mais_velho, mais_novo = resultado # Cada elemento da tupla é atribuído a uma variável

    print("\nRESULTADO DA PESQUISA")
    print(f"\nÓTIMO -------- {o:>2}({(o/50)*100:.2f}%)"
          f"\nBOM ---------- {b:>2}({(b/50)*100:.2f}%)"
          f"\nREGULAR ------ {re:>2}({(re/50)*100:.2f}%)"
          f"\nRUIM --------- {ru:>2}({(ru/50)*100:.2f}%)"
          f"\nPÉSSIMO ------ {p:>2}({(p/50)*100:.2f}%)\n"
          f"\nIdade da pessoa mais velha = {mais_velho}"
          f"\nIdade da pessoa mais nova = {mais_novo}")

main()