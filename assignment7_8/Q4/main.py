from Employee import Employee
    
dummy_employee1 = Employee("Dummy1", 10)
dummy_employee2 = Employee("Dummy2", 20)
list = Employee()
choice = -1
while choice != 0:
    print("1.Add new employee\n2.Add or Subtract salary of 2 employees\n3.Compare salary of 2 employees\n0.Exit\n")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        list.add_employee()
        print("\nEmployee successfully added\n")

    elif choice == 2:
        inner_choice = -1
        while inner_choice != 0:
            print("\n1.Add employees salary\n2.Subtract employees salary\n0.Exit\n")
            inner_choice = int(input("Enter your choice: "))

            if inner_choice == 1:
                name1 = str(input("Enter name of employee 1: "))
                name2 = str(input("Enter name of employee 2: "))

                employee1 = next((emp for emp in list.employees if emp.name == name1), dummy_employee1)
                employee2 = next((emp for emp in list.employees if emp.name == name2), dummy_employee2)

                if employee1 != dummy_employee1 and employee2 != dummy_employee2:
                    print(f"\nThe addition of employee salaries is {employee1 + employee2}")
                else:
                    employee1 = dummy_employee1
                    employee2 = dummy_employee2
                    print("\n1 or 2 employees not found!\nUsing dummy employees with salary 10 and 20")
                    print(f"\nThe addition of employee salaries is {employee1 + employee2}")
            
            elif inner_choice == 2:
                name1 = str(input("Enter name of employee 1: "))
                name2 = str(input("Enter name of employee 2: "))

                employee1 = next((emp for emp in list.employees if emp.name == name1), dummy_employee1)
                employee2 = next((emp for emp in list.employees if emp.name == name2), dummy_employee2)

                if employee1 != dummy_employee1 and employee2 != dummy_employee2:
                    print(f"\nThe substraction of employee salaries (Employee 1 - Employee 2) is {employee1 - employee2}")
                else:
                    employee1 = dummy_employee1
                    employee2 = dummy_employee2
                    print("\n1 or 2 employees not found!\nUsing dummy employees with salary 10 and 20\n")
                    print(f"\nThe substraction of employee salaries (Employee 1 - Employee 2) is {employee1 - employee2}")
            
            elif inner_choice == 0:
                print("Exiting operator menu...\n")

            else:
                print("\nPlease enter a valid number!\n")
            
    elif choice == 3:
        inner_choice = -1
        while inner_choice != 0:
            print("\n1.Compare greater than\n2.Compare less than\n0.Exit\n")
            inner_choice = int(input("Enter your choice: "))

            if inner_choice == 1:
                name1 = str(input("Enter name of employee 1: "))
                name2 = str(input("Enter name of employee 2: "))

                employee1 = next((emp for emp in list.employees if emp.name == name1), dummy_employee1)
                employee2 = next((emp for emp in list.employees if emp.name == name2), dummy_employee2)

                if employee1 != dummy_employee1 and employee2 != dummy_employee2:
                    print(f"\nSalary of (Employee 1 > Employee 2): {employee1>employee2}")
                else:
                    employee1 = dummy_employee1
                    employee2 = dummy_employee2
                    print("\n1 or 2 employees not found!\nUsing dummy employees with salary 10 and 20")
                    print(f"\nSalary of (Employee 1 > Employee 2): {employee1>employee2}")
            
            elif inner_choice == 2:
                name1 = str(input("Enter name of employee 1: "))
                name2 = str(input("Enter name of employee 2: "))

                employee1 = next((emp for emp in list.employees if emp.name == name1), dummy_employee1)
                employee2 = next((emp for emp in list.employees if emp.name == name2), dummy_employee2)

                if employee1 != dummy_employee1 and employee2 != dummy_employee2:
                    print(f"\nSalary of (Employee 1 < Employee 2): {employee1<employee2}")
                else:
                    employee1 = dummy_employee1
                    employee2 = dummy_employee2
                    print("\n1 or 2 employees not found!\nUsing dummy employees with salary 10 and 20")
                    print(f"\nSalary of (Employee 1 < Employee 2): {employee1<employee2}")
            
            elif inner_choice == 0:
                print("Exiting comparison menu...\n")

            else:
                print("\nPlease enter a valid number!\n")

    elif choice == 0:
        print("\nExiting the program...")

    else:
        print("\nPlease enter a valid number!\n")
exit(0)
