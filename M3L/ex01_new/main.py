from vehicle import Vehicle
from engine import Engine

def create_engine():
    engine_type = input("\nEnter engine type: ")
    horsepower = int(input("Enter engine horsepower: "))
    return Engine(engine_type, horsepower)

def create_vehicle(engine: Engine):
    current_speed = input("\nEnter current speed (km/h): ")
    direction = input("Enter direction (degrees): ")
    owner = input("Enter owner's name: ")
    return Vehicle(current_speed, direction, owner, engine)

def view_engine_data(engine: Engine):
    print(f"\nEngine Type: {engine.get_type()}")
    print(f"Horsepower: {engine.get_horsepower()}")

def view_vehicle_data(vehicle: Vehicle):
    print(f"\nCurrent Speed: {vehicle.get_current_speed()}")
    print(f"Direction: {vehicle.get_direction()}")
    print(vehicle.get_owner())
    print(vehicle.get_engine_info())

def main():
    engine = None
    vehicle = None

    while True:
        print("\nMenu:")
        print("1. Create Engine")
        print("2. Create Vehicle")
        print("3. View Engine Data")
        print("4. View Vehicle Data")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            engine = create_engine()
            print("Engine created successfully.")
        elif choice == 2:
            vehicle = create_vehicle(engine)
            print("Vehicle created successfully.")
        elif choice == 3:
            if engine:
                view_engine_data(engine)
            else:
                print("No engine created yet.")
        elif choice == 4:
            if vehicle:
                view_vehicle_data(vehicle)
            else:
                print("No vehicle created yet.")
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

main()
