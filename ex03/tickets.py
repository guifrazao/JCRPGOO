'''
3. Crie uma classe chamada Ticket que possui um valor em reais e um método que 
retorne o valor do ingresso. 
a. Crie uma classe VIP, que herda Ticket e possui um valor adicional. Crie um 
método sobreposto que retorne o valor do ingresso VIP (com o adicional 
incluído). 
b. Crie uma classe Normal, que herda Ticket e possui um método que retorna o 
valor “normal” do ingresso. 
c. Crie uma classe LowerStateroom (que possui a localização do ingresso e 
métodos para acessar e imprimir a localização) e uma classe 
SuperiorStateroom, que é mais cara (possui valor adicional). Esta última 
possui um método para retornar o valor do ingresso, sobrepondo o método 
que retorna este valor. Ambas as classes herdam a classe VIP. 
'''
class Ticket:
    def __init__(self, valor):
        self.valor = valor

    def get_valor(self):
        return self.valor

class VIP(Ticket):
    def __init__(self, valor, valor_adicional):
        super().__init__(valor)
        self.valor_adicional = valor_adicional

    def get_valor(self):
        return self.valor + self.valor_adicional

class Normal(Ticket):
    def get_valor(self):
        return self.valor

class LowerStateroom(VIP):
    def __init__(self, valor, valor_adicional, localizacao):
        super().__init__(valor, valor_adicional)
        self.localizacao = localizacao

    def get_localizacao(self):
        return self.localizacao

    def exibir_localizacao(self):
        print(f"Localização: {self.localizacao}")

class SuperiorStateroom(VIP):
    def __init__(self, valor, valor_adicional, valor_adicional_superior):
        super().__init__(valor, valor_adicional)
        self.valor_adicional_superior = valor_adicional_superior

    def get_valor(self):
        return super().get_valor() + self.valor_adicional_superior


