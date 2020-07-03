#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   urls.py
@Time    :   2020/05/26 15:53:34
@Author  :   Zefeng Zhu
@Version :   1.0
@Contact :   mingsec@outlook.com
@License :   (C)Copyright 2009-2020, MingsecIndustry
@Desc    :   None
'''

# 在下方引入需要的库
from django.urls import path
from . import views

app_name='nsp_RecordMoney'

urlpatterns = [
    path('Index/', views.index, name='RecordMoney'),
    path('NewRecord/', views.new_record, name='NewRecord'),
    path('DataVisual/', views.data_visual, name='DataVisual'),
    path('Ajax/LoadSLAT/', views.ajax_load_SLAT, name='AjaxLoadSLAT'),
    path('Ajax/LoadTLAT/', views.ajax_load_TLAT, name='AjaxLoadTLAT'),
]