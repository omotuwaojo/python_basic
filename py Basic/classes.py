class car:
    def _init_(self,name,gear,miles):
        self.name = name
        self.gear = gear
        self.miles =miles
    def drive(self,miles):
        self.miles = self.miles + miles
    def shift_gear(self,gear):
        self.gear = gear
#car = car("Tesal", 0 ,0)
del car  

# object oriented programming
# inheritance
class Employee:
    def __init__(self, name, age, dob, job_description):
        self.name = name
        self.age = age
        self.dob = dob
        self.job_description = job_description
    def get_salary(self):
        print("salary printend")
#child class
class Manager(Employee):
    def __init__(self, name, age, dob, job_description):
        super().__init__(  name, age, dob, job_description)
        self.department = department
        self.employees = employees
    def add_employee(self):
        print("adding employees")
    def get_salary(self):
        print("salary printed for manager")
manager = Manager("me, ojo, 23,  i998/9/19, softwear enginnering, softwear",)
manager.get_salary()
manager.add_employee()
