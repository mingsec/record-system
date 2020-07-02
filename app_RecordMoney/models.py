# -*- encoding: utf-8 -*-


# 在下方引入需要的库
from django.db import models


# 请在下方创建模型。
class FirstLevelAccountTitles(models.Model):
    """收入与支出项目的一级科目"""
    first_level_account_titles = models.CharField(verbose_name="一级科目", max_length=10)

    def __str__(self):
        return self.first_level_account_titles


class SecondLevelAccountTitles(models.Model):
    """收入与支出项目的二级科目""" 
    first_level_account_titles = models.ForeignKey(FirstLevelAccountTitles, on_delete=models.CASCADE)
    second_level_account_titles = models.CharField(verbose_name="二级科目", max_length=10)

    def __str__(self):
        return self.second_level_account_titles


class ThirdLevelAccountTitles(models.Model):
    """收入与支出项目的三级科目"""
    first_level_account_titles = models.ForeignKey(FirstLevelAccountTitles, on_delete=models.CASCADE)
    second_level_account_titles = models.ForeignKey(SecondLevelAccountTitles, on_delete=models.CASCADE)
    third_level_account_titles = models.CharField(verbose_name="三级科目", max_length=10)
    
    def __str__(self):
        return self.third_level_account_titles


class Accounts(models.Model):
    """收支交易发生的账户"""
    accounts = models.CharField(verbose_name="交易账户", max_length=10)

    def __str__(self):
        return self.accounts

    
class RecordMoney(models.Model):
    """记录交易的时间、内容、金额等信息"""
    trading_date = models.DateField(verbose_name="交易日期")
    #trading_year = models.IntegerField(verbose_name="年")
    #trading_month = models.IntegerField(verbose_name="月")
    trading_week = models.IntegerField(verbose_name="周")
    #trading_day = models.IntegerField(verbose_name="日")
    trading_period = models.IntegerField(verbose_name="所属期间")
    trading_FLAT = models.ForeignKey(FirstLevelAccountTitles, on_delete=models.CASCADE, verbose_name="一级科目")
    trading_SLAT = models.ForeignKey(SecondLevelAccountTitles, on_delete=models.CASCADE, verbose_name="二级科目")
    trading_TLAT = models.ForeignKey(ThirdLevelAccountTitles, on_delete=models.CASCADE, verbose_name="三级科目")
    trader = models.CharField(verbose_name="交易商家", max_length=20)
    summary = models.CharField(verbose_name="摘要", max_length=255)
    amount = models.DecimalField(verbose_name="金额(元)", max_digits=12, decimal_places=2)
    trading_account = models.ForeignKey(Accounts, on_delete=models.CASCADE, verbose_name="交易账户")
    record_time = models.DateTimeField("记录时间", auto_now_add=True)

    def __str__(self):
        return self.summary