from modules import *

def main():
    vehicle = None
    owner = None

    while True:
        print("\nMenu:")
        print("1. Create Vehicle")
        print("2. Create Owner")
        print("3. Associate Vehicle and Owner")
        print("4. Show Vehicle and Owner Info")
        print("5. Indicate Vehicle Speed")
        print("6. Enter the Vehicle")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            current_speed = float(input("Enter the current speed (km/h): "))
            direction = float(input("Enter the direction (°): "))
            vehicle = Vehicle(current_speed, direction)
            print("Vehicle created successfully.")
        elif choice == '2':
            name = input("Enter the owner's name: ")
            owner = Owner(name)
            print("Owner created successfully.")
        elif choice == '3':
            if vehicle and owner:
                owner.set_vehicle(vehicle)
                vehicle.set_owner(owner)
                print("Vehicle and Owner associated successfully.")
            else:
                print("You need to create both a vehicle and an owner first.")
        elif choice == '4':
            if vehicle and owner:
                print("\nVehicle Info:")
                vehicle_owner = vehicle.get_owner()
                if vehicle_owner:
                    vehicle_owner.introduce_yourself()
                else:
                    print("No owner associated with the vehicle.")
                print(f"Current Speed: {vehicle.get_current_speed()} km/h")
                print(f"Direction: {vehicle.get_direction()}°")

                print("\nOwner Info:")
                owner_vehicle = owner.get_vehicle()
                if owner_vehicle:
                    print(f"Owner's Vehicle Current Speed: {owner_vehicle.get_current_speed()} km/h")
                else:
                    print("No vehicle associated with the owner.")
            else:
                print("You need to create and associate both a vehicle and an owner first.")
        elif choice == '5':
            if owner and vehicle:
                owner.indicate_the_vehicle_speed(vehicle)
            else:
                print("You need to create and associate both a vehicle and an owner first.")
        elif choice == '6':
            if owner and vehicle:
                owner.enter_the_vehicle(vehicle)
            else:
                print("You need to create and associate both a vehicle and an owner first.")
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

main()
