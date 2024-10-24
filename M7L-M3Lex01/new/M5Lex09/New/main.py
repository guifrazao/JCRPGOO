from invoice import Invoice
from owner import Owner
from validator import Validator

def obter_valor(mensagem, tipo, validar_funcao):
    while True:
        try:
            valor = tipo(input(mensagem))
            return validar_funcao(valor)
        except ValueError as e:
            print(f"Erro: {e}. Tente novamente.")
        except Exception as err:
            print(f"Erro: {err}. Tente novamente.")

def criar_proprietario():
    while True:
        try:
            nome_proprietario = obter_valor("Digite o nome do proprietário: ", str, Validator.verify_name)
            print("--"*30)
            cpf_proprietario = obter_valor("Digite o CPF do proprietário: ", str, Validator.verify_cpf)
            print("=-"*30)
            tel_proprietario = obter_valor("Digite o Telefone do proprietário com DDD: ", str, Validator.verify_tel)
            print("=-"*30)
            return Owner(nome_proprietario, cpf_proprietario, tel_proprietario)
        except Exception as err:
            print(f"Erro: {err}. Tente novamente.")
            print("--"*30)

def criar_invoice():
    owner = criar_proprietario()
    while True:
        try:
            item_number = obter_valor("Digite o ID do produto: ", int, Validator.verify_item_number)
            description = input("Digite a descrição do produto: ")
            quantity = obter_valor("Digite a quantidade de produtos comprados: ", int, Validator.verify_quantity)
            price = obter_valor("Digite o preço unitario do produto: R$", float, Validator.verify_price)
            return Invoice(item_number, description, quantity, price, owner)
        except Exception as err:
            print(f"Erro: {err}. Tente novamente.")

def main():
    fatura = criar_invoice()
    print("=-"*30)
    print("### FATURA ###")
    print(fatura)
    total = fatura.calculate_total()
    print(f"Valor total da fatura: R${total:.2f}")

main()
