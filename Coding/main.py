class Employee:
    increment = 2
    no_of_employees = 0
    def __init__(self,fname,lname,salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        # self.increment = 3
        Employee.no_of_employees += 1
    def increase(self):
        # self.salary = self.salary * Employee.increment
        self.salary = self.salary * self.increment

print("Number of employee:", Employee.no_of_employees,"\n")
E1 = Employee("aslam", "raza", 44000)
E2 = Employee("ali", "hamza", 44000)
print(E1, E2)
print(E1.fname, E2.fname)
E1.increase()
print(E1.salary)
print(E1.__dict__)
E1.id = 2
print(E1.__dict__)
print(Employee.__dict__), print()
print("Number of employee: ", Employee.no_of_employees)