class Employee:
    def __init__(self, name, emp_id, base_salary):
        self.name = name
        self.emp_id = emp_id
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary

    def show_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Base Salary: ${self.base_salary}")
        print(f"Total Salary: ${self.calculate_salary()}")
        print("-" * 30)


class Manager(Employee):
    def __init__(self, name, emp_id, base_salary):
        super().__init__(name, emp_id, base_salary)

    def calculate_salary(self):
        bonus = 0.20 * self.base_salary  
        return self.base_salary + bonus


class Engineer(Employee):
    def __init__(self, name, emp_id, base_salary):
        super().__init__(name, emp_id, base_salary)

    def calculate_salary(self):
        performance_bonus = 0.10 * self.base_salary  
        return self.base_salary + performance_bonus


class Intern(Employee):
    def __init__(self, name, emp_id, stipend):
        super().__init__(name, emp_id, stipend)  

    def calculate_salary(self):
        return self.base_salary  



if __name__ == "__main__":
    
    manager = Manager("John Doe", "M001", 80000)
    engineer = Engineer("Jane Smith", "E001", 60000)
    intern = Intern("Alice Johnson", "I001", 20000)

    print("Manager Details:")
    manager.show_details()

    print("Engineer Details:")
    engineer.show_details()

    print("Intern Details:")
    intern.show_details()