#from random import choice
from random import choice


#Define Courses Function
class Courses:
    def __init__(self, course_id, name, fee):
        self.course_id = course_id
        self.name = name
        self.fee = fee

#Define Students Function
class Students:
    def __init__(self, email, name, student_id, courses, balance):
        self.email = email
        self.name = name
        self.student_id = student_id
        self.courses = []
        self.balance = 0

#Define Enrollment Function
    def enroll(self, course):
        self.courses.append(course)
        self.balance += course.fee

#Define Course Payment Calculation Function
    def calculate_payment(self, fee):
        if fee < 0.4 * self.balance:
            print("A Minimum of 40% of the outstanding balance is required.")
            return False
        self.balance -= fee
        return True

#Define ERegistration Function
class RegistrationSystem:
      def __init__(self):
        self.courses = {}
        self.students = {}

#Define Student Registration Function
    def register_student(self, student_id, name, email):
        if student_id in Students:
            print("Error: ID already exists.")
            if name in Students:
                print("Error: Name already exists.")
                if email in Students:
                    print("Error: Email already exists.")
            return self.students[student_id]
        print("Student registered successfully!")

#Define Course Creation Function
    def add_course(self, course_id, name, fee):
        if course_id in self.courses:
            print("Error: Course ID already exists.")
        else:
            self.courses[course_id] = self.courses
            print("Course added successfully.")

#Define Student Enrollment in Course(s) function
    def enroll_in_course(self, student_id, course_id):
        if student_id not in self.students:
            print("Error: Student not registered.")
            return
        if course_id not in self.courses:
            print("Error: Course not available.")
            return
        student = self.students[student_id]
        course = self.courses[course_id]
        student.enroll(course)
        print(student.name + "has been enrolled in" + course.name)

#Define Student Balance Check Function
    def check_student_balance(self, student_id):
        if student_id not in self.students:
            print("Error: Student not Registered.")
            return
        student = self.students[student_id]
        print(student.name + "balance:" + student.balance)

#Define Viewing All Courses Function
    def show_courses(self):
        return self.courses

#Define Viewing All Registered Students Function
    def show_registered_students(self):
        if not self.students:
            print("No students registered.")
        return self.students

# Define Viewing All Registered Students In A Course Function
    def show_students_in_course(self, name, student_id, course_id):
        return name, student_id, course_id in self.students,


#Define Main Function for Program
def main():
    program = RegistrationSystem()

    while True:
        print('1. Add Course')
        print('2.View Available courses')
        print('3.Register Student(s)')
        print('4.Student Enrollment')
        print('5.Student Enrollment Status')
        print('6.Students Enrolled in Courses')
        print('7.Student Payment Calculation')
        print('8.Student Account Status', )
        print('9.Exit')

       choice = input("Select an option: ")

        if choice == "1":
            course_id = input("Enter Course ID: ")
            name = input("Enter Course Name: ")
            fee = input("Enter Course Fee: ")
            if fee.isdigit():
                program.add_course(course_id, name, float(fee))
            else:
                print("Error: Fee must be a valid number.")

        elif choice == "2":
            program.display_courses(course_id)

        elif choice == "3":
            student_id = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            email = input('Enter Student Email: ')
            if student_id.isnumeric():
                program.register_student(student_id, name, email)
            else:
                print("Error: Student ID must be numeric.")

        elif choice == "4":
            student_id = input("Enter Student ID: ")
            course_id = input("Enter Course ID: ")
            program.enroll(student_id, course_id)

        elif choice == "5":
            program.students()

        elif choice == "6":
            program.students_enrolled()


        elif choice == "7":
            student_id = input("Enter Student ID: ")
            amount = input("Enter Payment Amount: ")
            program.calculate_payment(student_id, float(amount))
            else:
                print("Error: Incorrect Value Entered.")

        elif choice == '8':
            student_id = input("Enter Student ID: ")
            program.view_student_balance(student_id)

        else:
            choice == "9"
        print("Goodbye")


