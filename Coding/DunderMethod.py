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

    @staticmethod
    def isopen(day):
        if (day == "sunday" or day == "Sunday"):
            return "Office Close"
        else:
            return "Office Open"

    def __add__(self, other):
        return self.salary + other.salary
    def __repr__(self):
        return "Employee({}, {}, {})".format(self.fname, self.lname, self.salary)
    def __str__(self):
        return "The name of Employee is {} {}".format(self.fname, self.lname)


E1 = Employee("ali", "raza", 500)
E2 = Employee("adnan", "ali", 50)

print(E1 + E2)
print(E1.__add__(E2))
print(str(E1))
print(repr(E1))
print(E1)
