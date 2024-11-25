from property import *

def menu():
    option = -1
    while option < 0 or option > 6:
        print("\n1 - Criar Propriedade Nova\n" +
              "2 - Criar Propriedade Antiga\n" +
              "3 - Exibir dados da Propriedade Nova\n" +
              "4 - Exibir dados da Propriedade Antiga\n" +
              "5 - Sair\n")
        option = int(input("Digite sua opção: "))
        if option < 0 or option > 6:
            print("\tOpção inválida! Digite novamente.")
    return option

def main():
    new_prop = None
    old_prop = None

    choice = 100

    while choice != 5:
        choice = menu()

        if choice == 5:
            print("Encerrando...\n")
            break

        elif choice == 1:
            endereco = input("Digite o endereço da Propriedade Nova: ")
            preco = float(input("Digite o preço da Propriedade Nova: "))
            adicional = float(input("Digite o valor adicional: "))
            new_prop = NewProperty(endereco, preco, adicional)
            print("Propriedade Nova criada.\n")

        elif choice == 2:
            endereco = input("Digite o endereço da Propriedade Antiga: ")
            preco = float(input("Digite o preço da Propriedade Antiga: "))
            desconto = float(input("Digite o valor do desconto: "))
            old_prop = OldProperty(endereco, preco, desconto)
            print("Propriedade Antiga criada.\n")

        elif choice == 3:
            if new_prop:
                print("\nDados da Propriedade Nova:")
                new_prop.exibir_dados()
            else:
                print("Nenhuma Propriedade Nova criada.\n")

        elif choice == 4:
            if old_prop:
                print("\nDados da Propriedade Antiga:")
                old_prop.exibir_dados()
            else:
                print("Nenhuma Propriedade Antiga criada.\n")

main()
