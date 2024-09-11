'''
10. A convenção de graus Fahrenheit para Celsius é obtida pela fórmula C = 5.(F-32)/9. 
Escreva um programa que calcule e imprima uma tabela de graus centígrados em 
função de graus Fahrenheit que variem de 50 a 150 de 5 em 5. Utilize constantes 
simbólicas para indivehicle o início (50) e o fim (150) do intervalo, além do passo (5). 
'''

def converter(graus_f):
    c = 5 * (graus_f - 32) / 9
    return c

def gerar_tabela():
    for fahrenheit in range(50, 150 + 1, 5):
        celcius = converter(fahrenheit)
        print(f"{fahrenheit}\t\t{celcius:.1f}")

def main():
    print("\tGraus Fahrenheit para Celsius\n")
    print("FAHRENHEIT", end='')
    print("\tCELCIUS")
    gerar_tabela()

main()
    


