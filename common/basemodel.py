#!/usr/bin/env python
# coding: utf-8

from django.db import models
import time

from common.timeutil import friendly_time


class Timestampable(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='modify time')

    @property
    def get_updated_friendly_time(self):
        time_array = time.strptime(str(self.updated_at.replace(microsecond=0)), "%Y-%m-%d %H:%M:%S")
        timestamp = int(time.mktime(time_array))
        return friendly_time(timestamp)

    @property
    def get_created_friendly_time(self):
        time_array = time.strptime(str(self.created_at.replace(microsecond=0)), "%Y-%m-%d %H:%M:%S")
        timestamp = int(time.mktime(time_array))
        return friendly_time(timestamp)

    class Meta:
        abstract = True
