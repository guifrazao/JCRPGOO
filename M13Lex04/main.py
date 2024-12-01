"""
Implemente um sistema de Empresa com os tipos de funcionários (gerente, vendedor,
recepcionista, secretário, etc.), evidenciando a classe Employee como uma classe
abstrata.
"""
from gerente import Gerente
from vendedor import Vendedor
from recepcionista import Recepcionista
from secretario import Secretario
def main():
    funcionarios = [
        Gerente("Gustavo", "001", 8000),
        Vendedor("Carlos", "002", 3000),
        Recepcionista("Gui", "003", 2000),
        Secretario("Kendy", "004", 2500)
    ]

    print("Lista de Funcionários:\n")
    for funcionario in funcionarios:
        print(f"Role: {funcionario.get_role()}")
        print(funcionario)
        if isinstance(funcionario, Gerente):
            funcionario.manage_team()
        elif isinstance(funcionario, Vendedor):
            funcionario.sell_product()
        elif isinstance(funcionario, Recepcionista):
            funcionario.greet_visitors()
        elif isinstance(funcionario, Secretario):
            funcionario.organize_documents()
        print("=-"*30)
        print()

main()
