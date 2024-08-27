"""
11. O volume de uma esfera é dado pela expressão V(r) = 4/3πr³. 
Faça um programa que leia do teclado o valor do raio e calcule o volume da esfera correspondente.
"""

from math import pi
def calcular_volume(r):
    return 4/3 * pi * pow(r, 3)

def main():
    try:
        raio = float(input("Digite o raio: "))
        print(f"Volume da esfera = {calcular_volume(raio)} u³")
    except Exception as e:
        print(f"Erro fatal: {e}")
main()
