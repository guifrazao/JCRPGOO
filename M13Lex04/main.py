"""
Sistema de Empresa com diferentes tipos de funcionários, demonstrando o uso
do Princípio da Inversão da Dependência (DIP).
"""

from gerente import Gerente
from vendedor import Vendedor
from recepcionista import Recepcionista
from secretario import Secretario
from email_servico import ServicoEmail
from sms_servico import ServicoSMS

def main():
    # Serviços de notificação
    servico_email = ServicoEmail()
    servico_sms = ServicoSMS()

    # Funcionários
    funcionarios = [
        Gerente("Gustavo", "001", 8000),
        Vendedor("Carlos", "002", 3000),
        Recepcionista("Gui", "003", 2000),
        Secretario("Kendy", "004", 2500)
    ]

    print("Lista de Funcionários:\n")
    for funcionario in funcionarios:
        print(f"Cargo: {funcionario.obter_cargo()}")
        print(funcionario)
        if isinstance(funcionario, Gerente):
            funcionario.gerenciar_equipe()
            servico_email.notificar(funcionario.obter_nome(), "Relatório de desempenho enviado para análise.")
        elif isinstance(funcionario, Vendedor):
            funcionario.vender_produtos()
            servico_sms.notificar(funcionario.obter_nome(), "Meta de vendas atualizada.")
        elif isinstance(funcionario, Recepcionista):
            funcionario.cumprimentar_visitantes()
            servico_email.notificar(funcionario.obter_nome(), "Treinamento sobre atendimento disponível.")
        elif isinstance(funcionario, Secretario):
            funcionario.organizar_documentos()
            servico_sms.notificar(funcionario.obter_nome(), "Nova tarefa adicionada à agenda.")
        print("=-"*30)
        print()

main()
