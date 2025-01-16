import sys
import math

class Student:
    def __init__(self, name, exam, ca):
        self.name = name
        self.exam_mark = exam
        self.ca_mark = ca

    def get_average(self):
        return (self.exam_mark + self.ca_mark) / 2

    def __str__(self):
        return "Name: {}, Average: {}".format(self.name, self.get_average())

import sys
if __name__ == '__main__':
    with open(sys.argv[1]) as inF:
        for line in inF:
            student_info = line.split(',')
            student = Student(student_info[0],float(student_info[1]),float(student_info[2]))
            print(student)