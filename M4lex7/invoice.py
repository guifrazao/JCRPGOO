'''Crie uma classe Invoice para que uma loja de suprimentos de informática possa
utilizá-la para representar a fatura de um item vendido na loja. Uma Invoice deve
incluir quatro variáveis de instância: o número da fatura (string), a descrição (string),
a quantidade comprada de um item (int) e o preço por item (float). Sua classe deve ter
um construtor que inicializa as quatro variáveis de instância. Forneça um método set
e um get para cada variável de instância. Forneça também um método chamado que
calcula o valor da fatura (multiplica preço por quantidade do item) e retorna o
resultado. Se a quantidade de itens passada pelo usuário não for positiva, deve ser
configurada como 0. Se o preço do item não for positivo, deve ser configurado como
0.0. Teste a classe implementada e seus métodos.'''

class Invoice:
    def __init__(self, invoice_number, description, quantity, price_per_item):
        self.__invoice_number = invoice_number
        self.__description = description
        self.set_quantity(quantity)  # Usando o setter com validação
        self.set_price_per_item(price_per_item)  # Usando o setter com validação
    
    def set_invoice_number(self, invoice_number):
        self.__invoice_number = invoice_number

    def get_invoice_number(self):
        return self.__invoice_number
    
    def set_description(self, description):
        self.__description = description

    def get_description(self):
        return self.__description
    
    # Método para validar a quantidade
    def validate_quantity(self, quantity):
        if quantity < 0:
            return 0  # Retorna 0 se a quantidade for negativa
        return quantity

    # Setter que usa a validação
    def set_quantity(self, quantity):
        self._quantity = self.validate_quantity(quantity)

    def get_quantity(self):
        return self._quantity
    
    # Método para validar o preço por item
    def validate_price(self, price_per_item):
        if price_per_item < 0:
            return 0.0  # Retorna 0.0 se o preço for negativo
        return price_per_item

    # Setter que usa a validação
    def set_price_per_item(self, price_per_item):
        self._price_per_item = self.validate_price(price_per_item)

    def get_price_per_item(self):
        return self._price_per_item
    
    # Método para calcular o total da fatura
    def invoice_calculation(self):
        return self.get_price_per_item() * self.get_quantity()


