class School:
    def __init__(self):
        self.students = {}

    def add_student(self, name, grade):
        if grade in self.students.keys():
            self.students[grade].append(name)
        else:
            self.students[grade] = [name]

    def roster(self):
        students = []
        for grade in sorted(self.students.keys()):
            students += sorted(self.students[grade])
        return students

    def grade(self, grade_number):
        if grade_number in self.students.keys():
            return sorted(self.students[grade_number])
        else:
            return []
