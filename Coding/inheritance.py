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

class Programmer(Employee):
    def __init__(self, fname, lname, salary, progLang, exprnc):
        super().__init__(fname, lname, salary)
        self.progLang = progLang
        self.exprnc = exprnc

    def increase(self):
        self.salary = self.salary * ( self.increment + 1 )
E1 = Programmer("ali","raza",50000,"C++",'2 years')
print(E1.fname)
print(E1.lname)
print(E1.salary)
print(E1.progLang)
print(E1.exprnc)
E1.increase()
print(E1.salary)
# print(help(Programmer))