from vehicle import Vehicle

vehicle = Vehicle(current_speed="100", direction="0", owner="Gui Frazao")

print(vehicle.get_current_speed())  
print(vehicle.get_direction())      
print(vehicle.get_owner())          

vehicle_type = int(input("Vehicle type([1] - Car [2] - Motorcycle): "))
vehicle.type_vehicle(vehicle_type)
