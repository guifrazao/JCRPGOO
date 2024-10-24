from datetime import datetime
from Calendar import Calendar

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
5 - Sair""")
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
                    if self.calendario.verificar_feriado(data) is not None:
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
