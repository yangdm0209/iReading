#!/usr/bin/env python
# coding: utf-8

from django.db import models


# Create your models here.



class School(models.Model):
    name = models.CharField(max_length=128, verbose_name="名字")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "学校"
        verbose_name = "学校"


class Teacher(models.Model):
    name = models.CharField(max_length=128, verbose_name="名字")
    school = models.ForeignKey(School, verbose_name="学校")

    def __unicode__(self):
        return '%s(%s)' % (self.name, self.school)

    class Meta:
        verbose_name_plural = "老师"
        verbose_name = "老师"


class Course(models.Model):
    name = models.CharField(max_length=128, verbose_name="名称")
    school = models.ForeignKey(School, verbose_name="学校")
    teacher = models.ForeignKey(Teacher, verbose_name="老师")

    def __unicode__(self):
        return "%s-%s-%s" % (self.name, self.teacher.name, self.school)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "课程"
        verbose_name = "课程"
        # ordering = ['teacher', 'name']


class Student(models.Model):
    name = models.CharField(max_length=128, verbose_name="名字")
    school = models.ForeignKey(School, verbose_name="学校")
    course = models.ManyToManyField(Course, verbose_name="课程")

    def __unicode__(self):
        return "%s-%s" % (self.name, self.course)

    class Meta:
        verbose_name_plural = "学生"
        verbose_name = "学生"
