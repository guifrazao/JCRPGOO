from pessoa import Pessoa
from supplier import Supplier
from employee import Employee
from administrator import Administrator
from factory_worker import FactoryWorker
from seller import Seller

def criar_pessoa():
    name = input("\nDigite o nome: ")
    endereço = input("Digite o endereço: ")
    cpf = input("Digite o CPF: ")
    rg = input("Digite o RG: ")
    telefone = input("Digite o telefone: ")

    try:
        pessoa = Pessoa(name, endereço, cpf, rg, telefone)
        print("Pessoa criada com sucesso!\n")
        return pessoa
    except Exception as e:
        print(f"Erro ao criar pessoa: {e}")
        return None

def mostrar_detalhes_pessoa(pessoa):
    try:
        print(f"\nNome: {pessoa.get_name()}")
        print(f"Endereço: {pessoa.get_endereço()}")
        print(f"CPF: {pessoa.formatar_cpf()}")
        print(f"RG: {pessoa.formatar_rg()}")
        print(f"Telefone: {pessoa.formatar_telefone()}\n")
    except AttributeError:
        print("\nPessoa inválida. Por favor, crie uma pessoa primeiro.\n")
    except NameError:
        print("\nNenhuma pessoa foi criada ainda. Por favor, crie uma pessoa primeiro.\n")

def criar_supplier():
    name = input("\nDigite o nome: ")
    endereço = input("Digite o endereço: ")
    cpf = input("Digite o CPF: ")
    rg = input("Digite o RG: ")
    telefone = input("Digite o telefone: ")
    valueCredit = float(input("Digite o valor do crédito: $"))
    valueDebt = float(input("Digite o valor da dívida: $"))

    try:
        supplier = Supplier(name, endereço, cpf, rg, telefone, valueCredit, valueDebt)
        print("Supplier criado com sucesso!\n")
        return supplier
    except Exception as e:
        print(f"Erro ao criar supplier: {e}")
        return None

def mostrar_detalhes_supplier(supplier):
    try:
        print(f"\nNome: {supplier.get_name()}")
        print(f"Endereço: {supplier.get_endereço()}")
        print(f"CPF: {supplier.formatar_cpf()}")
        print(f"RG: {supplier.formatar_rg()}")
        print(f"Telefone: {supplier.formatar_telefone()}")
        print(f"Crédito: ${supplier.get_valueCredit()}")
        print(f"Dívida: ${supplier.get_valueDebt()}")
        print(f"Saldo: ${supplier.getBalance()}\n")
    except AttributeError:
        print("\nSupplier inválido. Por favor, crie um supplier primeiro.")
    except NameError:
        print("\nNenhum supplier foi criado ainda. Por favor, crie um supplier primeiro.")

def criar_employee():
    name = input("\nDigite o nome: ")
    endereço = input("Digite o endereço: ")
    cpf = input("Digite o CPF: ")
    rg = input("Digite o RG: ")
    telefone = input("Digite o telefone: ")
    sectorCode = int(input("Digite o código do setor: "))
    baseSalary = float(input("Digite o salário base: $"))
    tax = float(input("Digite o imposto(em porcentagem): ")) 

    try:
        employee = Employee(name, endereço, cpf, rg, telefone, sectorCode, baseSalary, tax)
        print("Employee criado com sucesso!\n")
        return employee
    except Exception as e:
        print(f"Erro ao criar employee: {e}")
        return None

def mostrar_detalhes_employee(employee):
    try:
        print(f"\nNome: {employee.get_name()}")
        print(f"Endereço: {employee.get_endereço()}")
        print(f"CPF: {employee.formatar_cpf()}")
        print(f"RG: {employee.formatar_rg()}")
        print(f"Telefone: {employee.formatar_telefone()}")
        print(f"Código do Setor: {employee.get_sectorCode()}")
        print(f"Salário Base: ${employee.get_baseSalary()}")
        print(f"Imposto: {employee.get_tax()}%")
        print(f"Salário Líquido: ${employee.calculateSalary()}\n")
    except AttributeError:
        print("\nEmployee inválido. Por favor, crie um employee primeiro.")
    except NameError:
        print("\nNenhum employee foi criado ainda. Por favor, crie um employee primeiro.")

def criar_administrator():
    name = input("\nDigite o nome: ")
    endereço = input("Digite o endereço: ")
    cpf = input("Digite o CPF: ")
    rg = input("Digite o RG: ")
    telefone = input("Digite o telefone: ")
    sectorCode = int(input("Digite o código do setor: "))
    baseSalary = float(input("Digite o salário base: $"))
    tax = float(input("Digite o imposto(em porcentagem): "))
    subsistenceAllowance = float(input("Digite o valor das ajudas de custo: $"))

    try:
        administrator = Administrator(name, endereço, cpf, rg, telefone, sectorCode, baseSalary, tax, subsistenceAllowance)
        print("Administrator criado com sucesso!\n")
        return administrator
    except Exception as e:
        print(f"Erro ao criar administrator: {e}")
        return None

def mostrar_detalhes_administrator(administrator):
    try:
        print(f"\nNome: {administrator.get_name()}")
        print(f"Endereço: {administrator.get_endereço()}")
        print(f"CPF: {administrator.formatar_cpf()}")
        print(f"RG: {administrator.formatar_rg()}")
        print(f"Telefone: {administrator.formatar_telefone()}")
        print(f"Código do Setor: {administrator.get_sectorCode()}")
        print(f"Salário Base: ${administrator.get_baseSalary()}")
        print(f"Imposto: {administrator.get_tax()}%")
        print(f"Ajudas de Custo: ${administrator.get_subsistenceAllowance()}")
        print(f"Salário Líquido (com ajudas de custo): ${administrator.calculateSalary()}\n")
    except AttributeError:
        print("\nAdministrator inválido. Por favor, crie um administrator primeiro.")
    except NameError:
        print("\nNenhum administrator foi criado ainda. Por favor, crie um administrator primeiro.")

