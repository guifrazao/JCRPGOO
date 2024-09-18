
"""
11. O volume de uma esfera pode ser calculado pela fórmula V = 4/3πr³, onde r é o raio da
esfera. Faça um programa que imprima uma tabela de volumes para esferas que
tenham raios entre 0 e 15 cm, de 0.5 em 0.5cm.
"""
from ex33 import calcular_pi
def calcular_volume_esfera(raio):
    pi = calcular_pi(1000)
    return 4/3 * pi * pow(raio, 3)

#a tabela fica torta a partir de quando o raio é 10
def tabela_volumes():
    raio = 0.0
    print("RAIO\t\tVOLUME")
    for i in range(30+1):
        volume = calcular_volume_esfera(raio)
        print(f"{raio:.1f}\t\t{volume:.2f}")
        raio += 0.5

def main():
    tabela_volumes()
main()
