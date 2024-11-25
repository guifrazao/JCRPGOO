class Empregado:
    def __init__(self, nome, numero_matricula, salario):
        self.nome = nome
        self.numero_matricula = numero_matricula
        self.salario = salario

    def exibir_dados(self):
        print(f"Nome: {self.nome}, Matrícula: {self.numero_matricula}, Salário: R$ {self.salario:.2f}")

class AssistenteAdministrativo(Empregado):
    def __init__(self, nome, numero_matricula, salario, cargo):
        super().__init__(nome, numero_matricula, salario)
        self.cargo = cargo

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Cargo: {self.cargo}")

class Tecnico(Empregado):
    def __init__(self, nome, numero_matricula, salario, area):
        super().__init__(nome, numero_matricula, salario)
        self.area = area

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Área de Atuação: {self.area}")

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def caminhar(self):
        print(f"{self.nome} está caminhando.")

    def comer(self):
        pass  # Método a ser sobreposto

class Cachorro(Animal):
    def latir(self):
        print(f"{self.nome} está latindo: Au Au!")

    def comer(self):
        return "Bife"

class Gato(Animal):
    def miar(self):
        print(f"{self.nome} está miando: Miau!")

    def comer(self):
        return "Peixe"

class Ticket:
    def __init__(self, valor):
        self.valor = valor

    def get_valor(self):
        return self.valor

class VIP(Ticket):
    def __init__(self, valor, adicional):
        super().__init__(valor)
        self.adicional = adicional

    def get_valor(self):
        return super().get_valor() + self.adicional

class CamaroteSuperior(VIP):
    def __init__(self, valor, adicional, adicional_superior):
        super().__init__(valor, adicional)
        self.adicional_superior = adicional_superior

    def get_valor(self):
        return super().get_valor() + self.adicional_superior

class CamaroteInferior(VIP):
    def __init__(self, valor, adicional):
        super().__init__(valor, adicional)

class Property:
    def __init__(self, endereco, preco):
        self.endereco = endereco
        self.preco = preco

    def get_preco(self):
        return self.preco

class NewProperty(Property):
    def __init__(self, endereco, preco, adicional):
        super().__init__(endereco, preco)
        self.adicional = adicional

    def get_preco(self):
        return super().get_preco() + self.adicional

class OldProperty(Property):
    def __init__(self, endereco, preco, desconto):
        super().__init__(endereco, preco)
        self.desconto = desconto

    def get_preco(self):
        return super().get_preco() - self.desconto