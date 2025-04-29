from student import Student, StudentManager

def menu():
  print("\n--- Student Management System ---")
  print("1. Add Student")
  print("2. Update Student")
  print("3. Delete Student")
  print("4. Search Student")
  print("5. List All Students")
  print("6. Exit")

def main():
  manager = StudentManager()

  while True:
    menu()
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
      student_id = input("Enter Student ID: ")
      name = input("Enter Name: ")
      age = input("Enter Age: ")
      grade = input("Enter Grade: ")
      student = Student(student_id, name, age, grade)
      manager.add_student(student)
      print("Student added successfully!")

    elif choice == "2":
      student_id = input("Enter Student ID to update: ")
      print("Enter new details (leave blank to keep unchanged):")
      name = input("New Name: ")
      age = input("New Age: ")
      grade = input("New Grade: ")

      updated_data = {}
      if name:
        updated_data["name"] = name
      if age:
        updated_data["age"] = age
      if grade:
        updated_data["grade"] = grade

      if manager.update_student(student_id, updated_data):
        print("Student updated successfully!")
      else:
        print("Student not found.")

    elif choice == "3":
      student_id = input("Enter Student ID to delete: ")
      if manager.delete_student(student_id):
        print("Student deleted successfully!")
      else:
        print("Student not found.")

    elif choice == "4":
      student_id = input("Enter Student ID to search: ")
      student = manager.search_student(student_id)
      if student:
          print("Student Found:", student)
      else:
          print("Student not found.")

    elif choice == "5":
      students = manager.list_students()
      if students:
          for student in students:
              print(student)
      else:
          print("No students found.")

    elif choice == "6":
      print("Exiting... Goodbye!")
      break

    else:
      print("Invalid choice. Please enter between 1 and 6.")

if __name__ == "__main__":
  main()
