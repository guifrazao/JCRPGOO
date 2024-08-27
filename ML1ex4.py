"""
4. Faça um programa que calcule o valor total da venda de uma mercadoria, qualquer
que seja o número de unidades vendidas e o valor da mercadoria.
"""

def calcular_venda(qtd_protudo, valor_produto):
    return qtd_protudo * valor_produto


def main():
    total = calcular_venda(32, 5)
    print(total)
    
main()
