from marksman.db import Modelz

from marksman.validators import get_pos_int, get_str, get_email


def _roll():
    return get_pos_int('Enter roll number of student: ')


def _uid():
    return get_pos_int('Enter the unique id of exam: ')


class Student:

    def __init__(self, students: Modelz) -> None:
        self.students = students
        self.object = self.read()

    def read(self):
        return self.students.exists(roll=_roll())

    def create(self, roll):
        self.students.insert((roll, get_str(), get_email()))

    def update(self):
        self.students.update(roll=self.object[0],
                             name=get_str(default=self.object[1]),
                             email=get_email(default=self.object[2]))

    def delete(self):
        self.students.delete(self.object[0])


class Exam:
    def __init__(self, exams: Modelz) -> None:
        self.exams = exams
        self.object = self.read()

    def read(self):
        return self.exams.exists(uid=_uid())

    def create(self, uid):
        self.exams.insert((uid, get_str()))

    def update(self):
        self.exams.update(uid=self.object[0], name=get_str(default=self.object[1]))

    def delete(self):
        self.exams.delete(self.object[0])


class MarksEntry:
    def __init__(self, marks: Modelz) -> None:
        self.marks = marks
        self.object = self.read()

    def read(self):
        return self.marks.exists(roll=_roll(), uid=_uid())

    def create(self, roll, uid):
        self.exams.insert((roll, uid, get_pos_int('Enter marks: ')))

    def update(self):
        self.exams.update(marks=get_pos_int('Enter marks: '))

    def delete(self):
        self.exams.delete(self.exam[0])
