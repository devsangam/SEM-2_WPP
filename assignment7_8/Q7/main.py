
class except2d3d(Exception):
    pass

try:
    choice = input("type 2D to operate on 2D vectors 3D to operate on 3D vectors: ").lower()
    if choice != "2d" and choice !="3d":
        raise except2d3d("Invalid Input")
except except2d3d as e:
    print(e)
if choice=="2d":
    from vectors import Vector2D
    obj = Vector2D(int(input("Enter X coordinate: ")),int(input("Enter Y coordinate: ")))
    option = -1
    while option!=0:
        option = int(input("1 for magnitude\n2 for angle with x axis\n3 for distance with other point\n4 for dot product\n5 for cross product\n6 to display\n0 to Exit\n"))
        if option == 1:
            print(obj.magnitude())
        elif option==2:
            print(obj.angle_with_x_axis())
        elif option==3:
            print("Enter Information for other point...")
            obj1 = Vector2D(int(input("Enter X coordinate: ")),int(input("Enter Y coordinate: ")))
            print(obj.distance(obj1))
        elif option==4:
            print("Enter Information for other point...")
            obj1 = Vector2D(int(input("Enter X coordinate: ")),int(input("Enter Y coordinate: ")))
            print(obj.dot_product(obj1))
        elif option==5:
            print("Enter Information for other point...")
            obj1 = Vector2D(int(input("Enter X coordinate: ")),int(input("Enter Y coordinate: ")))
            print(obj.cross_product(obj1))
        elif option==6:
            print(obj.__repr__)
        elif option==0:
            exit()
        else:
            print("Invalid Option")
elif choice=="3d":
    from vectors import Vector3D
    
    obj = Vector3D(int(input("Enter X coordinate: ")),int(input("Enter Y coordinate: ")),int(input("Enter Z coordinate: ")))
    option = -1
    while option!=0:
        option = int(input("1 for magnitude\n2 for distance with other point\n3 for dot product\n4 for cross product\n5 to display\n0 to Exit\n"))
        if option == 1:
            print(obj.magnitude())
        elif option==2:
            print("Enter Information for other point...")
            
            obj1 = Vector3D(int(input("Enter X coordinate: ")),int(input("Enter Y coordinate: ")),int(input("Enter Z coordinate: ")))
            print(obj.distance(obj1))
        elif option==3:
            print("Enter Information for other point...")
            obj1 = Vector3D(int(input("Enter X coordinate: ")),int(input("Enter Y coordinate: ")),int(input("Enter Z coordinate: ")))
            print(obj.dot_product(obj1))
        elif option==4:
            print("Enter Information for other point...")    
            obj1 = Vector3D(int(input("Enter X coordinate: ")),int(input("Enter Y coordinate: ")),int(input("Enter Z coordinate: ")))
            print(obj.cross_product(obj1))
        elif option==5:
            print(obj.__repr__)
        elif option==0:
            exit()
        else:
            print("Invalid Option")
else: 
    print("Invalid Value")