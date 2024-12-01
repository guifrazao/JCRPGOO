from employee import Employee
from gerente import Gerente
from recepcionista import Recepcionista
from vendedor import Vendedor
from secretario import Secretario

class Departamento:
    def __init__(self, nome):
        self.__nome = nome
        self.__funcionarios = []

    def adicionar_funcionario(self, funcionario):
        if isinstance(funcionario, Employee):  # Garante que é um funcionário
            self.__funcionarios.append(funcionario)
        else:
            print("O funcionário não é válido.")

    def remover_funcionario(self, funcionario):
        if funcionario in self.__funcionarios:
            self.__funcionarios.remove(funcionario)
        else:
            print(f"{funcionario.get_name()} não está no departamento.")

    def listar_funcionarios(self):
        print(f"Funcionários no departamento de {self.__nome}:")
        for funcionario in self.__funcionarios:
            print(f"{funcionario.get_name()} - {funcionario.get_role()}")

    def get_nome(self):  # Método adicionado para acessar o nome do departamento
        return self.__nome

    def __str__(self):
        return f"Departamento: {self.__nome}"

