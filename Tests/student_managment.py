class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def accept_student_details(self):
        name = input("Enter student's name: ")
        age = input("Enter student's age: ")
        grade = input("Enter student's grade: ")
        self.students.append(Student(name, age, grade))

    def display_student_details(self):
        for student in self.students:
            print(f"Name: {student.name}, Age: {student.age}, Grade: {student.grade}")

    def search_student_details(self, name):
        for student in self.students:
            if student.name == name:
                return f"Name: {student.name}, Age: {student.age}, Grade: {student.grade}"
        return "Student not found"

    def delete_student_details(self, name):
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                return "Student details deleted"
        return "Student not found"

    def update_student_details(self, name):
        for student in self.students:
            if student.name == name:
                student.name = input("Enter new name: ")
                student.age = input("Enter new age: ")
                student.grade = input("Enter new grade: ")
                return "Student details updated"
        return "Student not found"

def main():
    sms = StudentManagementSystem()
    while True:
        print("\n1. Accept Student Details")
        print("2. Display Student Details")
        print("3. Search Details of a Student")
        print("4. Delete Details of Student")
        print("5. Update Student Details")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            sms.accept_student_details()
        elif choice == 2:
            sms.display_student_details()
        elif choice == 3:
            name = input("Enter the name of the student to search: ")
            print(sms.search_student_details(name))
        elif choice == 4:
            name = input("Enter the name of the student to delete: ")
            print(sms.delete_student_details(name))
        elif choice == 5:
            name = input("Enter the name of the student to update: ")
            print(sms.update_student_details(name))
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
