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
