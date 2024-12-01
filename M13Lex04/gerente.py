from funcionario import Funcionario

class Gerente(Funcionario):
    def obter_cargo(self):
        return "Gerente"

    def gerenciar_equipe(self):
        print(f"{self.obter_nome()} está gerenciando a equipe.")
