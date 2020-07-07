# -*- encoding: utf-8 -*-


# 请在下面输入需要引入的库。
from django.db import models


# 请在下方创建模型。
class EventTypes(models.Model):
    """活动的类型"""
    event_type = models.CharField(verbose_name="活动类型", max_length=10)

    class Meta:
        db_table = "RT_Event_Types"
        verbose_name = "活动类型表"
        verbose_name_plural = "活动类型表"

    def __str__(self):
        return self.event_type


class Events(models.Model):
    """活动的明细类型"""
    event_type = models.ForeignKey(EventTypes, verbose_name="活动类型", on_delete=models.CASCADE)
    event = models.CharField(verbose_name="具体活动", max_length=100)

    class Meta:
        db_table = "RT_Events"
        verbose_name = "具体活动表"
        verbose_name_plural = "具体活动表"
    
    def __str__(self):
        return self.event


class Projects(models.Model):
    """活动所属的项目"""
    project = models.CharField(verbose_name="所属项目", max_length=10)

    class Meta:
        db_table = "RT_Projects"
        verbose_name = "项目名称表"
        verbose_name_plural = "项目名称表"

    def __str__(self):
        return self.project

    
class RecordTime(models.Model):
    """记录事件的时间信息"""
    event_date = models.DateField(verbose_name="活动日期")
    event_week = models.IntegerField(verbose_name="周")
    event_type = models.ForeignKey(EventTypes, verbose_name="活动类型", on_delete=models.CASCADE)
    event = models.ForeignKey(Events, verbose_name="具体活动", on_delete=models.CASCADE)
    project = models.ForeignKey(Projects, verbose_name="所属项目", on_delete=models.CASCADE, blank=True)
    event_description = models.CharField(verbose_name="活动描述", max_length=255)
    begin_time = models.DateTimeField(verbose_name="开始时间", blank=True)
    end_time = models.DateTimeField(verbose_name="结束时间", blank=True)
    time_duration = models.IntegerField(verbose_name="耗用时长(min)")
    record_time = models.DateTimeField(verbose_name="记录时间", auto_now_add=True)

    class Meta:
        db_table = "RT_RecordTime"
        verbose_name = "时间记录表"
        verbose_name_plural = "时间记录表"

    def __str__(self):
        return self.event_description