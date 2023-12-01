class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def display(self):
        print(f"Employee ID: {self.emp_id}, Name: {self.name}")

class Developer(Employee):
    def __init__(self, emp_id, name, lang):
        super().__init__(emp_id, name)
        self.lang = lang

    def display(self):
        super().display()
        print(f"Programming Language: {self.lang}\n")

class Tester(Employee):
    def __init__(self, emp_id, name, tool):
        super().__init__(emp_id, name)
        self.tool = tool

    def display(self):
        super().display()
        print(f"Testing Tool: {self.tool}\n")

class Manager(Employee):
    def __init__(self, emp_id, name):
        super().__init__(emp_id, name)
        self.managed_employees = []

    def add_employee(self, employee):
        self.managed_employees.append(employee)

    def remove_employee(self, employee):
        self.managed_employees.remove(employee)

    def display(self):
        print(f"Employees managed by {self.name}:\n")
        for employee in self.managed_employees:
            employee.display()

dev1 = Developer(1, "John", "Python")
dev2 = Developer(2, "Alice", "JavaScript")
tester1 = Tester(3, "Bob", "Selenium")
tester2 = Tester(4, "Eve", "BeautifulSoup")
manager = Manager(5, "Manager")
manager.add_employee(dev1)
manager.add_employee(dev2)
manager.add_employee(tester1)
manager.add_employee(tester2)
manager.display()
manager.remove_employee(dev1)
print("After removing a developer:\n")
manager.display()