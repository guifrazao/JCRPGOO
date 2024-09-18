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


    
def validar_entrada_int(msg):
    while True:
        try:
            valor_str = input(msg)
            valor_int = int(valor_str)
            return valor_int
        except ValueError:
            print(46*"=")
            print("ERRO! Informe um inteiro válido.")
            print(46*"=")
        
def coletar_dados():
    while True:
        sexo = -1
        cor_olho = -1
        cor_cabelo = -1
        idade = -2
        while idade < -1 and idade != 0:
            idade = validar_entrada_int("Informe sua idade (Digite -1 para sair do programa): ")
            if idade == -1:
                return [0, 0, 0, -1]
        while sexo < 0 or sexo > 1:
            sexo = validar_entrada_int("Informe o seu sexo (0 - Masculino, 1 - Feminino): ")
        while cor_olho < 0 or cor_olho > 2:
            cor_olho = validar_entrada_int("Informe a cor de seus olhos (0 - Azuis, 1 - Verdes, 2 - Castanhos): ")
        while cor_cabelo < 0 or cor_cabelo > 2:
            cor_cabelo = validar_entrada_int("Informe a cor de seus cabelos (0 - Louros, 1 - Castanhos, 2 - Pretos): ")        
        
        return sexo, cor_olho, cor_cabelo, idade
    
def processar_dados(dados_habitante, total_hab, total_h, total_m, total_idades, maior_idade, menor_idade, requisito_e):
    sexo, cor_olho, cor_cabelo, idade = dados_habitante[0], dados_habitante[1], dados_habitante[2], dados_habitante[3]

    total_hab += 1
    total_idades += dados_habitante[3]

    if sexo == 0:
        total_h += 1
    else:
        total_m += 1

    if dados_habitante[3] > maior_idade:
        maior_idade = dados_habitante[3]
    elif dados_habitante[3] < menor_idade:
        menor_idade = dados_habitante[3]
                  
    if sexo == 1:
        if idade >= 18 and idade <= 35:
            if cor_olho == 1 and cor_cabelo == 0:
                requisito_e += 1     
    
    return total_hab, total_h, total_m, total_idades, maior_idade, menor_idade, requisito_e

def main():
    total_hab = total_h = total_m = total_idades = requisito_e = 0
    maior_idade = 0
    menor_idade = 0
    while True:
        """coletar_dados() retorna [sexo, cor_olho, cor_cabelo, idade]"""
        dados_habitante = coletar_dados()
        if dados_habitante[3] == -1:
            break
        total_hab, total_h, total_m, total_idades, maior_idade, menor_idade, requisito_e = processar_dados(dados_habitante, 
                                                                                                           total_hab, 
                                                                                                           total_h, 
                                                                                                           total_m, 
                                                                                                           total_idades, 
                                                                                                           maior_idade, 
                                                                                                           menor_idade, 
                                                                                                           requisito_e)
    if total_hab == 0:
        print("Nenhum habitante registrado")
        exit()

    print("=" * 80 + "\n")
    print(f"Total de habitantes: {total_hab}")
    print(f"Total de habitantes do sexo masculino: {total_h}")
    print(f"Total de habitantes do sexo feminino: {total_m}")
    print(f"Maior idade registrada: {maior_idade}")
    print(f"Menor idade registrada: {menor_idade}")
    print(f"Média das idades dos habitantes: {total_idades/total_hab:.2f}")
    print(f"percentagem de indivíduos de sexo feminino cuja idade está entre 18 e 35 anos e que tenham olhos verdes e cabelos louros: {(requisito_e/total_hab)*100:.2f}%")

main()
            
