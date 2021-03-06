import datetime
class Employee:
    num_of_emp = 0 #classVariables 
    raise_amount = 1.04

    def __init__(self, fname, lname, salary):
        self.fname= fname    #instance variables
        self.lname = lname
        self.salary = salary

        Employee.num_of_emp +=1

    @property  # define a method like it's an attribute
    def email(self):
        return self.fname+'.'+ self.lname + '@company.com'
     
        
    def apply_raise(self):
         # we could use Employee.raise_amount but maybe in the future we wanted to change the raise vaule for a specific employee
         self.salary = int(self.salary * self.raise_amount)

    @classmethod
    def set_raise_value(cls, raise_amount):
        cls.raise_amount = raise_amount

    @classmethod # as a constructor this time
    def set_obj_from_string(cls, string):
        first, last, pay = string.split('-')
        return cls(first, last, int(pay))

    @staticmethod
    def is_workday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True

    #dunder methods
    def __str__(self):
        return '{}'.format(self.email)

    def __repr(self):
        return 'name: {}, lastname: {}, email {} '.format(self.fname, self.lname, self.email)
class Developer(Employee): #subclass of based class Employee
    raise_amount = 1.1
    def __init__(self,  fname, lname, salary, prog_lang):
        super().__init__(fname, lname, salary)
        #alternate way line below
        #Employee.__init__(self, fname, lname, salary)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, fname, lname, salary, employees = None):
        super().__init__(fname, lname, salary)
        if employees==None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)
        else:
            print("employee already exists")

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove()
        else:
            print("employee does not exist")

    def print_employees (self):
        for employee in self.employees:
            print(employee.fname)

def main():
    print(Employee.num_of_emp)
    emp = Employee("harry", "potter", 90000)
    print(str(emp))
    print(emp.email)
    print(emp.salary)
    emp.apply_raise()
    print(emp.salary)
    print(Employee.num_of_emp)

    emp.raise_amount= 0.3
    print(Employee.raise_amount)
    Employee.set_raise_value(1.05)
    print(Employee.raise_amount)
    print(emp.raise_amount)

    string = "hermoine-grenger-80000"
    emp_2= Employee.set_obj_from_string(string)
    print(emp_2.fname)

    print(Employee.is_workday(datetime.date(2018, 10, 6)))

    dev_1 = Developer("ron", "wisely", 70000, "python")
    print(dev_1.raise_amount)
    print(dev_1.prog_lang)

    mng_1 = Manager("albos", "dombledor", 140000, [emp, dev_1])

    mng_1.print_employees()
    print(emp)
    print(dev_1)
    print(mng_1)
   
main()