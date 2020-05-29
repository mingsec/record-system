#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   admin.py
@Time    :   2020/05/26 17:39:54
@Author  :   Zefeng Zhu
@Version :   1.0
@Contact :   mingsec@outlook.com
@License :   (C)Copyright 2009-2020, MingsecIndustry
@Desc    :   None
'''

# 在下方引入需要的库
from django.contrib import admin
from .models import IncomeAndExpenditureType, FirstLevelAccounts, DetailAccounts, Account, RecordMoney


class IncomeAndExpenditureTypeAdmin(admin.ModelAdmin):
    """自定义收支大类的字段的展示形式"""
    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('id', 'income_and_expenditure_type', )
    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('income_and_expenditure_type',)
    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('id',)


class FirstLevelAccountsAdmin(admin.ModelAdmin):
    """自定义一级科目的字段的展示形式"""
    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('id', 'income_and_expenditure_type', 'first_level_account',)
    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('first_level_account',)
    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('income_and_expenditure_type', 'id')
    # 设置显示的字段的先后顺序
    fields =  (('income_and_expenditure_type', 'first_level_account'),)


class DetailAccountsAdmin(admin.ModelAdmin):
    """自定义明细科目的字段的展示形式"""
    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('id', 'income_and_expenditure_type', 'first_level_account', 'detail_account')
    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('detail_account',)
    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('income_and_expenditure_type', 'first_level_account', 'id')
    # 设置显示的字段的先后顺序
    fields =  (('income_and_expenditure_type', 'first_level_account','detail_account'),)


class AccountAdmin(admin.ModelAdmin):
    """自定义账户的字段的展示形式"""
    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('id', 'account', )
    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('account',)
    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('id',)


class RecordTimeAdmin(admin.ModelAdmin):
    """自定义活动记录的字段的展示形式"""
    #listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = (
        'id',
        'trading_year',
        'trading_month',
        'trading_day',
        'trading_week',
        'trading_period',
        'trading_type',
        'trading_first_level_account',
        'trading_detail_account',
        'trading_account',
        'amount',
        'trader',
        'summary',
        'record_time'
    )
    #设置哪些字段可以点击进入编辑界面
    list_display_links = (
        'trading_type',
        'trading_first_level_account',
        'trading_detail_account',
        'trading_account',
        'amount',
        'trader',
        'summary',
    )
    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('record_time', '-id')
    # 设置过滤器
    list_filter =(
        'trading_type',
        'trading_first_level_account',
        'trading_detail_account', 
        'trading_account',
    ) 
    # 设置搜索字段
    #search_fields =('event_description',) 
    # 详细时间分层筛选　
    date_hierarchy = 'record_time'
    
    # 详细字段分组进行展示 //用()将字段放在同一行展示
    fieldsets = [
        ('交易发生日期', {'fields': [('trading_year','trading_month','trading_day', 'trading_week','trading_period')]}),
        ('交易科目信息', {'fields': [('trading_type','trading_first_level_account','trading_detail_account')]}),
        ('交易账户信息', {'fields': [('trading_account','amount')]}),
        ('交易详细内容', {'fields': [('trader', 'summary')]}),
    ]


# Register your models here.
admin.site.register(IncomeAndExpenditureType, IncomeAndExpenditureTypeAdmin)
admin.site.register(FirstLevelAccounts, FirstLevelAccountsAdmin)
admin.site.register(DetailAccounts, DetailAccountsAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(RecordMoney, RecordTimeAdmin)