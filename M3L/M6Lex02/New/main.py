from owner import Owner
from bicycle import Bicycle
from validator import Validator_Bicycle, Validator_Owner, Validator_Roda
from roda import Roda

def obter_valor_valido(mensagem, tipo, validacao_func):
    while True:
        try:
            valor = tipo(input(mensagem))
            if validacao_func(valor):
                return valor
            else:
                raise ValueError("Valor inválido.")
        except ValueError as e:
            print(f"Erro: {e}. Tente novamente.\n")

def criar_proprietario():
    print("\n--- Cadastro de Proprietário ---")
    nome = obter_valor_valido("Digite o nome do proprietário: ", str, Validator_Owner.verifyName)
    cpf = obter_valor_valido("Digite o CPF do proprietário (somente números): ", str, Validator_Owner.verifyCPF)
    return Owner(nome, cpf)

def criar_roda():
    print("\n--- Cadastro de Roda ---")
    tamanho = obter_valor_valido("Digite o tamanho da roda (em cm): ", float, Validator_Roda.verifyTamanho)
    pressao = obter_valor_valido("Digite a pressão da roda (em PSI): ", float, Validator_Roda.verifyPressao)
    return Roda(tamanho, pressao)

def criar_bicicleta():
    print("\n--- Cadastro de Bicicleta ---")
    owner = criar_proprietario()
    print("\n--- Informações da bicicleta ---")
    velocidade = obter_valor_valido("Digite a velocidade (km/h): ", float, Validator_Bicycle.verifyVelocidade)
    cadencia = obter_valor_valido("Digite a cadência (rpm): ", float, Validator_Bicycle.verifyCadencia)
    marcha = obter_valor_valido("Digite a marcha (1-18): ", int, Validator_Bicycle.verifyMarcha)
    serie = obter_valor_valido("Digite o número de série: ", int, Validator_Bicycle.verifyNumeroSerie)
    rodas = [criar_roda() for _ in range(2)]
    return Bicycle(velocidade, cadencia, marcha, serie, owner, rodas)

def exibir_menu():
    print("""
==================================
        Sistema de Bicicletas      
==================================
Escolha uma das opções abaixo:
1 - Cadastrar nova bicicleta
2 - Mostrar informações das bicicletas
3 - Calcular velocidade relativa entre duas bicicletas
4 - Sair
==================================
""")

def main():
    bicicleta1 = None
    bicicleta2 = None

    while True:
        exibir_menu()
        opcao = input("Digite o número da opção desejada: ")
        
        if opcao == "1":
            if bicicleta1 is None:
                bicicleta1 = criar_bicicleta()
                print("✅ Bicicleta 1 cadastrada com sucesso!\n")
            else:
                bicicleta2 = criar_bicicleta()
                print("✅ Bicicleta 2 cadastrada com sucesso!\n")
        
        elif opcao == "2":
            if bicicleta1:
                print("\n--- Informações da Bicicleta 1 ---")
                print()
                print(bicicleta1)
            else:
                print("\n❌ Bicicleta 1 não cadastrada.\n")
                
            if bicicleta2:
                print("\n--- Informações da Bicicleta 2 ---")
                print()
                print(bicicleta2)
            else:
                print("\n❌ Bicicleta 2 não cadastrada.\n")
        
        elif opcao == "3":
            if bicicleta1 and bicicleta2:
                velocidade_relativa = bicicleta1.velocidade_relativa(bicicleta2)
                print(f"\nA diferença de velocidade entre as duas bicicletas é de: {velocidade_relativa:.2f} km/h\n")
            else:
                print("\nAmbas as bicicletas precisam estar cadastradas para calcular a velocidade relativa.\n")
        
        elif opcao == "4":
            print("\nSaindo do sistema. Até mais!")
            break
        else:
            print("\nOpção inválida. Por favor, selecione um número entre 1 e 4.\n")

main()
