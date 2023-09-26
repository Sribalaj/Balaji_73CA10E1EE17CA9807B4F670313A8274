class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(students):
    sorted_students = sorted(students, key=lambda x: x.cgpa, reverse=True)
    return sorted_students

# Get the input from the user
students = []
n = int(input("Enter the number of students: "))
for i in range(n):
    name = input("\n Enter the name of student {}: ".format(i + 1))
    roll_number = input("\n Enter the roll number of student {}: ".format(i + 1))
    cgpa = float(input("\n Enter the CGPA of student {}: ".format(i + 1)))
    student = Student(name, roll_number, cgpa)
    students.append(student)

# Call the sort_students function
sorted_students = sort_students(students)

# Print the sorted list of students
for student in sorted_students:
    print("\n Name: {},\n Roll Number: {}, \n CGPA: {}".format(student.name, student.roll_number, student.cgpa))
