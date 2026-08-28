class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def calculate_total(self):
        return sum(self.marks)

    def calculate_percentage(self):
        return self.calculate_total() / 3

    def get_grade(self):
        percentage = self.calculate_percentage()

        if percentage >= 80:
            return "A"
        elif percentage >= 60:
            return "B"
        elif percentage >= 40:
            return "C"
        else:
            return "F"

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks)
        print("Total:", self.calculate_total())
        print("Percentage:", self.calculate_percentage())
        print("Grade:", self.get_grade())


s1 = Student("Amrit", 101, [85, 78, 92])
s2 = Student("Rahul", 102, [65, 70, 58])

s1.display()
print()
s2.display()