# -*- encoding: utf-8 -*-
'''
@File    :   views.py
@Time    :   2020/05/14 10:59:31
@Author  :   Zhu Zefeng 
@Version :   1.0
@Contact :   mingsec@outlook.com
@License :   (C)Copyright 2009-2020, MingsecIndust
@Desc    :   None
'''

# 请在下面输入需要引入的库
from django.shortcuts import render
from django.http import HttpResponse

# 请在下方创建视图.
def homepage(request):
    """网站的主页"""
    return render(request, 'HomePage/HomePage.html')