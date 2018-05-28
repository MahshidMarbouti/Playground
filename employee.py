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

main()