from menu import Menu
from estudantes import EnsinoMedio, Graduacao, Mestrado, Doutorado
from interfaces import IEntregaTrabalho, IEnviaParaBanca

def main():
    IEntregaTrabalho.register(Graduacao)
    IEntregaTrabalho.register(Mestrado)
    IEntregaTrabalho.register(Doutorado)

    IEnviaParaBanca.register(Graduacao)
    IEnviaParaBanca.register(Mestrado)
    
    menu = Menu()
    menu.menuPrincipal()

main()