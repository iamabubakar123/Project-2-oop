class Employee:
    def __init__(self, name,age,salary,employeesyearofservice):
        self.name = name
        self.age = age
        self.salary = salary
        self.employeesyearofservice = employeesyearofservice
    
    def display_info(self):
        print(f"name: {self.name}")
        print(f"age: {self.age}")
        print(f"salary: {self.salary}")
        print(f"employeesyearofservice: {self.employeesyearofservice}")
class Employee_management_system:
    def __init__(self):
        self.employee_array = []
    def add_employee(self, employee):
        hash1 = {"name": employee.name, "age": employee.age, "salary": employee.salary, "employeesyearofservice":employee.employeesyearofservice}
        self.employee_array.append(hash1)
        
    def add_employee(self, employee):
        self.employee_array.append(employee)

    def find_employee_by_name(self, name):
        for employee in self.employee_array:
            if employee.name == name:
               
                print("Employee Found:")
                print(f"Name: {employee.name}")
                print(f"Age: {employee.age}")
                print(f"Salary: {employee.salary}")
                found = True
                break
        if not found:
            print ("not found")
    
    
    def total_employee_salary(self):
        total_salary = 0
        for employee in self.employee_array:
            total_salary += employee.salary
        return total_salary
    
    def add_increment_salary(self, increment):
        for employee in self.employee_array:
            employee.salary += (employee.salary * increment / 100)

    def add_bonus_salary(self, bonus):
        for employee in self.employee_array:
            if employee.employeesyearofservice >= 5:
                employee.salary += bonus
      
            
employee1 = Employee("Abubakar", 20, 30000, 6)
employee2 = Employee("Waleed", 28, 50000, 7)
employee3 = Employee("Usman", 32, 80000, 2)

ems = Employee_management_system()

ems.add_employee(employee1)
ems.add_employee(employee2)
ems.add_employee(employee3)

print(f"name: {ems.employee_array[1].name}")

value = ems.employee_array[1].name
found_employee = ems.find_employee_by_name(value)


total_salary = ems.total_employee_salary()
print("Total Salary:", total_salary)

ems.add_increment_salary(10)
for employee in ems.employee_array:
    employee.display_info()

bonus_added = ems.add_bonus_salary(10000)
if bonus_added:
    print('Bonus was added')
    print(f"Name: {bonus_added.name}")
    print(f"Age: {bonus_added.age}")
    print(f"Salary: {bonus_added.salary}")
    bonus_added.display_info()
else:
    print("NOT bonus")    
value = ems.employee_array[1].name
found_employee = ems.find_employee_by_name(value)