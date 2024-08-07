class Employee:
    increment = 2
    no_of_employees = 0
    def __init__(self,fname,lname,salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        Employee.no_of_employees += 1
    def increase(self):
        self.salary = self.salary * self.increment
    # def change_increment(self,i):
    #     self.increment = i
    #     Employee.increment = i
    @classmethod
    def change_increment(cls, i):
        cls.increment = i
        Employee.increment = i
E1 = Employee("aslam", "raza", 44000)
E2 = Employee("ali", "hamza", 44000)

print(E1.salary)
E1.increase()
print(E1.salary)
E1.change_increment(3)
E1.increase()
print(E1.salary)




