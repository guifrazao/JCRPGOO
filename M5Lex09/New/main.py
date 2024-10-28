from Modulos import *

def menu():
    validator_invoice = Validator_invoice()
    validator_owner = Validator_Owner()
    proprietario = None
    faturas = []

    while True:
        print("\n" + "=" * 50)
        print(" " * 12 + "✦ MENU PRINCIPAL ✦")
        print("=" * 50)
        print("1️⃣ Criar Proprietário")
        print("2️⃣ Criar Fatura")
        print("3️⃣ Mostrar Informações da Fatura")
        print("4️⃣ Sair")
        print("=" * 50)

        escolha = input("Digite sua escolha: ")

        if escolha == '1':
            proprietario = criar_proprietario(validator_owner)
            print("✔️ Proprietário criado com sucesso.")
        elif escolha == '2':
            if proprietario is None:
                print("⚠️ Primeiro, crie um proprietário para associar a fatura.")
            else:
                fatura = criar_invoice(validator_invoice, proprietario)
                faturas.append(fatura)
                print("✔️ Fatura criada e associada ao proprietário com sucesso.")
        elif escolha == '3':
            if not faturas:
                print("⚠️ Nenhuma fatura disponível.")
            else:
                print("\n" + "=" * 50)
                print(" " * 12 + "✦ INFORMAÇÕES DAS FATURAS ✦")
                print("=" * 50)
                for index, fatura in enumerate(faturas):
                    print(f"\nFatura {index + 1}:")
                    print(fatura)
                    total = fatura.calculate_total()
                    print(f"💰 Valor total da fatura: R${total:.2f}")
                print("=" * 50)
        elif escolha == '4':
            print("👋 Saindo...")
            break
        else:
            print("❌ Escolha inválida. Tente novamente.")

def main():
    menu()

if __name__ == "__main__":
    main()
