from datetime import datetime
import calendar

class HolidayProvider:
    @staticmethod
    def carregar_feriados(ano):
        return [
            datetime(ano, 1, 1),    # Ano Novo
            datetime(ano, 2, 25),   # Carnaval (data variável)
            datetime(ano, 2, 26),   # Carnaval (data variável)
            datetime(ano, 4, 21),    # Tiradentes
            datetime(ano, 4, 19),   # Paixão de Cristo (data variável)
            datetime(ano, 5, 1),     # Dia do Trabalhador
            datetime(ano, 9, 7),     # Independência do Brasil
            datetime(ano, 10, 12),   # Nossa Senhora Aparecida
            datetime(ano, 11, 1),    # Dia de Todos os Santos
            datetime(ano, 11, 2),    # Dia de Finados
            datetime(ano, 11, 15),   # Proclamação da República
            datetime(ano, 12, 25),   # Natal
        ]