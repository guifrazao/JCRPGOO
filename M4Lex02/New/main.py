"""
Refazer as listas M3L e M5L, aplicando o Princípio Aberto-Fechado e mostrar as diferenças
de seu código, antes e depois.

Escreva uma classe chamada Bicycle que possua campos para a velocidade,
cadência dos pedais (número de rotações dos pedais por minuto), marcha atual e
número de série. A velocidade e a cadência dos pedais não podem ser menores que
zero, a marcha atual deve estar entre 1 e 18 e o número de série deve ser maior que
1000. Crie constantes simbólicas e métodos de acesso e impressão que reflitam
esses limites. Teste a classe implementada e seus métodos. A seguir, crie um método
que calcule a velocidade relativa entre a bicicleta e outra dada como parâmetro. Teste
o seu novo método.
"""

from Bicycle import Bicycle

def get_bicycle_data():
    while True:
        try:
            velocidade = float(input("Digite a velocidade da bicicleta (km/h): "))
            print("--"*30)
            cadencia = float(input("Digite a cadência da bicicleta (rotações por minuto): "))
            print("--"*30)
            marcha = int(input("Digite a marcha atual da bicicleta (entre 1 e 18): "))
            print("--"*30)
            serie = int(input("Digite o número de série da bicicleta (deve ser maior que 1000): "))
            print("--"*30)
            
            bike = Bicycle(0, 0, 1, 1000)
            
            bike.set_velocidade(velocidade)
            bike.set_cadencia(cadencia)
            bike.set_marcha(marcha)
            bike.set_serie(serie)
            
            return bike

        except ValueError as e:
            print(f"Erro: {e}. Por favor, tente novamente.")

print("Bicicleta 1:")
bike1 = get_bicycle_data()
print("=-"*30)

print("\nBicicleta 2:")
bike2 = get_bicycle_data()
print("=-"*30)

print("\nInformações da Bicicleta 1:")
print(bike1)
print("=-"*30)

print("\nInformações da Bicicleta 2:")
print(bike2)
print("=-"*30)

print(f"\nVelocidade relativa entre as bicicletas: {bike1.velocidade_relativa(bike2)} km/h")
