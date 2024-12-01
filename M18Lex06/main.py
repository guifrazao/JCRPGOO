from menu import Menu
from estudantes import *
from interfaces import IEstudante, IEntregaTrabalho, IEnviaParaBanca

def main():
    IEstudante.register(EnsinoMedio)
    IEstudante.register(Graduacao)
    IEstudante.register(Mestrado)
    IEstudante.register(Doutorado)

    IEntregaTrabalho.register(Graduacao)
    IEntregaTrabalho.register(Mestrado)
    IEntregaTrabalho.register(Doutorado)

    IEnviaParaBanca.register(Graduacao)
    IEnviaParaBanca.register(Mestrado)

    menu = Menu()
    menu.menuPrincipal()

main()