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
    def __init__(self, invoice_number, description, quantity, price_per_item ):
        self.__invoice_number = invoice_number
        self.__description = description
        self.set_quantity(quantity)  # Usando o método setter para garantir a validação
        self.set_price_per_item(price_per_item) 
    
    def set_invoice_number(self, invoice_number):
        self.__invoice_number = invoice_number

    def get_invoice_number(self):
        return self.__invoice_number
    
    def set_description(self, description):
        self.__description = description

    def get_description(self):
        return self.__description
    
    def set_quantity(self, quantity):
        if quantity < 0:
            self._quantity = 0
        else:
            self._quantity = quantity

    def get_quantity(self):
        return self._quantity
    
    def set_price_per_item(self, price_per_item):
        if price_per_item < 0:
            self._price_per_item = 0.0
        else:
            self._price_per_item = price_per_item

    def get_price_per_item(self):
        return self._price_per_item
    
    def invoice_calculation(self):
        return self.get_price_per_item() * self.get_quantity()
        

