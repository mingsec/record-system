#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   urls.py
@Time    :   2020/05/14 10:59:13
@Author  :   Zhu Zefeng 
@Version :   1.0
@Contact :   mingsec@outlook.com
@License :   (C)Copyright 2009-2020, MingsecIndust
@Desc    :   None
'''

# 请在下面输入需要引入的库
from django.urls import path
from . import views

app_name='nsp_HomePage'

urlpatterns = [
    path('', views.homepage, name='HomePage'),
]