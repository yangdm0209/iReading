#!/usr/bin/env python
# coding: utf-8

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PRO_ABSPATH = os.path.abspath(os.path.join(BASE_DIR, '../'))
sys.path.insert(0, BASE_DIR)
sys.path.insert(0, PRO_ABSPATH)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ireading.settings")
import django

django.setup()

from usercenter.models import School, Teacher, Course, Student


def add_school(start, end):
    for n in range(start, end):
        school = School()
        school.name = 'school%s' % n
        school.save()


def add_teacher(start, end):
    for school in School.objects.all():
        for n in range(start, end):
            teacher = Teacher()
            teacher.school = school
            teacher.name = 'teacher%s' % n
            teacher.save()


def add_course(start, end):
    for teacher in Teacher.objects.all():
        for n in range(start, end):
            course = Course()
            course.teacher = teacher
            course.school = teacher.school
            course.name = 'course%s' % n
            course.save()


def add_student(start, end):
    for school in School.objects.all():
        for n in range(start, end):
            student = Student()
            student.name = 'student%s' % n
            student.level = 0
            student.school = school
            student.save()


if __name__ == '__main__':
    add_school(1, 3)
    add_teacher(1, 3)
    add_student(1, 9)
    add_course(1, 3)
