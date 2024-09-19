"""
Em um sistema de ensino experimental em 10 níveis, o aluno é submetido a
exercícios sobre o mesmo assunto até que ele alcance a nota máxima (100 pontos),
para só então passar ao assunto seguinte. Entretanto, se após 5 tentativas no mesmo
nível o aluno obtiver menos de 300 pontos acumulados ele retorna ao nível anterior.
Caso contrário, ele permanece no mesmo nível, zerando novamente os pontos
acumulados. Faça um programa que compute o progresso do aluno, através da
leitura de suas notas até que ele termine o 10° nível. Utilize o comando break (por
exemplo, para passar ao próximo nível e recomeçar quando o aluno tiver tirado a nota
máxima).
"""
def verificar_entrada(mensagem):
    """Função para validar a entrada de notas do aluno."""
    while True:
        try:
            nota = int(input(mensagem))
            if 0 <= nota <= 100:
                return nota
            else:
                print("Nota inválida! Digite um valor entre 0 e 100.")
                print("=-"*30)
        except ValueError:
            print("ERROR FATAL! Insira um valor numérico válido.")
            print("=-"*30)

def loop_tentativas():
    """Loop para gerenciar tentativas dentro de um nível específico."""
    tentativas = 0
    pontos_acumulados = 0

    while tentativas < 5:
        nota = verificar_entrada(f"Tentativa {tentativas + 1} - Digite sua nota: ")
        print("--"*30)
        pontos_acumulados += nota
        tentativas += 1

        if nota == 100:
            print("Nota máxima alcançada! Avançando para o próximo nível.")
            print("=-"*30)
            return 'avancar', pontos_acumulados
            #break

    if pontos_acumulados < 300:
        return 'retroceder', pontos_acumulados
    else:
        return 'permanecer', pontos_acumulados

def loop_niveis():
    """Loop para gerenciar os 10 níveis do sistema de ensino."""
    nivel = 1 

    while nivel <= 10:
        print(f"\n*** Nível {nivel} ***")
        resultado, pontos = loop_tentativas(nivel)

        if resultado == 'avancar':
            nivel += 1
        elif resultado == 'retroceder':
            if nivel > 1:
                nivel -= 1
                print(f"Menos de 300 pontos acumulados. Retornando ao Nível {nivel}.")
                print("=-"*30)
            else:
                print("Menos de 300 pontos acumulados. Permanece no Nível 1.")
                print("=-"*30)
        else:
            print(f"Você acumulou {pontos} pontos. Continue no mesmo nível.")
            print("=-"*30)


    print("\nParabéns! Você completou todos os 10 níveis.")

def main():
    loop_niveis()

main()
