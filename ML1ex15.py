"""
15. Faça um programa que leia do teclado as 3 notas bimestrais de um aluno, calcule a
média e imprima se o aluno está aprovado ou vai para a prova final, sendo a média
para aprovação igual a 7.
"""

def definir_aprovacao(notas):
    media = sum(notas)/len(notas)
    if media >= 7.0:
        return "O aluno está aprovado"
    return "O aluno irá para a prova final"

def verificar_notas(notas):
    for i in range(len(notas)):
        if notas[i] < 0.0 or notas[i] > 10.0:
            raise Exception("Nota(s) devem ser entre zero e dez, fim do programa")
    return True

def main():
    try:
        notas = [float(input(f"Digite a {i+1}° nota: ")) for i in range(3)]
        if verificar_notas(notas):
            print(definir_aprovacao(notas))
    except ValueError:
        print("Dado(s) inválido(s), fim do programa")
    except Exception as e:
        print(f"Erro fatal: {e}")
main()
