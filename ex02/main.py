from animal import Dog, Cat

def menu():
    option = -1
    while option < 0 or option > 7:
        print("\n1 - Adicionar um cachorro.\n" +
              "2 - Adicionar um gato.\n" +
              "3 - Fazer o cachorro latir.\n" +
              "4 - Fazer o gato miar.\n" +
              "5 - Fazer o cachorro andar.\n" +
              "6 - Fazer o gato andar.\n" +
              "7 - Sair.\n")
        option = int(input("Digite sua opção: "))
        if option < 0 or option > 7:
            print("\tOpção inválida! Digite novamente.")
    return option

def main():
    dog = None
    cat = None

    choice = 100

    while choice != 7:
        choice = menu()

        if choice == 7:
            print("Encerrando...\n")
            break

        elif choice == 1:
            name = input("Digite o nome do cachorro: ")
            breed = input("Digite a raça do cachorro (opcional): ")
            dog = Dog(name, breed)
            print(f"Cachorro {name} adicionado.\n")

        elif choice == 2:
            name = input("Digite o nome do gato: ")
            breed = input("Digite a raça do gato (opcional): ")
            cat = Cat(name, breed)
            print(f"Gato {name} adicionado.\n")

        elif choice == 3:
            if dog:
                print(dog.barks())
            else:
                print("Nenhum cachorro adicionado.\n")

        elif choice == 4:
            if cat:
                print(cat.meow())
            else:
                print("Nenhum gato adicionado.\n")

        elif choice == 5:
            if dog:
                print(dog.walk())
            else:
                print("Nenhum cachorro adicionado.\n")

        elif choice == 6:
            if cat:
                print(cat.walk())
            else:
                print("Nenhum gato adicionado.\n")

main()
