"""
Refazer as listas M3L e M5L, aplicando o Princípio Aberto-Fechado e mostrar as diferenças
de seu código, antes e depois.

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
