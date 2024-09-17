'''Faça um programa que leia um conjunto de números positivos, sendo o conjunto
destes números finalizado quando for digitado um número negativo. Ao final, imprima
o maior e o menor número lido e a média deles.'''

count = 1
soma = 0
maior_num = None
menor_num = None
qtd_numeros = 0

while True:
    try:
        num = float(input(f"\nInsira o número {count} (digite um número negativo para parar): "))
        
        if num < 0:
            break
        
        # Atualiza a soma
        soma += num
        
        # Atualiza o maior número
        if maior_num is None or num > maior_num:
            maior_num = num
        
        # Atualiza o menor número
        if menor_num is None or num < menor_num:
            menor_num = num
        
        # Incrementa o contador de números válidos
        qtd_numeros += 1
        count += 1
    
    except ValueError:
        print("\nEntrada inválida, digite novamente.\n")

if qtd_numeros > 0:
    media = soma / qtd_numeros

    print("\nResultados:")
    print(f"O maior número do conjunto é: {maior_num}")
    print(f"O menor número do conjunto é: {menor_num}")
    print(f"A média dos números do conjunto é: {media}\n")
else:
    print("\nNenhum número positivo foi inserido.\n")






