from invoice import Invoice
from owner import Owner
from order import Order
from validator import Validator_invoice, Validator_Owner

class OwnerFactory:
    def create(self):
        name = obter_valor("Digite o nome do proprietário: ", str, Validator_Owner.verifyName)
        cpf = obter_valor("Digite o CPF do proprietário: ", str, Validator_Owner.verifyCPF)
        tel = obter_valor("Digite o Telefone do proprietário com DDD: ", str, Validator_Owner.verifyTel)
        return Owner(name, cpf, tel)

class OrderFactory:
    def __init__(self, owner):
        self.owner = owner

    def create(self):
        return Order(self.owner)

class InvoiceFactory:
    def __init__(self, order):
        self.order = order

    def create(self):
        item_number = obter_valor("Digite o ID do produto: ", int, Validator_invoice.verifyItem_number)
        description = input("Digite a descrição do produto: ")
        quantity = obter_valor("Digite a quantidade de produtos comprados: ", int, Validator_invoice.verifyQuantity)
        price_per_item = obter_valor("Digite o preço unitario do produto: R$", float, Validator_invoice.verifyPrice)
        return Invoice(item_number, description, quantity, price_per_item, self.order.get_owner())

def obter_valor(mensagem, tipo, validar_funcao):
    while True:
        try:
            valor = tipo(input(mensagem))
            validar_funcao(valor)
            return valor
        except ValueError as e:
            print(f"Erro: {e}. Tente novamente.")
        except Exception as err:
            print(f"Erro: {err}. Tente novamente.")

def exibir_menu():
    print("""\n========= MENU PRINCIPAL =========
1 - Cadastrar pessoa
2 - Criar pedido
3 - Fazer fatura
4 - Mostrar informações da fatura
5 - Sair
=================================\n""")

def main():
    owner_factory = OwnerFactory()
    owner = None
    order = None
    invoice = None
    while True:
        exibir_menu()
        try:
            opcao = int(input("Digite a opção desejada: "))
            print("=-" * 30)
            if opcao == 1:
                owner = owner_factory.create()
                print("\n### Pessoa cadastrada com sucesso. ###\n")
            elif opcao == 2:
                if owner is not None:
                    order_factory = OrderFactory(owner)
                    order = order_factory.create()
                    print("\n### Pedido criado com sucesso. ###\n")
                else:
                    print("\nVocê deve cadastrar uma pessoa primeiro.\n")
            elif opcao == 3:
                if order is not None:
                    invoice_factory = InvoiceFactory(order)
                    invoice = invoice_factory.create()
                    print("\n### Fatura criada com sucesso. ###\n")
                else:
                    print("\nVocê deve criar um pedido primeiro.\n")
            elif opcao == 4:
                if invoice is not None:
                    print("\n========= FATURA =========")
                    print(invoice)
                    total = invoice.calculate_total()
                    print(f"Valor total da fatura: R${total:.2f}")
                    print("===========================\n")
                else:
                    print("\nNenhuma fatura disponível. Por favor, crie uma fatura primeiro.\n")
            elif opcao == 5:
                print("\nSaindo... Até a próxima!\n")
                break
            else:
                print("\nOpção inválida. Escolha um número entre 1 e 5.\n")
        except ValueError:
            print("\nErro: O valor deve ser um número inteiro. Tente novamente.\n")
        except Exception as err:
            print(f"\nErro: {err}. Tente novamente.\n")

main()
