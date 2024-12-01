"""
Implemente um sistema de Empresa com os tipos de funcionários (gerente, vendedor,
recepcionista, secretário, etc.), evidenciando a classe Employee como uma classe
abstrata.
"""
from gerente import Gerente
from vendedor import Vendedor
from recepcionista import Recepcionista
from secretario import Secretario
from departamento import Departamento
from projeto import Projeto

def main():
    # Criando os funcionários
    gerente = Gerente("Gustavo", "001", 8000)
    vendedor = Vendedor("Carlos", "002", 3000)
    recepcionista = Recepcionista("Gui", "003", 2000)
    secretario = Secretario("Kendy", "004", 2500)

    # Criando o departamento de "Vendas"
    vendas = Departamento("Vendas")
    vendas.adicionar_funcionario(gerente)
    vendas.adicionar_funcionario(vendedor)

    # Criando o departamento de "Administração"
    administracao = Departamento("Administração")
    administracao.adicionar_funcionario(recepcionista)
    administracao.adicionar_funcionario(secretario)

    # Listando os funcionários de cada departamento
    vendas.listar_funcionarios()
    print("="*60)
    administracao.listar_funcionarios()

    # Criando um projeto
    projeto_marketing = Projeto("Campanha de Marketing", "Campanha de vendas de fim de ano.")
    
    # Atribuindo departamentos ao projeto
    projeto_marketing.adicionar_equipe(vendas)
    projeto_marketing.adicionar_equipe(administracao)

    # Listando as equipes do projeto
    projeto_marketing.listar_equipe()

    print("="*60)

    # Simulando a remoção de um funcionário e a realocação para outro departamento
    print("Realocando o recepcionista para o departamento de Vendas...")
    administracao.remover_funcionario(recepcionista)
    vendas.adicionar_funcionario(recepcionista)
    vendas.listar_funcionarios()

main()
