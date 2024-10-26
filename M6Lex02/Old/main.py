from owner import Owner
from bicycle import Bicycle
from validator import Validator_Bicycle, Validator_Owner

def obter_valor_valido(mensagem, tipo, validacao_func):
    while True:
        try:
            valor = tipo(input(mensagem))
            validacao_func(valor)
            return valor
        except ValueError as e:
            print(f"Erro: {e}. Tente novamente.")
        except Exception as err:
            print(f"Erro: {err}. Tente novamente.")

def criar_proprietario(validator_owner):
    while True:
        try:
            nome_proprietario = obter_valor_valido("Digite o nome do proprietário: ", str, validator_owner.verifyName)
            print("--" * 30)
            cpf_proprietario = obter_valor_valido("Digite o CPF do proprietário: ", str, validator_owner.verifyCPF)
            print("=-" * 30)
            return Owner(nome_proprietario, cpf_proprietario)
        except Exception as err:
            print(f"Erro: {err}. Tente novamente.")
            print("--" * 30)

def criar_bicicleta(validator_bike, validator_owner):
    owner = criar_proprietario(validator_owner)
    while True:
        try:
            velocidade = obter_valor_valido("Digite a velocidade (km/h): ", float, validator_bike.verifyVelocidade)
            cadencia = obter_valor_valido("Digite a cadência (rpm): ", float, validator_bike.verifyCadencia)
            marcha = obter_valor_valido("Digite a marcha (1-18): ", int, validator_bike.verifyMarcha)
            serie = obter_valor_valido("Digite o número de série: ", int, validator_bike.verifyNumeroSerie)
            return Bicycle(velocidade, cadencia, marcha, serie, owner)
        except Exception as err:
            print(f"Erro: {err}. Tente novamente.")

def main():
    validator_bike = Validator_Bicycle()
    validator_owner = Validator_Owner()
    print("Bicicleta 1:")
    bike1 = criar_bicicleta(validator_bike, validator_owner)
    print("=-" * 30)
    print("\nBicicleta 2:")
    bike2 = criar_bicicleta(validator_bike, validator_owner)
    print("=-" * 30)
    print("\nInformações da Bicicleta 1:")
    print(bike1)
    print("=-" * 30)
    print("\nInformações da Bicicleta 2:")
    print(bike2)
    print("=-" * 30)
    velocidade_relativa = bike1.velocidade_relativa(bike2)
    print(f"\nA diferença de velocidade entre as duas bicicletas é: {velocidade_relativa:.2f} Km/h")

main()