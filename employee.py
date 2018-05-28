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
def main():
    print(Employee.num_of_emp)
    emp = Employee("harry", "potter", 90000)
    print(emp.email)
    print(emp.salary)
    emp.apply_raise()
    print(emp.salary)
    print(Employee.num_of_emp)

main()