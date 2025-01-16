import sys
import math


class Student:
    id_counter = 1
    def __init__(self, name, exam, ca):
        self.name = name
        self.exam_mark = exam
        self.ca_mark = ca
        self.id = Student.id_counter
        Student.id_counter += 1

    def get_average(self):
        return (self.exam_mark + self.ca_mark) / 2

    def __str__(self):
        return "Id: {}, Name: {}, Average: {}".format(self.id, self.name, self.get_average())


if __name__ == '__main__':
    with open("students.txt", "r") as inF:
        for line in inF:
            student_info = line.split(',')
            student = Student(student_info[0], float(student_info[1]), float(student_info[2]))
            print(student)