class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks)

if __name__ == '__main__':
    name = input()
    roll_no = int(input())
    marks = int(input())

    student = Student(name, roll_no, marks)
    student.display()