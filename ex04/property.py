class Property:
    def __init__(self, endereco, preco):
        self.endereco = endereco
        self.preco = preco

    def get_endereco(self):
        return self.endereco

    def get_preco(self):
        return self.preco

    def exibir_dados(self):
        print(f"Endereço: {self.endereco}")
        print(f"Preço: R$ {self.preco:.2f}")

class NewProperty(Property):
    def __init__(self, endereco, preco, adicional):
        super().__init__(endereco, preco)
        self.__adicional = adicional

    def get_adicional(self):
        return self.__adicional

    def exibir_adicional(self):
        print(f"Adicional: R$ {self.get_adicional()}")

    def get_preco(self):
        return super().get_preco() + self.get_adicional()

    def exibir_dados(self):
        super().exibir_dados()
        self.exibir_adicional()
        print(f"Preço com Adicional: R$ {self.get_preco()}")

class OldProperty(Property):
    def __init__(self, endereco, preco, desconto):
        super().__init__(endereco, preco)
        self.__desconto = desconto

    def get_desconto(self):
        return self.__desconto

    def exibir_desconto(self):
        print(f"Desconto: R$ {self.get_desconto():.2f}")

    def get_preco(self):
        return super().get_preco() - self.get_desconto()

    def exibir_dados(self):
        super().exibir_dados()
        self.exibir_desconto()
        print(f"Preço com Desconto: R$ {self.get_preco():.2f}")
