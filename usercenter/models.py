#!/usr/bin/env python
# coding: utf-8

from django.db import models

# Create your models here.
from common.basemodel import Timestampable


class School(Timestampable):
    name = models.CharField(max_length=128, verbose_name="名字")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "学校"
        verbose_name = "学校"


class Teacher(Timestampable):
    name = models.CharField(max_length=128, verbose_name="名字")
    school = models.ForeignKey(School, verbose_name="学校")

    def __unicode__(self):
        return '%s - %s' % (self.name, self.school)

    class Meta:
        verbose_name_plural = "老师"
        verbose_name = "老师"


class Student(Timestampable):
    L_TP = ((0, 'trial'),
            (1, 'vip'),
            (2, 'svip'))
    name = models.CharField(max_length=128, verbose_name="名字")
    school = models.ForeignKey(School, verbose_name="学校")
    level = models.IntegerField(choices=L_TP, blank=True, default=0, verbose_name="级别")

    def __unicode__(self):
        return '%s - %s' % (self.name, self.school)

    class Meta:
        verbose_name_plural = "学生"
        verbose_name = "学生"


class Course(models.Model):
    name = models.CharField(max_length=128, verbose_name="名称")
    school = models.ForeignKey(School, verbose_name="学校")
    teacher = models.ForeignKey(Teacher, verbose_name="老师")
    students = models.ManyToManyField(Student, through='CourseStudentShip')

    def __unicode__(self):
        return "%s-%s-%s" % (self.name, self.teacher.name, self.school)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "课程"
        verbose_name = "课程"
        # ordering = ['teacher', 'name']


class CourseStudentShip(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='学生')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='课程')
    date_joined = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "学生"
        verbose_name = "学生"
