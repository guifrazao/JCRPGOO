from os import system
from estudantes import Estudante, Graduacao, Mestrado, Doutorado, EnsinoMedio
from gestaoAcademica import GestaoAcademica

class Menu:
    def __init__(self):
        self.gestaoAcademica = GestaoAcademica()

    @staticmethod
    def escolherOpcao(opcoes, valor_min, valor_max):
        opcao = -1
        
        while opcao < valor_min or opcao > valor_max:
            print(opcoes)
            opcao = int(input("Digite sua opção: "))
            if opcao < valor_min or opcao > valor_max:
                system('cls')
                print("\tOpção inválida! Digite novamente.")
            
        return opcao
    
    @staticmethod 
    def coletarDadosEstudantes():
        nome = input("Nome do estudante: ")
        matricula = input("Matrícula do estudante: ")
        idade = int(input("Idade do estudante: "))
        
        return nome, matricula, idade
    
    def menuPrincipal(self):
        opcoes = "\n1 - Adicionar estudante.\n2 - Remover estudante.\n3 - Consultar Estudantes.\n4 - Avaliar trabalhos de estudantes.\n0 - Sair.\n"
        
        escolha = 100      
        while escolha:
            print("Gestão Acadêmica")
            escolha = escolha = Menu.escolherOpcao(opcoes, valor_min=0, valor_max=4)

            if escolha == 0:
                break

            if escolha == 1:
                system('cls')
                self.menuAdicionarEstudante()
                
            elif escolha == 2:
                system('cls')
                matricula = input("Digite a matrícula do estudante a ser removido: ")
                estudante = self.gestaoAcademica.buscarEstudantePorMatricula(matricula)
                if not estudante:
                    print("Estudante não existe no sistema")
                    continue

                if self.gestaoAcademica.removerEstudante(estudante):
                    print("Estudante removido com sucesso!")
                else:
                    print("Erro ao remover estudante")
            
            elif escolha == 3:
                system('cls')
                self.gestaoAcademica.consultarEstudantes()
            
            else:
                system('cls')
                self.gestaoAcademica.receberEntregaTrabalhos()

    def menuAdicionarEstudante(self):
        print("Qual tipo de estudante deseja adicionar?\n")
        opcoes = "\n1 - Ensino médio\n2 - Graduação.\n3 - Mestrado.\n4 - Doutorado.\n0 - Voltar.\n"

        escolha = 100      
        while escolha:
            escolha = escolha = Menu.escolherOpcao(opcoes, valor_min=0, valor_max=4)

            if escolha == 0:
                system('cls')
                break

            if escolha == 1:
                system('cls')
                nome, matricula, idade = Menu.coletarDadosEstudantes()
                self.gestaoAcademica.adicionarEstudante(EnsinoMedio(nome, matricula, idade, numero_notas=4))

            elif escolha == 2:
                system('cls')
                nome, matricula, idade = Menu.coletarDadosEstudantes()
                self.gestaoAcademica.adicionarEstudante(Graduacao(nome, matricula, idade, numero_notas=4))
                
            elif escolha == 3:
                system('cls')
                nome, matricula, idade = Menu.coletarDadosEstudantes()
                self.gestaoAcademica.adicionarEstudante(Mestrado(nome, matricula, idade, numero_notas=3))
            
            else:
                system('cls')
                nome, matricula, idade = Menu.coletarDadosEstudantes()
                self.gestaoAcademica.adicionarEstudante(Doutorado(nome, matricula, idade, numero_notas=3))
