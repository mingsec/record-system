#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   models.py
@Time    :   2020/05/14 11:11:05
@Author  :   Zhu Zefeng 
@Version :   1.0
@Contact :   mingsec@outlook.com
@License :   (C)Copyright 2009-2020, MingsecIndust
@Desc    :   None
'''

# 请在下面输入需要引入的库。
from django.db import models


# 请在下方创建模型。
class EventType(models.Model):
    """活动的大类"""
    event_type = models.CharField("活动类型", max_length=10)

    def __str__(self):
        return self.event_type


class Event(models.Model):
    """活动的明细类型"""
    event = models.CharField("具体活动", max_length=100)
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE)

    def __str__(self):
        return self.event


class Project(models.Model):
    """活动所属的项目"""
    project = models.CharField("所属项目", max_length=10)

    def __str__(self):
        return self.project

    
class RecordTime(models.Model):
    """记录事件的时间信息"""
    event_year = models.IntegerField("年")
    event_month = models.IntegerField("月")
    event_day = models.IntegerField("日")
    event_week = models.IntegerField("周")
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE, verbose_name="活动类型")
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name="具体活动")
    event_description = models.CharField("活动描述", max_length=255)
    begin_time = models.DateTimeField("开始时间")
    end_time = models.DateTimeField("结束时间")
    time_duration = models.IntegerField("耗用时长(min)")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name="所属项目", null=True)
    record_time = models.DateTimeField("记录时间", auto_now_add=True)

    def __str__(self):
        return self.event_description