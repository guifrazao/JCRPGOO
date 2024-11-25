from classesAuxiliares import *

class Test: 
    @staticmethod
    def main():
        # a. Assistente Administrativo e Técnico
        assistente = AssistenteAdministrativo("Maria", "12345", 3500, "Assistente Administrativo de RH")
        tecnico = Tecnico("João", "67890", 4000, "Redes")
        assistente.exibir_dados()
        tecnico.exibir_dados()
        print()

        # b. Cachorro e Gato
        cachorro = Cachorro("Luke")
        gato = Gato("Garfield")
        cachorro.latir()
        gato.miar()
        cachorro.caminhar()
        gato.caminhar()
        print(f"{cachorro.nome} come: {cachorro.comer()}")
        print(f"{gato.nome} come: {gato.comer()}")
        print()

        # c. Ingresso
        tipo_ingresso = int(input("Digite 1 para ingresso normal e 2 para VIP: "))
        if tipo_ingresso == 1:
            ingresso = Ticket(100)
            print("Ingresso Normal")
            print(f"Valor do ingresso: R$ {ingresso.get_valor():.2f}")
        elif tipo_ingresso == 2:
            tipo_vip = int(input("Digite 1 para Camarote Superior e 2 para Camarote Inferior: "))
            if tipo_vip == 1:
                ingresso = CamaroteSuperior(100, 50, 100)
                print("Ingresso VIP - Camarote Superior")
            else:
                ingresso = CamaroteInferior(100, 50)
                print("Ingresso VIP - Camarote Inferior")
            print(f"Valor do ingresso: R$ {ingresso.get_valor():.2f}")
        print()

        # d. Imóvel
        tipo_imovel = int(input("Digite 1 para imóvel novo e 2 para imóvel velho: "))
        if tipo_imovel == 1:
            imovel = NewProperty("Rua A, 123", 500000, 50000)
            print("Imóvel Novo")
        else:
            imovel = OldProperty("Rua B, 456", 400000, 30000)
            print("Imóvel Velho")
        print(f"Valor final do imóvel: R$ {imovel.get_preco():.2f}")

Test.main()


