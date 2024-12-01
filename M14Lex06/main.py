from menu import Menu
from estudantes import EnsinoMedio, Graduacao, Mestrado, Doutorado
from interfaces import IEntregaTrabalho

def main():
    IEntregaTrabalho.register(Graduacao)
    IEntregaTrabalho.register(Mestrado)
    IEntregaTrabalho.register(Doutorado)
    menu = Menu()
    menu.menuPrincipal()

main()