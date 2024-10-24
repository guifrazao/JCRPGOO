from datetime import datetime
import calendar

class Calendar:
    def __init__(self, ano, feriado_provider):
        self.__ano = ano
        self.__feriado_provider = feriado_provider
        self.__feriados = self.__feriado_provider.carregar_feriados(ano)

    def exibir_calendario(self, mes):
        print(calendar.month(self.__ano, mes))

    def verificar_feriado(self, data):
        try:
            data_usuario = datetime.strptime(data, "%d-%m-%Y")
            for feriado in self.__feriados:
                if data_usuario.date() == feriado.date():
                    return True
            return False
        except ValueError:
            print("Erro: Data inválida. O formato correto é DD-MM-AAAA.")
            return False

    @staticmethod
    def calcular_diferenca_dias(data1, data2):
        data1 = datetime.strptime(data1, "%d-%m-%Y")
        data2 = datetime.strptime(data2, "%d-%m-%Y")
        return abs((data2 - data1).days)

    def set_ano(self, novo_ano):
        self.__ano = novo_ano
        self.__feriados = self.__feriado_provider.carregar_feriados(novo_ano)
        print(f"Ano do calendário alterado para {novo_ano}.")

    def get_ano(self):
        return self.__ano
