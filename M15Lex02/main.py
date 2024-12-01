from interfaces import INadador, IVoador, IAnimal
from familias_animais import Anfibio, Reptil, Ave, Mamifero
from animais_especiais import AveAquatica, MamiferoVoador
from menu import Menu

def main():
    IAnimal.register(Anfibio)
    IAnimal.register(Reptil)
    IAnimal.register(Ave)
    IAnimal.register(Mamifero)
    
    INadador.register(AveAquatica)
    IVoador.register(MamiferoVoador)
    menu = Menu()
    menu.menuPrincipal()

main()
