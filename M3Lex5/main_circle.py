from circle import Circle

def main():
    circulo = Circle()
    
    print(circulo) 
    print("Área:", circulo.area()) 
    
    circulo.move(3, 4)
    print(circulo)  
    
    circulo.set_radius(10)
    print("\nNovo raio:", circulo.get_radius())  
    print(f"Nova área: {circulo.area():.2f}") 

main()

'''help(Circle)'''