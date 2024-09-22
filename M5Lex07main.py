from M5Lex07 import Calendar,CalendarUI,HolidayProvider

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
    
    feriado_provider = HolidayProvider()
    calendario = Calendar(ano, feriado_provider)
    
    ui = CalendarUI(calendario)
    ui.executar()

main()
