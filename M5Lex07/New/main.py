"""
Refazer as listas M3L e M5L, aplicando o Princípio Aberto-Fechado e mostrar as diferenças
de seu código, antes e depois.

Crie uma classe chamada Calendar que represente um calendário anual. Essa classe
deve ter métodos para exibir o calendário de um determinado mês, verificar se uma
data é feriado e calcular a diferença de dias entre duas datas.
"""

from BrazilianHolidayStrategy import BrazilianHolidayProvider
from HolidayProvider import HolidayProvider
from Calendar import Calendar
from CalendarUI import CalendarUI

def main():
    while True:
        try:
            ano = int(input("Digite o ano do calendário: "))
            print("=-"*30)
            if ano > 0:
                break
            else:
                print("Valor inválido! Tente novamente")
        except ValueError:
            print("Erro: O ano deve ser um número inteiro. Tente novamente.")

    feriado_provider = HolidayProvider(BrazilianHolidayProvider().carregar_feriados)
    calendario = Calendar(ano, feriado_provider)
    ui = CalendarUI(calendario)
    ui.executar()

main()
