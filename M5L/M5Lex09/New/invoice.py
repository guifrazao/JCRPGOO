'''
M5L-ex09. Crie uma classe chamada Invoice que possa ser utilizado por uma loja de 
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
'''

from validator import Validator_invoice
from owner import Owner

class Invoice:
    def __init__(self, item_number, description, quantity, price_per_item, owner: Owner):
        if not Validator_invoice.verifyItem_number(item_number):
            raise Exception("Item number")
        if not Validator_invoice.verifyQuantity(quantity):
            raise Exception("Quantity")
        if not Validator_invoice.verifyPrice(price_per_item):
            raise Exception("Price per item")
        self.__item_number = item_number
        self.__description = description
        self.__quantity = quantity
        self.__price_per_item = price_per_item
        self.__owner = owner

    def __str__(self):
        return f"\nInformações Proprietário\n{self.__owner}\n =--=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\nInformações produto\nItem number: {self.__item_number}\nQuantity: {self.__quantity}\nPrice per item: {self.__price_per_item}"

    def calculate_total(self):
        return self.__quantity * self.__price_per_item
