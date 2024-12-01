from funcionario import Funcionario

class Secretario(Funcionario):
    def obter_cargo(self):
        return "Secretário"

    def organizar_documentos(self):
        print(f"{self.obter_nome()} está organizando documentos.")
