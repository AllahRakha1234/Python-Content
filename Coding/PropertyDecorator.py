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

    @property
    def email(self):
        if self.fname == None:
            return "Email not set"
        else:
            return self.fname + '.' + self.lname + '@gmail.com'

    @email.setter
    def email(self, given_email):
        splitted_list = given_email.split('@')[0].split('.')
        print(splitted_list)
        self.fname = splitted_list[0]
        self.lname = splitted_list[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None
if __name__ == '__main__':
    E1 = Employee("ali", "raza", 500)
    E2 = Employee("adnan", "hassnain", 50)
    print(E1.email)
    print(E2.email)
    E1.lname = 'hassan'
    print(E1.email)

    E1.email = 'hassan.ali@gmail.com'
    print(E1.email)
    del E1.email
    print(E1.email)

