"""
Escolha pelo menos 5 exercícios das listas M3L e M5L (5 de cada) para expandir o projeto do
exercício, incluindo novas classes relacionadas, conforme a sua criatividade, demonstrando
a associação bilateral.

Crie uma classe chamada Invoice que possa ser utilizado por uma loja de
suprimentos de informática para representar uma fatura de um item vendido na loja.
Uma fatura deve incluir as seguintes informações como atributos:
• o número do item faturado,
• a descrição do item,
• a quantidade comprada do item e
• o preço unitário do item.
Sua classe deve ter um construtor que inicialize os quatro atributos. Se a quantidade
não for positiva, ela deve ser configurada como 0. Se o preço por item não for
positivo ele deve ser configurado como 0.0. Forneça um método set e um método get
para cada variável de instância. Além disso, forneça um método chamado que calcula
o valor da fatura (isso é, multiplica a quantidade pelo preço por item) e depois retorna
o valor real. Escreva um aplicativo de teste que demonstra as capacidades da classe
Invoice.
""" 


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