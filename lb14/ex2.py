class Student:
    def __init__(self, name, specialty, course):
        self.name = name
        self.specialty = specialty
        self.course = course
    def calculate_group(self):
        specialty_code = sum(ord(char) for char in self.specialty[:2])
        return specialty_code % 10 + self.course * 10
class InternStudent(Student):
    def __init__(self, name, specialty, course, internship_place):
        super().__init__(name, specialty, course)
        self.internship_place = internship_place
    def calculate_group(self):
        return 40
student1 = Student("Ватуля Іларіон", "Комп'ютерні науки", 2)
intern_student1 = InternStudent("Любченко Єфросинія", "Економіка", 4, "Банк 'Приват'")
print(f"Студент: {student1.name}, спеціальність: {student1.specialty}, курс: {student1.course}")
print(f"Студент: {intern_student1.name}, спеціальність: {intern_student1.specialty}, курс: {intern_student1.course}, місце практики: {intern_student1.internship_place}")
