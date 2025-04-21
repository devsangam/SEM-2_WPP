

class Employee:
    def __init__(self, name = "", salary = 0.0):
        self.name = name
        self.salary = salary

    employees = []

    def add_employee(self):
        employee = Employee(str(input("Enter employee name: ")), float(input("Enter employee salary: ")))
        self.employees.append(employee)

    def __add__(self, other):
        return self.salary + other.salary
    
    def __sub__(self, other):
        return self.salary - other.salary
    
    def __gt__(self, other):
        return self.salary > other.salary
    
    def __lt__(self, other):
        return self.salary < other.salary