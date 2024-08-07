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
print(Employee.isopen("Tuesday"))
print(Employee.isopen("Sunday"))
print(Employee.isopen("sunday"))




