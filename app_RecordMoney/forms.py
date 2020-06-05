#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   forms.py
@Time    :   2020/05/26 17:02:02
@Author  :   Zefeng Zhu
@Version :   1.0
@Contact :   mingsec@outlook.com
@License :   (C)Copyright 2009-2020, MingsecIndustry
@Desc    :   None
'''

# 在下方引入需要的库
from django import forms
from .models import Account


class NewRecordMoneyForm(forms.Form): 
    trading_date = forms.CharField(
        label='交易日期', 
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    trading_period = forms.CharField(
        label='所属期间', 
        widget=forms.Select(choices=[(2020,"2020年"), (2019,"2019年")],),
        initial=2020
    )
    trading_type = forms.CharField(
        label='收支类型', 
        widget=forms.Select(choices=[('0',"---请选择---")])
    )
    trading_first_level_account = forms.CharField(
        label='一级科目', 
        widget=forms.Select(choices=[('0',"---请选择---")])
    )
    trading_detail_account = forms.CharField(
        label='二级科目', 
        widget=forms.Select(choices=[('0',"---请选择---")])
    )
    trader = forms.CharField(
        label='交易商家',
        widget=forms.TextInput(attrs={'placeholder':"请输入交易商家"}),
        max_length = 20
    )
    summary = forms.CharField(
        label = '摘要', 
        widget = forms.Textarea(attrs={'rows':'2', 'placeholder':"请对交易事项做简要描述"}),
        max_length = 255
    )
    amount = forms.FloatField(
        label = '金额(元)',
        widget=forms.TextInput(attrs={'placeholder':"请输入交易金额，最多保留2位小数"}),
    )
    trading_account = forms.ModelChoiceField(
        label = '账户', 
        queryset=Account.objects.all(), 
        empty_label="---请选择---"
    )