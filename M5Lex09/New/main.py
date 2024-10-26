from Modulos import *  # Importa todas as classes e funções do módulo Modulos


def obter_valor(mensagem, tipo, validar_funcao):
    while True:
        try:
            valor = tipo(input(mensagem))
            if validar_funcao(valor):
                return valor
            else:
                print(f"⚠️ Valor inválido para {mensagem.strip(': ')}. Tente novamente.")
        except ValueError:
            print(f"⚠️ Entrada inválida. Por favor, insira um valor {tipo.__name__}.")


def criar_proprietario(validator_owner):
    nome = obter_valor("Digite o nome do proprietário: ", str, validator_owner.verifyName)
    cpf = obter_valor("Digite o CPF do proprietário (11 dígitos): ", str, validator_owner.verifyCPF)
    tel = obter_valor("Digite o telefone do proprietário com DDD (11 dígitos): ", str, validator_owner.verifyTel)
    return Owner(nome, cpf, tel)


def criar_invoice(validator_invoice, proprietario):
    item_number = obter_valor("Digite o ID do produto (5 a 8 dígitos): ", int, validator_invoice.verifyItem_number)
    description = input("Digite a descrição do produto: ")
    quantity = obter_valor("Digite a quantidade de produtos: ", int, validator_invoice.verifyQuantity)
    price_per_item = obter_valor("Digite o preço unitário do produto: R$", float, validator_invoice.verifyPrice)
    return Invoice(item_number, description, quantity, price_per_item, proprietario)


def menu():
    validator_invoice = Validator_invoice()
    validator_owner = Validator_Owner()
    proprietario = None
    faturas = []

    while True:
        print("\n" + "=" * 50)
        print(" " * 12 + "✦ MENU PRINCIPAL ✦")
        print("=" * 50)
        print("1️⃣  Criar Proprietário")
        print("2️⃣  Criar Fatura (associar com proprietário existente)")
        print("3️⃣  Mostrar Informações da(s) Fatura(s)")
        print("4️⃣  Sair")
        print("=" * 50)

        escolha = input("Digite sua escolha: ").strip()

        if escolha == '1':
            proprietario = criar_proprietario(validator_owner)
            print("✔️ Proprietário criado com sucesso.")
        elif escolha == '2':
            if proprietario is None:
                print("⚠️ Primeiro, crie um proprietário para associar a fatura.")
            else:
                fatura = criar_invoice(validator_invoice, proprietario)
                faturas.append(fatura)
                print("✔️ Fatura criada e associada ao proprietário com sucesso.")
        elif escolha == '3':
            if not faturas:
                print("⚠️ Nenhuma fatura disponível.")
            else:
                print("\n" + "=" * 50)
                print(" " * 12 + "✦ INFORMAÇÕES DAS FATURAS ✦")
                print("=" * 50)
                for index, fatura in enumerate(faturas):
                    print(f"\n📄 Fatura {index + 1}:")
                    print(fatura)
                    total = fatura.calculate_total()
                    print(f"💰 Valor total da fatura: R${total:.2f}")
                print("=" * 50)
        elif escolha == '4':
            print("👋 Saindo...")
            break
        else:
            print("❌ Escolha inválida. Tente novamente.")


def main():
    menu()

main()
