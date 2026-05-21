import json

class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade

    def to_dict(self):
        return {
            "ID": self.student_id,
            "Name": self.name,
            "Grade": self.grade
        }


class StudentManager:
    def __init__(self):
        self.students = []
        self.load_data()

    def add_student(self):
        student_id = input("Enter Student ID: ")

        for student in self.students:
            if student["ID"] == student_id:
                print("Student ID already exists!")
                return

        name = input("Enter Student Name: ")
        grade = input("Enter Student Grade: ")

        student = Student(student_id, name, grade)
        self.students.append(student.to_dict())

        self.save_data()
        print("Student added successfully!")

    def view_students(self):
        if not self.students:
            print("No student records found.")
            return

        print("\nStudent Records:")
        for student in self.students:
            print(student)

    def update_student(self):
        student_id = input("Enter Student ID to update: ")

        for student in self.students:
            if student["ID"] == student_id:
                student["Name"] = input("Enter New Name: ")
                student["Grade"] = input("Enter New Grade: ")

                self.save_data()
                print("Student updated successfully!")
                return

        print("Student not found.")

    def delete_student(self):
        student_id = input("Enter Student ID to delete: ")

        for student in self.students:
            if student["ID"] == student_id:
                self.students.remove(student)

                self.save_data()
                print("Student deleted successfully!")
                return

        print("Student not found.")

    def save_data(self):
        with open("students.json", "w") as file:
            json.dump(self.students, file, indent=4)

    def load_data(self):
        try:
            with open("students.json", "r") as file:
                self.students = json.load(file)
        except FileNotFoundError:
            self.students = []


manager = StudentManager()

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        manager.add_student()

    elif choice == "2":
        manager.view_students()

    elif choice == "3":
        manager.update_student()

    elif choice == "4":
        manager.delete_student()

    elif choice == "5":
        print("Exiting Program...")
        break

    else:
        print("Invalid choice! Please try again.")