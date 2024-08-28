"""
6. Um dado material radioativo perde metade de sua massa a cada 50s. Dada a massa
inicial em gramas, fazer um algoritmo que determine o tempo necessário para que
essa massa seja menor que 0,5g.
"""

def calcular_tempo_reducao(massa):
    if massa < 0.5:
        return 0
    return 50 + calcular_tempo_reducao(massa/2)

def main():
    tempo = calcular_tempo_reducao(50.0)
    print(f"O objeto demorará {tempo}s para que a massa seja menor que 0,5g")
main()
