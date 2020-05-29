#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   admin.py
@Time    :   2020/05/14 11:28:07
@Author  :   Zhu Zefeng 
@Version :   1.0
@Contact :   mingsec@outlook.com
@License :   (C)Copyright 2009-2020, MingsecIndust
@Desc    :   None
'''

# 请在下面输入需要引入的库
from django.contrib import admin
from .models import EventType, Event, Project, RecordTime


admin.site.site_header = 'Record System后台管理'  # 此处设置页面显示标题
admin.site.site_title = '后台管理'                # 此处设置页面头部标题
 

class EventTypeAdmin(admin.ModelAdmin):
    """自定义活动大类的字段的展示形式"""
    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('id', 'event_type')
    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('event_type',)
    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('id',)


class EventAdmin(admin.ModelAdmin):
    """自定义活动详细类型的字段的展示形式"""
    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('id', 'event_type', 'event',)
    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('event',)
    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('event_type', 'id')
    # 设置过滤器
    list_filter =('event_type',) 
    # 设置搜索字段
    search_fields =('event',) 
    # 设置显示的字段的先后顺序
    fields =  (('event_type', 'event'),)


class RecordTimeAdmin(admin.ModelAdmin):
    """自定义活动记录的字段的展示形式"""
    #listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = (
        'id',
        'event_year',
        'event_month',
        'event_day',
        'event_week',
        'event_type',
        'event',
        'event_description',
        'time_duration',
        'project',
        'record_time'
    )
    #设置哪些字段可以点击进入编辑界面
    list_display_links = ('id', 'event_description')
    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('record_time', '-id')
    # 设置过滤器
    list_filter =('event_type', 'event', 'project', 'event_week',) 
    # 设置搜索字段
    search_fields =('event_description',) 
    # 详细时间分层筛选　
    date_hierarchy = 'record_time'
    
    # 详细字段分组进行展示 //用()将字段放在同一行展示
    fieldsets = [
        ('活动的日期信息', {'fields': [('event_year','event_month','event_day', 'event_week')]}),
        ('活动的时间信息', {'fields': [('begin_time','end_time','time_duration')]}),
        ('活动的内容信息', {'fields': [('event_type', 'event', 'project'),'event_description']}),
    ]


class ProjectAdmin(admin.ModelAdmin):
    """自定义所属项目的字段的展示形式"""
    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('id', 'project')
    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('project',)
    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('id',)


# 在下方注册应用程序的模型
admin.site.register(EventType, EventTypeAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(RecordTime, RecordTimeAdmin)