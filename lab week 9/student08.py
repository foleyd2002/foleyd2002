import sys
import math
from student07 import Student

class CA278Student(Student):
    def __init__(self, name, exam, ca, group_idea):
        Student.__init__(self, name, exam, ca)
        self.group_idea = group_idea

    def __str__(self):
        return "Id: {}, Name: {}, Average: {}, Group Project Idea: {}".format(
            self.id, self.name, self.get_average(), self.group_idea)


if __name__ == '__main__':
    with open("students.txt", "r") as inF:
        for line in inF:
            student_info = line.split(',')
            ca278_student = CA278Student(student_info[0], float(student_info[1]), float(student_info[2]), student_info[3].strip())
            print(ca278_student)
