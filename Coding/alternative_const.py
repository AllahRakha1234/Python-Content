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
    @classmethod
    def from_str(cls, emp_string):
        fname,lname,salary = emp_string.split("-")
        return cls(fname, lname, salary)
E1 = Employee("aslam", "raza", 44000)
E2 = Employee("ali", "hamza", 44000)
E3 = Employee.from_str("luqman-ahmad-50000")
print(E3.salary)
print(E3.fname)
print(E3.lname)




