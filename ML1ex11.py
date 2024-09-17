
"""
11. O volume de uma esfera pode ser calculado pela fórmula V = 4/3πr³, onde r é o raio da
esfera. Faça um programa que imprima uma tabela de volumes para esferas que
tenham raios entre 0 e 15 cm, de 0.5 em 0.5cm.
"""
from math import pi
def calcular_volume_esfera(raio):
    return 4/3 * pi * raio

#a tabela fica torta a partir de quando o raio é 10
def tabela_volumes():
    raio = 0.0
    print("RAIO          VOLUME")
    for i in range(31):
        volume = calcular_volume_esfera(raio)
        print(f"{raio:.1f}          {volume:.2f}")
        raio += 0.5

def main():
    tabela_volumes()
main()
