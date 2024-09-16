"""
Numa universidade, o sistema de avaliação é o seguinte: para passar direto, o aluno
precisa ter média do período (mp) igual ou superior a 7 pontos. Caso contrário, o
aluno será submetido a exame final, sendo a sua média final (mf) calculada pela
seguinte fórmula: mf = 0.6mp + 0.4ne, onde ne é a nota do exame. Essa média final
deverá então ser igual ou superior a 5 pontos para que o aluno seja aprovado. Por
outro lado, a média do período é calculada através da média das notas dos créditos,
cujo número é diferente para cada disciplina. Faça um programa que leia do usuário o
número de créditos da disciplina, as notas dos créditos, e se necessário calcule a
nota que o aluno precisa tirar no exame final para ser aprovado. Se antes de terminar
todos os créditos o aluno já estiver aprovado, avise isso a ele e encerre a leitura de
notas (utilize aqui um comando break).
"""
def calcular_m(total_notas,total_creditos): 
    return total_notas/total_creditos

def calcular_nef(media_periodo):
    return (5 - 0.6 * media_periodo) / 0.4

def calcular_mf(media_periodo,nota_ef):
    return 0.6 * media_periodo + 0.4 * nota_ef

def entrada_notas():
    total_notas = total_creditos = 0

    while True:
        creditos = verificar_inteiro("Digite o número de créditos da disciplina: ")
        nota = verificar_float("Digite a nota da disciplina: ")

        total_notas += nota * creditos
        total_creditos += creditos
        media_periodo = calcular_m(total_notas, total_creditos)

        print(f"Média do período até agora: {media_periodo:.2f}")

        if media_periodo >= 7:
            print(f"Aluno aprovado diretamente! Média do período: {media_periodo:.2f}")
            return media_periodo, None

        continuar = input("Deseja lançar mais notas? [S/N]: ").strip().upper()[0]
        if continuar == 'S':
            return media_periodo, None
        
def exame_final(media_perido):
    nota_necessaria = calcular_nef(media_perido)
    print(f"O aluno precisa tirar {nota_necessaria} no exame final para passar")

    nota_ef = verificar_float("Digite a nota do Exame Final: ")
    media_final = calcular_mf(media_perido, nota_ef)

    return "Aluno APROVADO" if media_final > 5 else "Aluno REPROVADO"

def verificar_float(mensagem):
    while True:
        try:
            nota = float(input(mensagem))
            if nota < 0:
                print("Valor inválido! Tente novamente")
            else:
                return nota
        except ValueError:
            print("Entrada INVÁLIDA! Por favor, insira um número válido")

def verificar_inteiro(mensagem):
    while True:
        try:
            nota = int(input(mensagem))
            if nota < 0:
                print("ERRO! Insira um valor positivo")
            else:
                return nota
        except ValueError:
            print("Entrada INVÁLIDA! Por favor, insira um número inteiro")
        
def main():
    media_periodo,_ = entrada_notas()

    if media_periodo < 7:
        print(exame_final(media_periodo))


main()
