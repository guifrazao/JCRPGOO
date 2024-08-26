def calcular_venda(qtd_protudo, valor_produto):
    return qtd_protudo * valor_produto


def main():
    total = calcular_venda(32, 5)
    print(total)
    
main()
