"""
Crie uma classe chamada Calendar que represente um calendário anual. Essa classe
deve ter métodos para exibir o calendário de um determinado mês, verificar se uma
data é feriado e calcular a diferença de dias entre duas datas.
"""

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


class CalendarUI:
    def __init__(self, calendario):
        self.calendario = calendario

    def menu(self):
        print("""
Escolha uma opção:
1 - Exibir o calendário de um mês
2 - Verificar se uma data é feriado
3 - Calcular a diferença de dias entre duas datas
4 - Mudar o ano do calendário
5 - Sair
""")
        print("=-"*30)
        while True:
            try:
                opcao = int(input("Digite a opção desejada: "))
                print("=-"*30)
                if opcao not in range(1, 6):
                    raise ValueError("Opção inválida. Escolha um número entre 1 e 5.")
                return opcao
            except ValueError as e:
                print(f"Erro: {e}. Tente novamente.")
                

    def executar(self):
        while True:
            opcao = self.menu()

            if opcao == 1:
                while True:
                    try:
                        mes = int(input("Digite o número do mês (1-12): "))
                        print("=-"*30)
                        if mes < 1 or mes > 12:
                            raise ValueError("Mês deve estar entre 1 e 12.")
                        self.calendario.exibir_calendario(mes)
                        break
                    except ValueError as e:
                        print(f"Erro: {e}. Tente novamente.")
                        

            elif opcao == 2:
                while True:
                    data = input("Digite a data (DD-MM-AAAA): ")
                    print("--"*30)
                    if self.calendario.verificar_feriado(data):
                        print(f"A data {data} é um feriado.")
                        print("=-"*30)
                    else:
                        print(f"A data {data} não é um feriado.")
                        print("--"*30)
                    break

            elif opcao == 3:
                while True:
                    try:
                        data1 = input("Digite a primeira data (DD-MM-AAAA): ")
                        print("--"*30)
                        data2 = input("Digite a segunda data (DD-MM-AAAA): ")
                        print("--"*30)
                        datetime.strptime(data1, "%d-%m-%Y")
                        datetime.strptime(data2, "%d-%m-%Y")
                        diferenca = Calendar.calcular_diferenca_dias(data1, data2)
                        if diferenca < 0:
                            raise ValueError("As datas devem ser válidas e resultarem em diferença positiva.")
                        print(f"A diferença entre as datas é de {diferenca} dias.")
                        
                        break
                    except ValueError:
                        print("Erro: Certifique-se de que ambas as datas estão no formato correto DD-MM-AAAA e que são válidas.")
                        

            elif opcao == 4:
                while True:
                    try:
                        novo_ano = int(input("Digite o novo ano: "))
                        print("=-"*30)
                        if novo_ano <= 0:
                            raise ValueError("O ano deve ser maior que zero.")
                        
                        self.calendario.set_ano(novo_ano)
                        break
                    except ValueError as e:
                        print(f"Erro: {e}. O ano deve ser um número positivo. Tente novamente.")
                        

            elif opcao == 5:
                print("Saindo...")
                break

