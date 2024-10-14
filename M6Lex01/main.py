from owner import Owner
from vehicle import Vehicle

def getOwnerData():
    while True:
        try:
            name = str(input("\nEnter the owner's name: "))
            age = int(input("Enter your age: "))
            cpf = str(input("Enter your CPF: "))

            return Owner(name, age, cpf)
        
        except Exception as err:
            print(f"Error: {err}")
            
def getVehicleData(owner):
    while True:
        try:
            current_speed = int(input(("\nCurrent speed(km/h): ")))
            direction = int(input(("Tire direction[-45°/45°]: ")))

            return Vehicle(current_speed, direction, owner)
        
        except Exception as err:
            print(f"Error: {err}")

def menu():
    choice = -1
    print()
    print(" MENU ".center(30, "="))
    print("[1] - View owner data\n[2] - View vehicle data\n[3] - Change vehicle owner\n[4] - Edit vehicle data\n[5] - Exit program")
    print("="*30)
    while choice < 1 or choice > 5:
        choice = int(input("Enter your choice: "))
    return choice

def main():
    owner = getOwnerData()
    vehicle = getVehicleData(owner)
    while True:
        choice = menu()
        if choice == 1:
            print(owner)
        elif choice == 2:
            print(vehicle)
        elif choice == 3:
            new_owner = vehicle.getOwner()
            new_name = str(input("\nNew name: "))
            new_age = int(input("New age: "))
            new_cpf = str(input("New cpf: "))
            new_owner.setName(new_name)
            new_owner.setAge(new_age)
            new_owner.setCPF(new_cpf)
        elif choice == 4:
            vehicle = getVehicleData(owner)
        else:
            print("\nEXITING PROGRAM...")
            break

main()
