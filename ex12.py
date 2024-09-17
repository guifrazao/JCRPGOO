#Escreva um programa que leia um número inteiro do teclado e diga se o número lido
#é par ou ímpar.

def definir_parouimpar(numero):
    # Verifica se o número é um inteiro
    if not numero.is_integer():
        return None  # Retorna None para números não inteiros

    # Converte para inteiro para verificar a paridade
    numero = int(numero)
    if numero % 2 == 0:
        return True
    else:
        return False

def main():
    while True:
        try:
            entrada = (input("Insira o número desejado (ou escreva 'sair'): "))
            if entrada.lower() == 'sair':
                print('Programa encerrado')
                break
            else:
                numero = float(entrada)
                resultado = definir_parouimpar(numero)
            if resultado is None:
                print(f"O número {numero} não é um inteiro, portanto não pode ser classificado como par ou ímpar.")
            elif resultado:
                print(f"O número {int(numero)} é par.")
            else:
                print(f"O número {int(numero)} é ímpar.")
        except ValueError:
            print("Por favor, insira um número válido.")

main()

