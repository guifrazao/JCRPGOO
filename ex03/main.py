from tickets import *

def menu():
    option = -1
    while option < 0 or option > 9:
        print("\n1 - Criar Ingresso Normal\n" +
              "2 - Criar Ingresso VIP\n" +
              "3 - Criar LowerStateroom\n" +
              "4 - Criar SuperiorStateroom\n" +
              "5 - Exibir valor do ingresso Normal\n" +
              "6 - Exibir valor do ingresso VIP\n" +
              "7 - Exibir valor do LowerStateroom\n" +
              "8 - Exibir valor do SuperiorStateroom\n" +
              "9 - Obter localização do LowerStateroom\n" +
              "0 - Sair\n")
        option = int(input("Digite sua opção: "))
        if option < 0 or option > 9:
            print("\tOpção inválida! Digite novamente.")
    return option

def main():
    ingresso_normal = None
    ingresso_vip = None
    lower_stateroom = None
    superior_stateroom = None

    choice = 100

    while choice != 0:
        choice = menu()

        if choice == 0:
            print("Encerrando...\n")
            break

        elif choice == 1:
            valor = float(input("Digite o valor do ingresso Normal: "))
            ingresso_normal = Normal(valor)
            print("Ingresso Normal criado.\n")

        elif choice == 2:
            valor = float(input("Digite o valor do ingresso Normal: "))
            valor_adicional = float(input("Digite o valor adicional do ingresso VIP: "))
            ingresso_vip = VIP(valor, valor_adicional)
            print("Ingresso VIP criado.\n")

        elif choice == 3:
            valor = float(input("Digite o valor do ingresso Normal: "))
            valor_adicional = float(input("Digite o valor adicional do ingresso LowerStateroom: "))
            localizacao = input("Digite a localização do LowerStateroom: ")
            lower_stateroom = LowerStateroom(valor, valor_adicional, localizacao)
            print("LowerStateroom criado.\n")

        elif choice == 4:
            valor = float(input("Digite o valor do ingresso Normal: "))
            valor_adicional = float(input("Digite o valor adicional do ingresso SuperiorStateroom: "))
            valor_adicional_superior = float(input("Digite o valor adicional do SuperiorStateroom (extra): "))
            localizacao = input("Digite a localização do SuperiorStateroom: ")
            superior_stateroom = SuperiorStateroom(valor, valor_adicional, localizacao, valor_adicional_superior)
            print("SuperiorStateroom criado.\n")

        elif choice == 5:
            if ingresso_normal:
                print(f"Valor do ingresso Normal: R$ {ingresso_normal.get_valor():.2f}")
            else:
                print("Nenhum ingresso Normal criado.\n")

        elif choice == 6:
            if ingresso_vip:
                print(f"Valor do ingresso VIP: R$ {ingresso_vip.get_valor():.2f}")
            else:
                print("Nenhum ingresso VIP criado.\n")

        elif choice == 7:
            if lower_stateroom:
                print(f"Valor do LowerStateroom: R$ {lower_stateroom.get_valor():.2f}")
                lower_stateroom.exibir_localizacao()
            else:
                print("Nenhum LowerStateroom criado.\n")

        elif choice == 8:
            if superior_stateroom:
                print(f"Valor do SuperiorStateroom: R$ {superior_stateroom.get_valor():.2f}")
                superior_stateroom.exibir_localizacao()
            else:
                print("Nenhum SuperiorStateroom criado.\n")

        elif choice == 9:
            if lower_stateroom:
                print(f"Localização do LowerStateroom: {lower_stateroom.get_localizacao()}")
            else:
                print("Nenhum LowerStateroom criado.\n")

main()
