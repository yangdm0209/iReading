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
        name = school.name[6:]
        for n in range(start, end):
            teacher = Teacher()
            teacher.school = school
            teacher.name = 'teacher%s-%s' % (n, name)
            teacher.save()


def add_course(start, end):
    for teacher in Teacher.objects.all():
        for n in range(start, end):
            course = Course()
            course.teacher = teacher
            course.school = teacher.school
            course.name = 'course of %s(%s)' % (teacher.name[7:], n)
            course.save()


def add_student(start, end):
    for course in Course.objects.all():
        for n in range(start, end):
            student = Student()
            student.name = '%s-stu-%s' % (course.name, n)
            student.school = course.school
            # student.course.add(course.id)
            student.save()


if __name__ == '__main__':
    add_student(1, 3)
