import json
import os

class Student:
  def __init__(self, student_id, name, age, grade):
    self.student_id = student_id
    self.name = name
    self.age = age
    self.grade = grade

  def to_dict(self):
      return {
          "student_id": self.student_id,
          "name": self.name,
          "age": self.age,
          "grade": self.grade
      }

class StudentManager:
  def __init__(self, filename="storage.json"):
    self.filename = filename
    self.students = self.load_students()

  def load_students(self):
    if not os.path.exists(self.filename):
      return []
    with open(self.filename, "r") as f:
      try:
        return json.load(f)
      except json.JSONDecodeError:
        return []

  def save_students(self):
    with open(self.filename, "w") as f:
        json.dump(self.students, f, indent=4)

  def add_student(self, student):
    self.students.append(student.to_dict())
    self.save_students()

  def update_student(self, student_id, updated_data):
    for student in self.students:
      if student["student_id"] == student_id:
        student.update(updated_data)
        self.save_students()
        return True
    return False

  def delete_student(self, student_id):
    for student in self.students:
      if student["student_id"] == student_id:
        self.students.remove(student)
        self.save_students()
        return True
    return False

  def search_student(self, student_id):
    for student in self.students:
      if student["student_id"] == student_id:
        return student
    return None

  def list_students(self):
    return self.students
