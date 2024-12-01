from interfaces import INadador, IVoador
from animais_especiais import AveAquatica, MamiferoVoador
from menu import Menu

def main():
    INadador.register(AveAquatica)
    IVoador.register(MamiferoVoador)
    menu = Menu()
    menu.menuPrincipal()

main()
