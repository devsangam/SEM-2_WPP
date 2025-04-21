from Shapes import Rectangle,Circle
rectangle = Rectangle()
circle = Circle()
choice = -1
while choice != 0:
    print("1.Square\n2.Circle\n0.Exit\n")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        inner_choice = -1
        while inner_choice != 0:
            print("\n1.Set length\n2.Print Perimeter\n3.Print Area\n0.Exit\n")
            inner_choice = int(input("Enter your choice: "))

            if inner_choice == 1:
                rectangle.length = float(input("\nEnter the length of Square: "))
                while rectangle.length < 0:
                    rectangle.length = float(input("Please enter a positive value: "))
                print("\nValue successfully updated!")

            elif inner_choice == 2:
                print(f"\nThe perimeter of rectangle is {rectangle.perimeter():.3f}")

            elif inner_choice == 3:
                print(f"\nThe area of rectangle is {rectangle.area():.3f}")

            elif inner_choice == 0:
                print("\nExiting rectangle...\n")
            
            else:
                print("\nPlease enter a valid number!")
    
    elif choice == 2:
        inner_choice = -1
        while inner_choice != 0:
            print("\n1.Set Radius\n2.Print Circumference(Perimeter)\n3.Print Area\n0.Exit\n")
            inner_choice = int(input("Enter your choice: "))

            if inner_choice == 1:
                circle.radius = float(input("\nEnter the radius of circle: "))
                while circle.radius < 0:
                    circle.radius = float(input("Please enter a positive value: "))
                print("\nValue successfully updated!")

            elif inner_choice == 2:
                print(f"\nThe perimeter of circle is {circle.perimeter():.3f}")

            elif inner_choice == 3:
                print(f"\nThe area of circle is {circle.area():.3f}")

            elif inner_choice == 0:
                print("\nExiting circle...\n")
            
            else:
                print("\nPlease enter a valid number!")

    elif choice == 0:
        print("Exiting the program...")

    else:
        print("\nPlease enter a valid number!\n")
exit(0)
