import json
from abc import ABC,abstractmethod
from pathlib import Path

database = "school_data.json"
data = {"students" : [], "teachers" : []}

if Path(database).exists():
    with open(database, 'r') as f:
        content = f.read()
        if content :
            data = json.loads(content)

def save():
    with open(database,"w") as f:
        json.dump(data,f,indent=4)


class Persons(ABC):

    @abstractmethod
    def get_roles(self):
        pass

    @abstractmethod
    def register(self):
        pass

    @abstractmethod
    def show_details(self):
        pass

    @staticmethod
    def validate_email(email):
        if "@" in email and "." in email:
            return True
        else:
            return False

class Student(Persons):

    def get_roles(self):
        return "Student" 

    def register(self):
        name = input("Enter your name : ")
        age = int(input("Enter your age : "))
        email = input("Enter your email id : ")
        roll_no = input("Enter your roll number : ")

        if not Persons.validate_email(email):
            print("Invalid Email!")
            return

        for i in data['students']:
            if i['roll_no'] == roll_no:
                print("Student already exists!")
                return

        data['students'].append({
            "name" : name,
            "age" : age,
            "email" : email,
            "roll_no" : roll_no,
            "grades" : {}         #grades ke andr bhi ek aur dictionary bani isliye
        })                        #kyunki grades ke andr diff subjects ke grades ho skte hai
        save()
        print(f"Student {name} registered.")

    def show_details(self):
        roll_no = input("Enter your roll numner : ")
        for i in data['students']:
            if i['roll_no'] == roll_no:
                grades = i['grades']
                average = (sum(grades.values()) / len(grades)) if grades else 0

                print(f"\nName : {i['name']}")
                print(f"Roll no. : {i['roll_no']}")
                print(f"Grades : {grades}")
                print(f"Average : {average:.1f}")
                return


    def add_grade(self):
        roll_no = input("Enter the roll number : ")
        subject = input("Subject : ")
        marks = float(input("Marks : "))

        for i in data['students']:
            if i['roll_no'] ==roll_no:
                i['grades'][subject] = marks
                save()
                print("Grades added succesfully.")
                return
        print("Student not found!")


class Teacher(Persons):

    def get_roles(self):
            return "Teacher" 

    def register(self):
            name = input("Enter your name : ")
            age = int(input("Enter your age : "))
            email = input("Enter your email id : ")
            subject = input("Enter the subject department : ")
            emp_id = input("Enter your Employee id : ")

            if not Persons.validate_email(email):
                print("Invalid Email!")
                return

            for i in data['teachers']:
                if i['emp_id'] == emp_id:
                    print("Employee already exists!")
                    return

            data['teachers'].append({
                "name" : name,
                "age" : age,
                "email" : email,
                "subject" : subject,
                "emp_id" : emp_id            
                })
            save()
            print(f"Staff {name} registered.")

    def show_details(self):
        emp_id = input("Enter the employee ID : ")

        for i in data["teachers"]:
            if i["emp_id"] == emp_id:
                print(f"\nName : {i['name']}")
                print(f"Subject : {i['subject']}")
                print(f"Employee ID : {i['emp_id']}")
                return
        print("Staff not found!")

stud = Student()
teach = Teacher()

print("Press 1 to register a student")
print("Press 2 to register a teacher")
print("Press 3 to add grades")
print("Press 4 to display student details")
print("Press 5 to display teacher details")


choice = int(input("Enter your choice : "))

if choice == 1:
    stud.register()

elif choice == 2:
    teach.register()

elif choice == 3:
    stud.add_grade()

elif choice == 4:
    stud.show_details()

elif choice == 5:
    teach.show_details()