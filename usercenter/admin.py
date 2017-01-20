#!/usr/bin/env python
# coding: utf-8

from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from usercenter.models import Teacher, School, Course, Student


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    fields = ['name']
    search_fields = ['name']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'school']
    list_display_links = ['name']
    fields = ['name', 'school']
    list_filter = ['school']
    search_fields = ['name', 'school__name']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'teacher', 'school', 'students_num']
    list_display_links = ['name']
    fields = ['name', 'teacher', 'school']
    list_filter = ['teacher', 'school']
    search_fields = ['teacher__name', 'school__name']

    def teacher_of_class(self, obj):
        return mark_safe('<a href="/admin/usercenter/teacher/%s/">%s</a>' % (obj.teacher.id, obj.teacher))

    def students_num(self, obj):
        student_list = []
        for student in obj.student_set.all():
            student_list.append('<li><a href="/admin/usercenter/student/%s/">%s</a></li>' % (student.id, student.name))
        if len(student_list) > 0:
            students = ''.join(student_list)
            return mark_safe('学生总数: <b>%s</b><br/><ul class="list-unstyled">%s</ul>' % (
                len(student_list), students.encode('utf-8')))
        else:
            return mark_safe('<span class="text-warning">还没有学生</span>')

    students_num.short_description = '学生'
    teacher_of_class.short_description = '老师'


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'school', 'courses']
    list_display_links = ['name']
    fields = ['name', 'school', 'course']
    list_filter = ['school']
    search_fields = ['name', 'school__name']

    def courses(self, obj):
        courses = []
        for item in obj.course.all():
            courses.append(item.name)
        return ", ".join(courses)

    courses.short_description = "课程"
    # course.short_description = "课程"
