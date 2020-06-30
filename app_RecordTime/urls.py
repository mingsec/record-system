#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   urls.py
@Time    :   2020/05/14 11:06:49
@Author  :   Zhu Zefeng 
@Version :   1.0
@Contact :   mingsec@outlook.com
@License :   (C)Copyright 2009-2020, MingsecIndust
@Desc    :   None
'''

# 请在下面输入需要引入的库
from django.urls import path
from . import views

app_name='nsp_RecordTime'

urlpatterns = [
    path('Index', views.index, name='RecordTime'),
    path('NewRecord/', views.NewRecord, name='NewRecord'),
    path('Ajax/LoadEventTpye/', views.ajax_load_event_type, name='AjaxLoadEventType'),
    path('Ajax/LoadEvent/', views.ajax_load_event, name='AjaxLoadEvent'),
]