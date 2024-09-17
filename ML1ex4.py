"""
4. Desejando obter a média aritmética das idades dos alunos do curso de Odontologia,
do primeiro ano, do ano de 2023, construir um programa que leia, calcule e mostre a
média aritmética das idades. O programa é encerrado quando for lida uma idade igual
a zero e deve rejeitar idades negativas, pedindo que o usuário redigite.
"""
def media_aritmetica(valores):
    return sum(valores)/len(valores)

def main():
    idades = []
    media = 0.0
    try:
        while True:
            idade = -1
            while idade < 0:
                idade = int(input("Digite a idade do aluno: "))    
            if idade == 0:
                break                      
            idades.append(idade)
        if idades == []:
            raise Exception("A lista está vazia")
        
        media = media_aritmetica(idades)
        print(f"A média aritmética das idades é {media:.1f}")
    except Exception as e:
        print(f"Erro fatal: {e}")

main()
