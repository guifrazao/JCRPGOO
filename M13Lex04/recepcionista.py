from funcionario import Funcionario

class Recepcionista(Funcionario):
    def obter_cargo(self):
        return "Recepcionista"

    def cumprimentar_visitantes(self):
        print(f"{self.obter_nome()} está cumprimentando os visitantes.")
