"""
Implemente um sistema de Concessionária com os tipos de veículos (automóvel,
moto, caminhão, etc.), evidenciando a classe Vehicle como uma classe abstrata.
"""
from caminhao import Caminhao
from moto import Moto
from automovel import Automovel

def main():
    veiculos = [
        Automovel("Toyota", "Corolla", 2020, 20000),
        Moto("Honda", "CBR500R", 2019, 7000),
        Caminhao("Volvo", "FH", 2018, 75000)
    ]

    print("CATÁLOGO DE VEÍCULOS:\n")
    for veiculo in veiculos:
        print(f"Tipo: {veiculo.get_vehicle_type()}")
        print(veiculo)
        print("=-"*30)

main()
