import datetime
class Employee:
    num_of_emp = 0 #classVariables 
    raise_amount = 1.04

    def __init__(self, fname, lname, salary):
        self.fname= fname    #instance variables
        self.lname = lname
        self.salary = salary
        self.email =fname+'.'+ lname + '@company.com'

        Employee.num_of_emp +=1

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

    Dev_1 = Developer("ron", "wisely", 70000, "python")
    print(Dev_1.raise_amount)
    print(Dev_1.prog_lang)

    mng_1 = Manager("albos", "dombledor", 140000, [emp, Dev_1])

    mng_1.print_employees()


main()