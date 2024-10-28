"""
Escolha pelo menos 5 exercícios das listas M3L e M5L (5 de cada) para expandir o projeto do
exercício, incluindo novas classes relacionadas, conforme a sua criatividade, demonstrando
a associação bilateral.

Escreva uma classe chamada Bicycle que possua campos para a velocidade,
cadência dos pedais (número de rotações dos pedais por minuto), marcha atual e
número de série. A velocidade e a cadência dos pedais não podem ser menores que
zero, a marcha atual deve estar entre 1 e 18 e o número de série deve ser maior que
1000. Crie constantes simbólicas e métodos de acesso e impressão que reflitam
esses limites. Teste a classe implementada e seus métodos. A seguir, crie um método
que calcule a velocidade relativa entre a bicicleta e outra dada como parâmetro. Teste
o seu novo método.
"""

from Modulos import *

def mostrar_menu():
    print("\n" + "=" * 40)
    print("🚲✨ Bem-vindo ao Sistema de Bicicletas ✨🚲")
    print("=" * 40)
    print("Escolha uma das opções abaixo:")
    print("1️⃣  Criar Bicicleta 1")
    print("2️⃣  Criar Bicicleta 2")
    print("3️⃣  Criar Proprietário")
    print("4️⃣  Associar Bicicleta e Proprietário")
    print("5️⃣  Mostrar Informações da Bicicleta e do Proprietário")
    print("6️⃣  Mostrar Velocidade Relativa entre as Bicicletas")
    print("7️⃣  Subir na Bicicleta")
    print("8️⃣  Sair 🚪")
    print("=" * 40)

def obter_escolha():
    try:
        escolha = int(input("👉 Digite sua escolha (1-8): "))
        if 1 <= escolha <= 8:
            return escolha
        else:
            print("⚠️ Escolha inválida! Por favor, insira um número entre 1 e 8.")
            return None
    except ValueError:
        print("⚠️ Entrada inválida! Por favor, insira um número.")
        return None

def main():
    bicicleta1 = None
    bicicleta2 = None
    proprietario = None

    while True:
        mostrar_menu()
        escolha = obter_escolha()
        
        if escolha == 1:
            velocidade_atual = float(input("🏎️ Digite a velocidade atual da Bicicleta 1 (km/h): "))
            cadencia = float(input("🔄 Digite a cadência da Bicicleta 1 (rpm): "))
            marcha = int(input("⚙️ Digite a marcha da Bicicleta 1: "))
            bicicleta1 = Bicicleta(velocidade_atual, cadencia, marcha)
            print("✅ Bicicleta 1 criada com sucesso.")
        
        elif escolha == 2:
            velocidade_atual = float(input("🏎️ Digite a velocidade atual da Bicicleta 2 (km/h): "))
            cadencia = float(input("🔄 Digite a cadência da Bicicleta 2 (rpm): "))
            marcha = int(input("⚙️ Digite a marcha da Bicicleta 2: "))
            bicicleta2 = Bicicleta(velocidade_atual, cadencia, marcha)
            print("✅ Bicicleta 2 criada com sucesso.")
        
        elif escolha == 3:
            nome = input("👤 Digite o nome do proprietário: ")
            proprietario = Proprietario(nome)
            print("✅ Proprietário criado com sucesso.")
        
        elif escolha == 4:
            if bicicleta1 and proprietario:
                proprietario.definir_bicicleta(bicicleta1)
                bicicleta1.definir_proprietario(proprietario)
                print("🔗 Proprietário e Bicicleta 1 associados com sucesso.")
            else:
                print("⚠️ É necessário criar o proprietário e a bicicleta 1 primeiro.")
        
        elif escolha == 5:
            if bicicleta1 and proprietario:
                print("\n--- 📋 Informações da Bicicleta 1 ---")
                bicicleta_proprietario = bicicleta1.obter_proprietario()
                if bicicleta_proprietario:
                    bicicleta_proprietario.se_apresentar()
                else:
                    print("⚠️ Nenhum proprietário associado à Bicicleta 1.")
                print(f"Velocidade Atual: {bicicleta1.obter_velocidade_atual()} km/h")
                print(f"Cadência: {bicicleta1.obter_cadencia()} rpm")
                print(f"Marcha: {bicicleta1.obter_marcha()}")
            else:
                print("⚠️ É necessário criar e associar uma bicicleta e um proprietário primeiro.")
        
        elif escolha == 6:
            if bicicleta1 and bicicleta2:
                proprietario.mostrar_velocidade_relativa(bicicleta1, bicicleta2)
            else:
                print("⚠️ É necessário criar as duas bicicletas primeiro.")
        
        elif escolha == 7:
            if proprietario and bicicleta1:
                proprietario.subir_na_bicicleta(bicicleta1)
            else:
                print("⚠️ É necessário criar e associar uma bicicleta e um proprietário primeiro.")
        
        elif escolha == 8:
            print("👋 Encerrando o programa. Até logo!")
            break

main()
