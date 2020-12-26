from marksman.db import Modelz

from marksman.validators import get_pos_int, get_str, get_email


def _roll():
    return get_pos_int('Enter roll number of student: ')


def _uid():
    return get_pos_int('Enter the unique id of exam: ')


class Student:

    def __init__(self, students: Modelz) -> None:
        self.students = students
        self.roll = _roll()
        self.object = self.read()

    def read(self):
        return self.students.exists(roll=self.roll)

    def create(self):
        self.students.insert((self.roll, get_str(), get_email()))

    def update(self):
        self.students.update(f'''name="{get_str(default=self.object[1])}",\
            email="{get_email(default=self.object[2])}"''', roll=self.roll)

    def delete(self):
        self.students.delete(roll=self.roll)


class Exam:
    def __init__(self, exams: Modelz) -> None:
        self.exams = exams
        self.uid = _uid()
        self.object = self.read()

    def read(self):
        return self.exams.exists(uid=self.uid)

    def create(self):
        self.exams.insert((self.uid, get_str()))

    def update(self):
        self.exams.update(f'''name="{get_str(default=self.object[1])}"''',
                          uid=self.uid)

    def delete(self):
        self.exams.delete(uid=self.uid)


class MarksEntry:
    def __init__(self, marks: Modelz) -> None:
        self.marks = marks
        self.roll = _roll()
        self.uid = _uid()
        self.object = self.read()

    def read(self):
        return self.marks.exists(student=self.roll, exam=self.uid)

    def create(self):
        self.marks.insert((self.roll, self.uid, get_pos_int('Enter marks: ')))

    def update(self):
        self.marks.update(
            f"marks={get_pos_int('Enter marks: ')}", student=self.roll, exam=self.uid)

    def delete(self):
        self.marks.delete(student=self.roll, exam=self.uid)
