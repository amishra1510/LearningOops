class Employee:
    def __init__(self,name,employee_id,salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print(self.name)
        print(self.employee_id)
        print(self.salary)    

class Developer(Employee):
    def __init__(self,name,employee_id,salary,programming_language):
        super().__init__(name,employee_id,salary)
        self.programming_language = programming_language

    def write_code(self):
        print(self.programming_language)

class Manager(Employee):
    def __init__(self,name,employee_id,salary,team_size):
        super().__init__(name,employee_id,salary)
        self.team_size = team_size

    def manage_team(self):
        print(self.team_size)

d1 = Developer("Amrit","D01",100000,"C++")
d2 = Developer("Aditya","D09",150000,"Python")
m1 = Manager("Richa","M02",90000,"5")
m2 = Manager("Tanya","M03",120000,"4")

d1.display_details()
d1.write_code()

print("----------------")

d2.display_details()
d2.write_code()

print("----------------")

m1.display_details()
m1.manage_team()

print("----------------")

m2.display_details()
m2.manage_team()





