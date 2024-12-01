from os import system
from zoologico import Zoologico
from familias_animais import Anfibio, Reptil, Ave, Mamifero
from animais_especiais import AveAquatica, MamiferoVoador

class Menu:
    def __init__(self):
        self.__zoologico = Zoologico()

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
    
    def menuPrincipal(self):
        opcoes = "\n1 - Adicionar animal.\n2 - Visitar animais\n3 - Listar anfíbios.\n4 - Listar repteis.\n5 - Listar aves.\n6 - Listar mamíferos.\n0 - Sair.\n"
        
        escolha = 100      
        while escolha:
            print("Zoológico")
            escolha = escolha = Menu.escolherOpcao(opcoes, valor_min=0, valor_max=6)

            if escolha == 0:
                break

            if escolha == 1:
                system('cls')
                self.menuAdicionarAnimal()

            elif escolha == 2:
                system('cls')
                self.menuVisitarAnimais()
                
            elif escolha == 3:
                system('cls')
                if self.__zoologico.temEsteTipo(Anfibio):
                    self.__zoologico.imprimirInformacoesAnfibios()
                else:
                    print("Não tem nenhum anfíbio neste zoológico\n")
            
            elif escolha == 4:
                system('cls')
                if self.__zoologico.temEsteTipo(Reptil):
                    self.__zoologico.imprimirInformacoesRepteis()
                else:
                    print("Não tem nenhum réptil neste zoológico\n")
            
            elif escolha == 5:
                system('cls')
                if self.__zoologico.temEsteTipo(Ave):
                    self.__zoologico.imprimirInformacoesAves()
                else:
                    print("Não tem nenhuma ave neste zoológico\n")

            else:
                system('cls')
                if self.__zoologico.temEsteTipo(Mamifero):
                    self.__zoologico.imprimirInformacoesMamiferos()
                else:
                    print("Não tem nenhum mamífero neste zoológico\n")

    def menuAdicionarAnimal(self):
        print("Qual tipo de animal deseja adicionar?\n")
        opcoes = "\n1 - Anfíbio.\n2 - Réptil.\n3 - Ave.\n4 - Mamífero.\n0 - Voltar.\n"

        escolha = 100      
        while escolha:
            escolha = escolha = Menu.escolherOpcao(opcoes, valor_min=0, valor_max=5)

            if escolha == 0:
                system('cls')
                break

            if escolha == 1:
                system('cls')
                nome = input("Nome do anfíbio: ")
                cor = input("Cor do anfíbio: ")
                anfibio = Anfibio(nome, cor)
                self.__zoologico.adicionarAnimal(anfibio)
                
            elif escolha == 2:
                system('cls')
                nome = input("Nome do réptil: ")
                cor = input("Cor do réptil: ")
                reptil = Reptil(nome, cor)
                self.__zoologico.adicionarAnimal(reptil)
            
            elif escolha == 3:
                system('cls')
                nome = input("Nome da ave: ")
                cor = input("Cor da ave: ")
                envergadura = float(input("Envergadura(cm) da ave: "))
                ave = Ave(nome, cor, envergadura) if input("Esta ave nada? [s/n]: ").lower() == "n" else AveAquatica(nome, cor, envergadura)
                self.__zoologico.adicionarAnimal(ave) 
            
            else:
                system('cls')
                nome = input("Nome do mamífero: ")
                cor = input("Cor do mamífero: ")

                if input("Este mamífero voa? [s/n]: ").lower() == "s":
                    envergadura = float(input("Envergadura(cm) do mamífero: "))
                    mamifero = MamiferoVoador(nome, cor, envergadura)
                else:
                    mamifero = Mamifero(nome, cor)
                self.__zoologico.adicionarAnimal(mamifero)

    def menuVisitarAnimais(self):
        print("Quais animais deseja visitar?\n")
        opcoes = "\n1 - Anfíbios.\n2 - Répteis.\n3 - Aves.\n4 - Mamíferos.\n0 - Voltar.\n"

        escolha = 100      
        while escolha:
            escolha = escolha = Menu.escolherOpcao(opcoes, valor_min=0, valor_max=5)

            if escolha == 0:
                system('cls')
                break

            if escolha == 1:
                system('cls')
                anfibios = self.__zoologico.getAnfibios()
                if anfibios == []:
                    system('cls')
                    print("Não tem nenhum anfíbio neste zoológico.")
                    continue

                for anfibio in anfibios:
                    anfibio.fazerTruque()
                
            elif escolha == 2:
                system('cls')
                repteis = self.__zoologico.getRepteis()
                if repteis == []:
                    system('cls')
                    print("Não tem nenhum réptil neste zoológico.")
                    continue

                for reptil in repteis:
                    reptil.fazerTruque()

            elif escolha == 3:
                system('cls')
                aves = self.__zoologico.getAves()
                if aves == []:
                    system('cls')
                    print("Não tem nenhuma ave neste zoológico.")
                    continue

                for ave in aves:
                    if isinstance(ave, AveAquatica):
                        ave.nadar()
                    else:
                        ave.fazerTruque()
            
            else:
                system('cls')
                mamiferos = self.__zoologico.getMamiferos()
                if mamiferos == []:
                    system('cls')
                    print("Não tem nenhum mamífero neste zoológico.")
                    continue

                for mamifero in mamiferos:
                    if isinstance(mamifero, MamiferoVoador):
                        mamifero.voar()
                    else:
                        mamifero.fazerTruque()
