class HolidayProvider:
    def __init__(self, carregar_feriados_func):
        self.carregar_feriados_func = carregar_feriados_func

    def carregar_feriados(self, ano):
        return self.carregar_feriados_func(ano)

