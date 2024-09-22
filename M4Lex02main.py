from M4Lex02 import Bicycle,BicycleValidator



def obter_valor_valido(mensagem, tipo, validacao_func):
    while True:
        try:
            valor = tipo(input(mensagem))
            validacao_func(valor) 
            return valor
        except ValueError as e:
            print(f"Erro: {e}. Tente novamente.")

def criar_bicicleta(validator):

    velocidade = obter_valor_valido("Digite a velocidade: ", float, validator.validar_velocidade)
    cadencia = obter_valor_valido("Digite a cadência: ", float, validator.validar_cadencia)
    marcha = obter_valor_valido("Digite a marcha: ", int, validator.validar_marcha)
    serie = obter_valor_valido("Digite o número de série: ", int, validator.validar_serie)


    return Bicycle(velocidade, cadencia, marcha, serie)

def main():

    validator = BicycleValidator()

    print("Bicicleta 1:")
    bike1 = criar_bicicleta(validator)
    print("=-"*30)

    print("\nBicicleta 2:")
    bike2 = criar_bicicleta(validator)
    print("=-"*30)

    print("\nInformações da Bicicleta 1:")
    print(bike1)
    print("=-"*30)

    print("\nInformações da Bicicleta 2:")
    print(bike2)
    print("=-"*30)


    velocidade_relativa = bike1.velocidade_relativa(bike2)
    print(f"\nA diferença de velocidade entre as duas bicicletas é: {velocidade_relativa:.2f} Km/h")

main()

