from employee import Employee
from company import Company

def menu():
    print("\nMenu:")
    print("[1] - Add employee to company\n[2] - Remove employee from a company\n[3] - Show a company's information\n[4] - Show a company's employee list\n[5] - Exit")

    choice = -1
    while choice < 1 or choice > 5:
        choice = int(input())  
    return choice

def company_type_menu():
    print("[1] - IT\n[2] - Health\n[3] - Education\n[4] - Commerce\n[5] - Industry\n[6] - Services\n[7] - Agro"
          "\n[8] - Tourism and Hospitality\n[9] - Entertainment and Media\n[10] - Finances")

    choice = int(input("Company type: "))
    type_list = ["IT", "Health", "Education", "Commerce", "Industry", "Services", "Agro", 
                 "Tourism and Hospitality", "Entertainment and Media", "Finances"]
    
    if Company.verifyType(choice):
        return type_list[choice-1]
    else:
        print("Invalid type")
        company_type_menu()

def getCompanyData():
    try:
        name = input("Company's name: ")
        type = company_type_menu()
        cnpj = input("CNPJ: ") 

        return Company(name, type, cnpj)

    except Exception as err:
        print(f"Error: {err}")
        getEmployeeData()

def getEmployeeData():
    try:
        name = input("Name: ")
        surname = input("Surname: ")
        salary = float(input("Salary: $")) 

        return Employee(name, surname, salary)
    
    except Exception as err:
        print(f"Error: {err}")
        getEmployeeData()


def main():
    company = getCompanyData()
    while True:
        choice = menu()

        if choice == 1:
            employee = getEmployeeData()
            company.addEmployee(employee)

        elif choice == 2:
            name = input("Enter the employee's first name: ")
            employee = company.searchEmployeesByName(name)
            company.removeEmployee(employee)


        elif choice == 3:
            print(company)

        elif choice == 4:
            print(company.getEmployees())

        else:
            print("EXITING")
            exit()

main()


