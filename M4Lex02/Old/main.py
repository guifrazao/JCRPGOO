"""
Escreva uma classe chamada Bicycle que possua campos para a velocidade,
cadência dos pedais (número de rotações dos pedais por minuto), marcha atual e
número de série. A velocidade e a cadência dos pedais não podem ser menores que
zero, a marcha atual deve estar entre 1 e 18 e o número de série deve ser maior que
1000. Crie constantes simbólicas e métodos de acesso e impressão que reflitam
esses limites. Teste a classe implementada e seus métodos. A seguir, crie um método
que calcule a velocidade relativa entre a bicicleta e outra dada como parâmetro. Teste
o seu novo método.
"""

from bicycle import Bicycle
from validatorVel import VelocidadeValidator
from validatorCad import CadenciaValidator
from validatorMarcha import MarchaValidator
from validatorSerie import SerieValidator
from ComparadorVel import VelocidadeComparator


def obter_valor_valido(mensagem, tipo, validadores):
    while True:
        try:
            valor = tipo(input(mensagem))
            for validador in validadores:
                validador.validar(valor)
            return valor
        except ValueError as e:
            print(f"Erro: {e}. Tente novamente.")


def criar_bicicleta():
    velocidade = obter_valor_valido("Digite a velocidade: ", float, [VelocidadeValidator()])
    cadencia = obter_valor_valido("Digite a cadência: ", float, [CadenciaValidator()])
    marcha = obter_valor_valido("Digite a marcha: ", int, [MarchaValidator()])
    serie = obter_valor_valido("Digite o número de série: ", int, [SerieValidator()])

    return Bicycle(velocidade, cadencia, marcha, serie)


def main():
    print("Bicicleta 1:")
    bike1 = criar_bicicleta()
    print("=-" * 30)

    print("\nBicicleta 2:")
    bike2 = criar_bicicleta()
    print("=-" * 30)

    print("\nInformações da Bicicleta 1:")
    print(bike1)
    print("=-" * 30)

    print("\nInformações da Bicicleta 2:")
    print(bike2)
    print("=-" * 30)


    comparador = VelocidadeComparator()
    print(f"\nA diferença de velocidade entre as duas bicicletas é: {comparador.comparar(bike1,bike2):.2f} Km/h")


main()
