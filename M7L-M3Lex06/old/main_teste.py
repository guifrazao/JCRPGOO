from point import Point
from circle import Circle

def main():
    def create_point():
        x = float(input("Enter x coordinate for the point: "))
        y = float(input("Enter y coordinate for the point: "))
        return Point(x, y)

    def create_circle():
        center = create_point()
        radius = float(input("Enter radius for the circle: "))
        return Circle(center, radius)

    circle = None

    while True:
        print("\nMenu:")
        print("1. Create Circle")
        print("2. Move Circle")
        print("3. Calculate Circle Area")
        print("4. Get Circle Data")
        print("5. Set Circle Radius")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            circle = create_circle()
            print("Circle created successfully.")
        elif choice == '2':
            if circle:
                dx = float(input("Enter dx to move the circle: "))
                dy = float(input("Enter dy to move the circle: "))
                circle.move(dx, dy)
            else:
                print("No circle created yet.")
        elif choice == '3':
            if circle:
                area = circle.area()
                print(f"The area of the circle is: {area:.2f}")
            else:
                print("No circle created yet.")
        elif choice == '4':
            if circle:
                print(circle.get_circle_data())
            else:
                print("No circle created yet.")
        elif choice == '5':
            if circle:
                radius = float(input("Enter new radius for the circle: "))
                circle.set_radius(radius)
            else:
                print("No circle created yet.")
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

main()
