class Student:
    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        avg = sum(self.marks) / len(self.marks) if self.marks else 0
        if avg >= 90: return "A"
        elif avg >= 75: return "B"
        elif avg >= 60: return "C"
        elif avg >= 50: return "D"
        else: return "F"

class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name, marks):
        student = Student(student_id, name, marks)
        self.students[student_id] = student
        print(f"✅ Student '{name}' added successfully!")

    def display_all(self):
        if not self.students:
            print("No student records found.")
            return
        print("\n--- Student Records ---")
        for sid, s in self.students.items():
            avg = sum(s.marks) / len(s.marks) if s.marks else 0
            print(f"ID: {sid} | Name: {s.name} | Avg Marks: {avg:.2f} | Grade: {s.grade}")

# Quick execution check
if __name__ == "__main__":
    sys = StudentManagementSystem()
    sys.add_student("S101", "Alice", [85, 92, 78])
    sys.add_student("S102", "Bob", [60, 70, 65])
    sys.display_all()