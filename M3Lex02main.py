from M3Lex02 import Bicycle

def get_bicycle_data():
    while True:
        try:
            velocidade = float(input("Digite a velocidade da bicicleta (km/h): "))
            print("--"*30)
            cadencia = float(input("Digite a cadência da bicicleta (rotações por minuto): "))
            print("--"*30)
            marcha = int(input("Digite a marcha atual da bicicleta (entre 1 e 18): "))
            print("--"*30)
            serie = int(input("Digite o número de série da bicicleta (deve ser maior que 1000): "))
            print("--"*30)
            
            bike = Bicycle(0, 0, 1, 1000)
            
            bike.set_velocidade(velocidade)
            bike.set_cadencia(cadencia)
            bike.set_marcha(marcha)
            bike.set_serie(serie)
            
            return bike

        except ValueError as e:
            print(f"Erro: {e}. Por favor, tente novamente.")

print("Bicicleta 1:")
bike1 = get_bicycle_data()
print("=-"*30)

print("\nBicicleta 2:")
bike2 = get_bicycle_data()
print("=-"*30)

print("\nInformações da Bicicleta 1:")
print(bike1)
print("=-"*30)

print("\nInformações da Bicicleta 2:")
print(bike2)
print("=-"*30)

print(f"\nVelocidade relativa entre as bicicletas: {bike1.velocidade_relativa(bike2)} km/h")