def criar_factory_worker():
    name = input("\nDigite o nome: ")
    endereço = input("Digite o endereço: ")
    cpf = input("Digite o CPF: ")
    rg = input("Digite o RG: ")
    telefone = input("Digite o telefone: ")
    sectorCode = int(input("Digite o código do setor: "))
    baseSalary = float(input("Digite o salário base: $"))
    tax = float(input("Digite o imposto (em porcentagem): "))
    valueProduction = float(input("Digite o valor da produção: $"))
    commission = float(input("Digite a comissão (em porcentagem): "))

    try:
        factory_worker = FactoryWorker(name, endereço, cpf, rg, telefone, sectorCode, baseSalary, tax, valueProduction, commission)
        print("Factory Worker criado com sucesso!\n")
        return factory_worker
    except Exception as e:
        print(f"Erro ao criar factory worker: {e}")
        return None
    
def mostrar_detalhes_factory_worker(factory_worker):
    try:
        print(f"\nNome: {factory_worker.get_name()}")
        print(f"Endereço: {factory_worker.get_endereço()}")
        print(f"CPF: {factory_worker.formatar_cpf()}")
        print(f"RG: {factory_worker.formatar_rg()}")
        print(f"Telefone: {factory_worker.formatar_telefone()}")
        print(f"Código do Setor: {factory_worker.get_sectorCode()}")
        print(f"Salário Base: ${factory_worker.get_baseSalary()}")
        print(f"Imposto: {factory_worker.get_tax()}%")
        print(f"Valor da Produção: ${factory_worker.get_valueProduction()}")
        print(f"Comissão: {factory_worker.get_commission()}%")
        print(f"Salário Líquido (com comissão): ${factory_worker.calculateSalary()}\n")
    except AttributeError:
        print("\nFactory Worker inválido. Por favor, crie um factory worker primeiro.")
    except NameError:
        print("\nNenhum factory worker foi criado ainda. Por favor, crie um factory worker primeiro.")

def criar_seller():
    name = input("\nDigite o nome: ")
    endereço = input("Digite o endereço: ")
    cpf = input("Digite o CPF: ")
    rg = input("Digite o RG: ")
    telefone = input("Digite o telefone: ")
    sectorCode = int(input("Digite o código do setor: "))
    baseSalary = float(input("Digite o salário base: $"))
    tax = float(input("Digite o imposto (em porcentagem): "))
    valueSales = float(input("Digite o valor das vendas: $"))
    commission = float(input("Digite a comissão (em porcentagem): "))

    try:
        seller = Seller(name, endereço, cpf, rg, telefone, sectorCode, baseSalary, tax, valueSales, commission)
        print("Seller criado com sucesso!\n")
        return seller
    except Exception as e:
        print(f"Erro ao criar seller: {e}")
        return None
    
def mostrar_detalhes_seller(seller):
    try:
        print(f"\nNome: {seller.get_name()}")
        print(f"Endereço: {seller.get_endereço()}")
        print(f"CPF: {seller.formatar_cpf()}")
        print(f"RG: {seller.formatar_rg()}")
        print(f"Telefone: {seller.formatar_telefone()}")
        print(f"Código do Setor: {seller.get_sectorCode()}")
        print(f"Salário Base: ${seller.get_baseSalary()}")
        print(f"Imposto: {seller.get_tax()}%")
        print(f"Valor das Vendas: ${seller.get_valueSales()}")
        print(f"Comissão: {seller.get_commission()}%")
        print(f"Salário Líquido (com comissão): ${seller.calculateSalary()}\n")
    except AttributeError:
        print("\nSeller inválido. Por favor, crie um seller primeiro.")
    except NameError:
        print("\nNenhum seller foi criado ainda. Por favor, crie um seller primeiro.")

def exibir_menu():
    print("Menu")
    print("1. Criar nova pessoa")
    print("2. Mostrar detalhes da pessoa")
    print("3. Criar novo supplier")
    print("4. Mostrar detalhes do supplier")
    print("5. Criar novo employee")
    print("6. Mostrar detalhes do employee")
    print("7. Criar novo administrator")
    print("8. Mostrar detalhes do administrator")
    print("9. Criar novo factory worker")
    print("10. Mostrar detalhes do factory worker")
    print("11. Criar novo seller")
    print("12. Mostrar detalhes do seller")
    print("13. Sair")
    choice = input("Escolha uma opção: ")
    return choice

def main():
    pessoa = None
    supplier = None
    employee = None
    administrator = None
    factory_worker = None
    seller = None

    while True:
        choice = exibir_menu()

        if choice == "1":
            pessoa = criar_pessoa()
        elif choice == "2":
            mostrar_detalhes_pessoa(pessoa)
        elif choice == "3":
            supplier = criar_supplier()
        elif choice == "4":
            mostrar_detalhes_supplier(supplier)
        elif choice == "5":
            employee = criar_employee()
        elif choice == "6":
            mostrar_detalhes_employee(employee)
        elif choice == "7":
            administrator = criar_administrator()
        elif choice == "8":
            mostrar_detalhes_administrator(administrator)
        elif choice == "9":
            factory_worker = criar_factory_worker
        elif choice == "10":
            mostrar_detalhes_factory_worker(factory_worker)
        elif choice == "11":
            seller = criar_seller()
        elif choice == "12":
            mostrar_detalhes_seller(seller)
        elif choice == "13":
            print("\nSaindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

main()
