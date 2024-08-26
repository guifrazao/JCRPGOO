def calcular_media(notas):
    return sum(notas)/len(notas)

def main():
    try:
        notas = []
        notas.append(float(input(f"Digite a {i}³ nota: ")) for i in range(0, 3))
        print(notas[0])
    except Exception as e:
        print(f"Erro fatal: {e}")
main()