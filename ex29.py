"""
Escreva uma função (FparaC) que receba uma temperatura em graus F e retorne a
temperatura em graus C, sendo:
C = 5/9 (F - 32).
A seguir, faça um programa que, em loop, leia um valor para F da entrada padrão e o imprima o valor de C correspondente,
utilizando a função FparaC.
"""

def calcular_conversaoFparaC(graus):
    return 5/9 * (graus - 32)

def verificar_float(mensagem):
    while True:
        try:    
            graus = float(input((mensagem)))
            return graus
        except ValueError:
            print("Entrada INVÁLIDA! Digite a informação CORRETAMENTE!")

def receber_entrada():
    print("""
=================================================
CONVERSOR DE TEMPERATURA FAHRENHEIT para CELSIUS
=================================================
""")
    while True:
        graus = verificar_float("""Digite um valor em Graus Fahrenheit para a conversão: """)
        print("="*90)
        conversao = calcular_conversaoFparaC(graus)
        print(f"{graus}° Fahrenheit em graus Celsius é {conversao:.2f}° C \n")

        while True:
            escolha = str(input("Deseja continuar? [S/N]: ")).strip().upper()
            if escolha in ["S","N"]:
                break
            else:
                print("Entrada inválida! Por favor, digite 'S' para Sim ou 'N' para Não.")
            
        if escolha == "N":
            print("Saindo...")
            break

def main():
    receber_entrada()

main()