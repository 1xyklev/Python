class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

        Employee.empCount += 1  # 클래스 변수 값 변경

    def displayEmp(self):
        print(f"Name:{self.name}, Salary:{self.salary}")

emp1 = Employee("kim", 5000)
emp2 = Employee("lee", 6000)

emp1.displayEmp()
emp2.displayEmp()

print(f"Total employees: {Employee.empCount}")