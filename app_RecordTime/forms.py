#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   forms.py
@Time    :   2020/05/14 16:17:28
@Author  :   Zhu Zefeng 
@Version :   1.0
@Contact :   mingsec@outlook.com
@License :   (C)Copyright 2009-2020, MingsecIndust
@Desc    :   None
'''

# 请在下面输入需要引入的库
from django import forms
from .models import EventType, Event, Project, RecordTime


class NewRecordTimeForm(forms.Form): 
    '''记录时间的表单'''
    begin_time = forms.CharField(
        label = '活动开始时间：', 
        widget = forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )
    end_time   = forms.CharField(
        label = '活动结束时间：',
        widget = forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )
    event_type = forms.CharField(
        label = '请选择活动的大类：', 
        widget = forms.Select(choices=[('0',"---请选择---")])
    )
    event = forms.CharField(
        label = '请选择活动的明细类：', 
        widget = forms.Select(choices=[('0',"---请选择---")])
    )
    event_description = forms.CharField(
        label = '活动描述：', 
        widget = forms.Textarea(attrs={'rows':'5', 'placeholder':"请对活动事项做简要描述"}),
        max_length = 255
    )
    project = forms.ModelChoiceField(
        label = '请选择活动所属的项目：', 
        queryset=Project.objects.all(), 
        empty_label="---请选择---",
        required=False,
    )

 