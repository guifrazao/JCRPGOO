from vehicle import Vehicle
from car import Car
from motorcycle import Motorcycle

def create_vehicle():
    current_speed = input("Enter the current speed: ")
    direction = input("Enter the direction: ")
    owner = input("Enter the owner: ")
    return Vehicle(current_speed, direction, owner)

def main():
    my_vehicle = create_vehicle()
    car = None
    motorcycle = None

    while True:
        print("\nMenu:")
        print("1. Show current speed")
        print("2. Set current speed")
        print("3. Show direction")
        print("4. Set direction")
        print("5. Show owner")
        print("6. Set owner")
        print("7. Create Car")
        print("8. Create Motorcycle")
        print("9. Relate and show vehicle type")
        print("10. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print(my_vehicle.get_current_speed())
        elif choice == '2':
            speed = input("Enter new speed: ")
            my_vehicle.set_current_speed(speed)
        elif choice == '3':
            print(my_vehicle.get_direction())
        elif choice == '4':
            direction = input("Enter new direction: ")
            my_vehicle.set_direction(direction)
        elif choice == '5':
            print(my_vehicle.get_owner())
        elif choice == '6':
            owner = input("Enter new owner: ")
            my_vehicle.set_owner(owner)
        elif choice == '7':
            car = Car()
            print("Car created successfully!")
        elif choice == '8':
            motorcycle = Motorcycle()
            print("Motorcycle created successfully!")
        elif choice == '9':
            if car is None and motorcycle is None:
                print("No vehicle created. Please create a Car or Motorcycle first.")
            else:
                vehicle_choice = input("Enter 'car' or 'motorcycle': ")
                if vehicle_choice.lower() == 'car' and car is not None:
                    my_vehicle.show_type_vehicle(car)
                elif vehicle_choice.lower() == 'motorcycle' and motorcycle is not None:
                    my_vehicle.show_type_vehicle(motorcycle)
                else:
                    print("Invalid choice or vehicle not created. Please try again.")
        elif choice == '10':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()