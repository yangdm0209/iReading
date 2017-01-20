#!/usr/bin/env python
# coding: utf-8

import time

def friendly_time(timestamp):
    """
    >>> friendly_time(int(time.time()))
    刚刚
    >>> friendly_time(int(time.time()) + 10*60)
    刚刚
    """
    current_time = int(time.time())
    time_distance = abs(current_time - timestamp)
    if time_distance < 60 * 5:
        return '刚刚'
    elif time_distance < 60 * 60:
        return '%s分钟前' % (time_distance / 60)
    elif time_distance < 60 * 60 * 24:
        return '%s小时前' % (time_distance / 60 / 60)
    elif time_distance < 60 * 60 * 24 * 30:
        return '%s天前' % (time_distance / 60 / 60 / 24)
    else:
        return time.strftime("%m-%d", time.localtime(timestamp))