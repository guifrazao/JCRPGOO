from point import Point

    # Cria uma instância da classe Point
p1 = Point()  # O ponto será inicializado em (1, 1)
    # Movimenta o ponto
p1.move(3, 4)  # O ponto se move para (4, 5)
    # Cria um segundo ponto
p2 = Point(6, 8)
    # Move o segundo ponto
p2.move(2, 3)  # O segundo ponto se move para (8, 11)
    # Calcula a distância entre os dois pontos
p1.distance(p2)
    # Atualiza as coordenadas do primeiro ponto
p2.set_values(6, 8)
    # Move o primeiro ponto para testar a atualização
p1.move(-1, -1)  # O ponto se move de (4, 5) para (3, 4)