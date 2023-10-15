class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa

def sort_students(student_list):
  # sort the list of the students in descending order of CGPA
  sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
  return sorted_students
  
# Example usage:
students = [Student("David","A143",7.8),
            Student("Sasi","A145",8.9),
            Student("Harish","A123",9.1),
            Student("Daisy","A126",9.9)]

sorted_students = sort_students(students)

# Print the sorted list of students
for student in sorted_students:
  print("Name: {}, Roll number: {}, CGPA: {}".format(student.name,student.roll_number, student.cgpa))


  


