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
    path('', views.index, name='RecordMoney'),
    path('NewRecord/', views.NewRecord, name='NewRecord'),
    path('Ajax/LoadIncomeAndExpenditureType/', views.ajax_load_income_and_expenditure_type, name='AjaxLoadIncomeAndExpenditureType'),
    path('Ajax/LoadFirstLevelAccounts/', views.ajax_load_first_level_accounts, name='AjaxLoadFirstLevelAccounts'),
    path('Ajax/LoadDetailAccounts/', views.ajax_load_detail_accounts, name='AjaxLoadDetailAccounts'),
]