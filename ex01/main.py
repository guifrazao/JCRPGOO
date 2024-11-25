from employee import *

def menu():
    option = -1
    while option < 0 or option > 5:
        print("\n1 - Adicionar Assistente Administrativo.\n" +
              "2 - Adicionar Assistente Técnico.\n" +
              "3 - Exibir dados de Assistente Administrativo.\n" +
              "4 - Exibir dados de Assistente Técnico.\n" +
              "5 - Sair.\n")
        option = int(input("Digite sua opção: "))
        if option < 0 or option > 5:
            print("\tOpção inválida! Digite novamente.")
    return option

def main():
    administrative_assistant = None
    technical_assistant = None

    choice = 100

    while choice != 5:
        choice = menu()

        if choice == 5:
            print("Encerrando...\n")
            break

        elif choice == 1:
            nome = input("Digite o nome: ")
            numero_matricula = input("Digite o número de matrícula: ")
            salario = float(input("Digite o salário base: R$"))
            turno = input("Digite o turno (dia/noite): ")
            adicional_noturno = 0.0
            if turno.lower() == "noite":
                adicional_noturno = float(input("Digite o adicional noturno(%): "))
            administrative_assistant = AdministrativeAssistant(nome, numero_matricula, salario, turno, adicional_noturno)
            administrative_assistant.atualizar_salario()
            print("Assistente Administrativo adicionado.\n")

        elif choice == 2:
            nome = input("Digite o nome: ")
            numero_matricula = input("Digite o número de matrícula: ")
            salario = float(input("Digite o salário base: R$"))
            bonus_salarial = float(input("Digite o bônus salarial: R$"))
            technical_assistant = TechnicalAssistant(nome, numero_matricula, salario, bonus_salarial)
            technical_assistant.atualizar_salario()
            print("Assistente Técnico adicionado.\n")

        elif choice == 3:
            if administrative_assistant:
                print("\nDados do Assistente Administrativo:")
                administrative_assistant.exibir_dados()
            else:
                print("Nenhum Assistente Administrativo cadastrado.\n")

        elif choice == 4:
            if technical_assistant:
                print("\nDados do Assistente Técnico:")
                technical_assistant.exibir_dados()
            else:
                print("Nenhum Assistente Técnico cadastrado.\n")

main()
