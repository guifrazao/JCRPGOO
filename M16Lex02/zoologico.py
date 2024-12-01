from interfaces import IAnimal
from familias_animais import Anfibio, Reptil, Ave, Mamifero

class Zoologico:
    def __init__(self):
        self.__animais = []

    def getAnimais(self):
        return self.__animais

    def adicionarAnimal(self, animal: IAnimal):
        self.__animais.append(animal)

    def getRepteis(self):
        repteis = []
        for animal in self.__animais:
            if isinstance(animal, Reptil):
                repteis.append(animal)
        return repteis
    
    def getAves(self):
        aves = []
        for animal in self.__animais:
            if isinstance(animal, Ave):
                aves.append(animal)
        return aves
    
    def getMamiferos(self):
        mamiferos = []
        for animal in self.__animais:
            if isinstance(animal, Mamifero):
                mamiferos.append(animal)
        return mamiferos
    
    def getAnfibios(self):
        anfibios = []
        for animal in self.__animais:
            if isinstance(animal, Anfibio):
                anfibios.append(animal)
        return anfibios

    def imprimirInformacoesMamiferos(self):
        for animal in self.__animais:
            if isinstance(animal, Mamifero):
                animal.imprimirInformacoes()
                print()

    def imprimirInformacoesAves(self):
        for animal in self.__animais:
            if isinstance(animal, Ave):
                animal.imprimirInformacoes()
                print()

    def imprimirInformacoesRepteis(self):
        for animal in self.__animais:
            if isinstance(animal, Reptil):
                animal.imprimirInformacoes()
                print()

    def imprimirInformacoesAnfibios(self):
        for animal in self.__animais:
            if isinstance(animal, Anfibio):
                animal.imprimirInformacoes()
                print()

    def temEsteTipo(self, tipo):
        for animal in self.__animais:
            if isinstance(animal, tipo):
                return True
        return False

    @staticmethod
    def imprimirInformacoesAnimal(animal: IAnimal):
        animal.imprimirInformacoes()