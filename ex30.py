# Desejamos calcular, a partir do sexo e da altura, o peso ideal de uma pessoa. Para
# isto, devemos saber que existem duas fórmulas para o peso ideal, que são:
# • Homens: (72,7 * altura) - 58
# • Mulheres: (62,1 * altura) - 44,7
# Para que uma pessoa seja considerada obesa, a diferença entre o seu peso e o peso
# ideal deve ser superior à 40 Kg. Elabore um programa que leia o sexo, o peso e a
# altura de uma pessoa, imprima o peso ideal e informe se a pessoa está abaixo do
# peso ideal, acima do peso ideal ou obesa.

def calcular_peso_ideal(sexo, altura):
    if sexo.lower() == 'homem':
        return (72.7 * altura) - 58
    elif sexo.lower() == 'mulher':
        return (62.1 * altura) - 44.7
    else:
        return None

def classificar_peso(peso_atual, peso_ideal):
    diferenca = peso_atual - peso_ideal
    if diferenca > 40:
        return "obeso/obesa, procure ajuda médica"
    elif diferenca > 2:
        return "acima do peso ideal"
    elif diferenca > 0:
        return "perto do peso ideal"
    else:
        return "abaixo do peso ideal"

def main():
    sexo = input("Informe o sexo (homem/mulher): ").strip().lower()
    altura = float(input("Informe a altura em metros: "))
    peso_atual = float(input("Informe o peso atual em kg: "))

    peso_ideal = calcular_peso_ideal(sexo, altura)

    if peso_ideal is not None:
        classificacao = classificar_peso(peso_atual, peso_ideal)
        print(f"O peso ideal é: {peso_ideal:.2f} kg.")
        print(f"Você está {classificacao}.")
    else:
        print("Sexo inválido. Por favor, informe 'homem' ou 'mulher'.")

main()
