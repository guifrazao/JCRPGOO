"""
25. Foi realizada uma pesquisa de algumas características físicas da população de uma
certa região, a qual foram coletados os seguintes dados referentes a cada habitante
para serem analisados:
• Sexo.
• Cor dos olhos (azuis, verdes, castanhos).
• Cor dos cabelos (louros, castanhos, pretos).
• Idade.
Faça um programa que determine e escreva:
a. O total de entrevistados
b. O total de homens e o total de mulheres entrevistados
c. A maior e a menor idade do conjunto de habitantes;
d. A média de idade do conjunto de habitantes;
e. A percentagem de indivíduos de sexo feminino cuja idade está entre 18 e 35
anos inclusive e que tenham olhos verdes e cabelos louros.
O final do conjunto de habitantes é reconhecido pelo valor -1 para a idade.
"""


    

def main():
    total_hab = 0 
    total_h = 0
    total_f = 0
    maior_idade = 0
    menor_idade = 0
    total_idades = 0
    requisito_e = 0.0
    try:       
        while True:
            sexo = -1
            cor_olho = -1
            cor_cabelo = -1
            idade = -2
            while sexo < 0 or sexo > 1:
                sexo = int(input("Informe o seu sexo (0 - Masculino, 1 - Feminino): "))
            while cor_olho < 0 or cor_olho > 2:
                cor_olho = int(input("Informe a cor de seus olhos (0 - Azuis, 1 - Verdes, 2 - Castanhos): "))
            while cor_cabelo < 0 or cor_cabelo > 2:
                cor_cabelo = int(input("Informe a cor de seus cabelos (0 - Louros, 1 - Castanhos, 2 - Pretos): "))
            while idade < -1:
                idade = int(input("Informe sua idade (Digite -1 para sair do programa): "))
            if idade == -1:
                break

            total_hab += 1
            total_idades += idade

            if sexo == 0:
                total_h += 1
            else:
                total_f += 1
            
            if idade > maior_idade:
                maior_idade = idade
            elif idade < menor_idade:
                menor_idade = idade
            
            if sexo == 1:
                if idade >= 18 and idade <= 35:
                    if cor_olho == 1 and cor_cabelo == 0:
                        requisito_e += 1
        
        if total_hab == 0:
            raise Exception("Nenhum habitante registrado")
        print("=" * 80 + "\n")
        print(f"Total de habitantes: {total_hab}")
        print(f"Total de habitantes do sexo masculino: {total_h}")
        print(f"Total de habitantes do sexo feminino: {total_f}")
        print(f"Maior idade registrada: {maior_idade}")
        print(f"Menor idade registrada: {menor_idade}")
        print(f"Média das idades dos habitantes: {total_idades/total_hab:.2f}")
        print(f"percentagem de indivíduos de sexo feminino cuja idade está entre 18 e 35 anos e que tenham olhos verdes e cabelos louros: {(requisito_e/total_hab)*100:.2f}%")
    except ValueError:
        print("Dado(s) inválido(s), fim do programa")
    except Exception as e:
        print(f"Erro fatal: {e}")

main()
            