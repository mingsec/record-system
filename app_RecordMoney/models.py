#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   models.py
@Time    :   2020/05/26 16:14:26
@Author  :   Zefeng Zhu
@Version :   1.0
@Contact :   mingsec@outlook.com
@License :   (C)Copyright 2009-2020, MingsecIndustry
@Desc    :   记录收支的数据库模型
'''

# 在下方引入需要的库
from django.db import models


# 请在下方创建模型。
class IncomeAndExpenditureType(models.Model):
    """收入与支出项目的分类"""
    income_and_expenditure_type = models.CharField("收支类型", max_length=10)

    def __str__(self):
        return self.income_and_expenditure_type


class FirstLevelAccounts(models.Model):
    """收入与支出项目的一级科目""" 
    income_and_expenditure_type = models.ForeignKey(IncomeAndExpenditureType, on_delete=models.CASCADE)
    first_level_account = models.CharField("一级科目", max_length=10)

    def __str__(self):
        return self.first_level_account


class DetailAccounts(models.Model):
    """收入与支出项目的明细科目"""
    income_and_expenditure_type = models.ForeignKey(IncomeAndExpenditureType, on_delete=models.CASCADE)
    first_level_account = models.ForeignKey(FirstLevelAccounts, on_delete=models.CASCADE)
    detail_account = models.CharField("明细科目", max_length=10)
    
    def __str__(self):
        return self.detail_account


class Account(models.Model):
    """收支交易发生的账户"""
    account = models.CharField("账户", max_length=10)

    def __str__(self):
        return self.account

    
class RecordMoney(models.Model):
    """记录交易的时间、内容、金额等信息"""
    trading_year = models.IntegerField("年")
    trading_month = models.IntegerField("月")
    trading_week = models.IntegerField("周")
    trading_day = models.IntegerField("日")
    trading_period = models.IntegerField("所属期间")
    trading_type = models.ForeignKey(
        IncomeAndExpenditureType,
        on_delete=models.CASCADE,
        verbose_name="收支类型"
    )
    trading_first_level_account = models.ForeignKey(
        FirstLevelAccounts,
        on_delete=models.CASCADE,
        verbose_name="一级科目"
    )
    trading_detail_account = models.ForeignKey(
        DetailAccounts,
        on_delete=models.CASCADE,
        verbose_name="明细科目"
    )
    trader = models.CharField("交易商家", max_length=20)
    summary = models.CharField("摘要", max_length=255)
    amount = models.DecimalField("金额(元)", max_digits=12, decimal_places=2)
    trading_account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE, 
        verbose_name="账户"
    )
    record_time = models.DateTimeField("记录时间", auto_now_add=True)

    def __str__(self):
        return self.summary