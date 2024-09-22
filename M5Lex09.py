"""
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

class Invoice:
    def __init__(self, item_number, description, quantity, price_per_item):
        self._item_number = self._validate_item_number(item_number)
        self._description = description
        self._quantity = self._validate_quantity(quantity)
        self._price_per_item = self._validate_price(price_per_item)

    @staticmethod
    def _validate_item_number(item_number):
        if not item_number.isdigit() or not (4 <= len(item_number) <= 8):
            raise ValueError("O número do item deve ser um número com 4 a 8 dígitos.")
        return item_number

    @staticmethod
    def _validate_quantity(quantity):
        if quantity < 0:
            return 0
        return quantity

    @staticmethod
    def _validate_price(price):
        if price < 0:
            return 0.0
        return price

    def set_item_number(self, item_number):
        self._item_number = self._validate_item_number(item_number)

    def get_item_number(self):
        return self._item_number

    def set_description(self, description):
        self._description = description

    def get_description(self):
        return self._description

    def set_quantity(self, quantity):
        self._quantity = self._validate_quantity(quantity)

    def get_quantity(self):
        return self._quantity

    def set_price_per_item(self, price):
        self._price_per_item = self._validate_price(price)

    def get_price_per_item(self):
        return self._price_per_item

    def calculate_total(self):
        return self._quantity * self._price_per_item