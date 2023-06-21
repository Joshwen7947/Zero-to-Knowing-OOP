class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id
        
    def __str__(self):
        return f"Employee: {self.name}, (ID: {self.employee_id})"
    
    def __eq__(self, other):
        if isinstance(other, Employee):
            return self.employee_id == other.employee_id
        return False
    
    def __add__(self, other):
        raise ValueError("Can not add employees!")
        
        
class Manager(Employee):
    def __init__(self, name, employee_id, department):
        Employee.__init__(self, name, employee_id)
        self.department = department
        
    def __str__(self):
        return f"Name: {self.name}, (ID: {self.employee_id}, Dept: {self.department})"
    
    def __eq__(self, other):
        if isinstance(other, Employee):
            return self.employee_id == other.employee_id
        return False
    
    def __add__(self, other):
        raise ValueError("Can not add Manager!")
    
    
class Staff(Employee):
    def __init__(self, name, employee_id, role):
        Employee.__init__(self, name, employee_id)
        self.role = role
        
    def __str__(self):
        return f"Name: {self.name}, (ID: {self.employee_id}, Position: {self.role})"
    
    def __eq__(self, other):
        if isinstance(other, Employee):
            return self.employee_id == other.employee_id
        return False
    
    def __add__(self, other):
        raise ValueError("Can not add Staff Members!")
     

employee1 = Employee("John Doe", 1)
employee2 = Employee("Jane Doe", 2)

manager1 = Manager("Bruce Bruce",9,"marketing")
manager2 = Manager("Sarah Jane", 8, "sales")

staff1 = Staff("Mark Jones", 12, "Marketing Ops Dev")
staff2 = Staff("Emily Davis", 14, "Software Engineer")


print(employee1)
print(manager1)
print(staff1)

print(employee1 == employee2)
print(staff1 == staff2)

print(manager1 + manager2)