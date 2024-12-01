from funcionario import Funcionario

class Vendedor(Funcionario):
    def obter_cargo(self):
        return "Vendedor"

    def vender_produtos(self):
        print(f"{self.obter_nome()} está vendendo produtos.")
