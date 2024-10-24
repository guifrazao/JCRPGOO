from vehicle import Vehicle
vehicle = Vehicle(current_speed="100", direction="0", owner="Carlão")

print(vehicle.get_current_speed())  
print(vehicle.get_direction())      
print(vehicle.get_owner())          

vehicle.set_current_speed("120")
vehicle.set_direction("45")
vehicle.set_owner("Gui Receba")

print(vehicle.get_current_speed()) 
print(vehicle.get_direction())      
print(vehicle.get_owner())         

help(Vehicle)