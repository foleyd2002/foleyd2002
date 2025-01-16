class Employee:
    def __init__(self, name, job_desc, salary):
        self.name = name
        self.job_desc = job_desc
        self.salary = salary

    def net_salary(self):
        return self.salary * 0.8


name = input("Enter the employee name:\n")
job_desc = input("Enter the employee job description:\n")
salary = int(input("Enter the employee salary:\n"))

employee_salary = Employee(name, job_desc, salary)
print("Net Salary:", employee_salary.net_salary())