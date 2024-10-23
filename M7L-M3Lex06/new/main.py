from point import Point
from circle import Circle
from circle_extra_actions import CircleCircumference

def main():
    circle = None

    def create_circle():
        x = float(input("Enter x coordinate for the center point: "))
        y = float(input("Enter y coordinate for the center point: "))
        radius = float(input("Enter radius for the circle: "))
        center = Point(x, y)
        return Circle(center, radius)

    while True:
        print("\nMenu:")
        print("1. Create Circle")
        print("2. Move Circle")
        print("3. Calculate Circle Area")
        print("4. Get Circle Data")
        print("5. Set Circle Radius")
        print("6. Calculate Circle Circumference")
        print("7. Exit")
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
                center = circle.get_center()
                data = f"Center: ({center.get_x()}, {center.get_y()}), Radius: {circle.get_radius()}"
                print(data)
            else:
                print("No circle created yet.")
        elif choice == '5':
            if circle:
                radius = float(input("Enter new radius for the circle: "))
                circle.set_radius(radius)
                print("Radius updated successfully.")
            else:
                print("No circle created yet.")
        elif choice == '6':
            if circle:
                circumference_action = CircleCircumference(circle)
                circumference = circle.perform_extra_action(circumference_action)
                print(f"The circumference of the circle is: {circumference:.2f}")
            else:
                print("No circle created yet.")
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

main()
