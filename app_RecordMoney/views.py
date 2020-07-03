# -*- encoding: utf-8 -*-
'''
@File    :   views.py
@Time    :   2020/05/26 15:53:56
@Author  :   Zefeng Zhu
@Version :   1.0
@Contact :   mingsec@outlook.com
@License :   (C)Copyright 2009-2020, MingsecIndustry
@Desc    :   None
'''

# 在下方引入需要的库
from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import RequestContext
#from django.core import serializers
from sqlalchemy import create_engine
import datetime
import json
import pandas

from .models import FirstLevelAccountTitles, SecondLevelAccountTitles, ThirdLevelAccountTitles, Accounts, RecordMoney
from .forms import NewRecordMoneyForm


# 请在下方创建视图 
def ajax_load_SLAT(request):
    """获取二级科目的选项数据"""
    FLAT_id = request.GET.get('FLAT_id')

    SLAT = SecondLevelAccountTitles.objects.filter(first_level_account_titles_id=FLAT_id).all()

    res = []
    for item in SLAT:
        res.append([item.id, item.second_level_account_titles])
       
    return JsonResponse({'trading_SLAT':res})

def ajax_load_TLAT(request):
    """获取三级科目的选项数据"""
    SLAT_id = request.GET.get('SLAT_id')
    TLAT = ThirdLevelAccountTitles.objects.filter(second_level_account_titles_id=SLAT_id).all()

    res = []
    for item in TLAT:
        res.append([item.id, item.third_level_account_titles])

    return JsonResponse({'trading_TLAT':res})

def index(request):
    """收支记录的首页,根据选择的时间范围选择记录进行展示"""
    record_moneys = RecordMoney.objects.filter().order_by("-trading_date")[:10]
    time_filter_label = "最近10条收支记录如下："

    if request.method == 'GET':
        #获取特定时间范围内的收支记录数据
        time_filter = request.GET.get('time_filter')

        today = datetime.date.today()

        # 查询今日数据
        if time_filter == '1':
            record_moneys = RecordMoney.objects.filter(
                trading_date=today
            ).order_by("-trading_date")
            time_filter_label = f"{ today.year }年{ today.month }月{ today.day }日的时间记录如下："
        # 查询本周数据
        elif time_filter == '2':
            # 计算当前日期是本周第几天
            day_num = today.isoweekday()
            # 计算当前日期所在周一
            monday = (today - datetime.timedelta(days=day_num))
            # 查询一周内的数据
            record_moneys = RecordMoney.objects.filter(
                trading_date__range=(today, monday)
            ).order_by("-trading_date")
            time_filter_label = f"{ today.year }年第{ today.isocalendar()[1] }周的时间记录如下："
        # 查询本月数据
        elif time_filter == '3':
            record_moneys = RecordMoney.objects.filter(
                trading_date__month=today.month
            ).order_by("-trading_date")
            time_filter_label = f"{ today.year }年{ today.month }月的时间记录如下："
        # 查询本年数据
        elif time_filter == '4':
            record_moneys = RecordMoney.objects.filter(
                trading_date__year=today.year
            ).order_by("-trading_date")
            time_filter_label = f"{ today.year }年的时间记录如下："

    context = {'record_moneys':record_moneys, 'time_filter_label':time_filter_label}

    return render(request, 'RecordMoney/Index.html', context)

def new_record(request):
    """保存新的交易的时间及详细描述"""

    new_recordmoney = RecordMoney()

    # 如果是一个POST的请求，则对表单数据进行处理
    if request.method == 'POST':
        # 创建一个 NewRecordTimeForm 的 form 类实体，并用 request 中的表单数据初始化它:
        form = NewRecordMoneyForm(request.POST)
        # 检查数据是否有效，如果有效则进行后续处理
        
        
        if form.is_valid():
            print(form.cleaned_data['trading_FLAT'])
            print(form.cleaned_data['trading_SLAT'])
        '''
            # 表单中的数据存储在 form.cleaned_data 字典中，通过读取字典中键的值获取表单中的数据
            print("test")
            trading_date = datetime.datetime.strptime(form.cleaned_data['trading_date'],'%Y-%m-%d')
            print(trading_date)
            FLAT_id = form.cleaned_data['trading_FLAT']
            SLAT_id = form.cleaned_data['trading_SLAT']
            TLAT_id = form.cleaned_data['trading_TLAT']
            
            

            # 根据表单中的数据获取数据库记录
            trading_FLAT = FirstLevelAccountTitles.objects.get(id=FLAT_id)
            trading_SLAT = SecondLevelAccountTitles.objects.get(id=SLAT_id)
            trading_TLAT = ThirdLevelAccountTitles.objects.get(id=TLAT_id)
            
            # 给 new_recordtime 记录赋值
            new_recordmoney.trading_date = trading_date
            new_recordmoney.trading_week = trading_date.isocalendar()[1]   #返回结束日期的星期
            new_recordmoney.trading_period = form.cleaned_data['trading_period']
            new_recordmoney.trading_FLAT = trading_FLAT
            new_recordmoney.trading_SLAT = trading_SLAT
            new_recordmoney.trading_TLAT = trading_TLAT
            new_recordmoney.trader = form.cleaned_data['trader']
            new_recordmoney.summary = form.cleaned_data['summary']
            new_recordmoney.amount = form.cleaned_data['amount']
            new_recordmoney.account = form.cleaned_data['account']
        '''
            #print(new_recordmoney)
            # 保存 new_recordmoney 记录
            #new_recordmoney.save()
            
            #return HttpResponseRedirect(reverse('nsp_RecordMoney:NewRecord'))

    # 如果是一个GET(或其他方式)的请求，我们将创建一个空的表单
    else:
        form = NewRecordMoneyForm()

    return render(request, 'RecordMoney/NewRecord.html', {'form': form})

def data_visual(request):
    """以可视化的方式查看收支记录数据"""
        
    # 创建数据库连接引擎
    # 数据库类型://用户名:口令@机器地址:端口号/数据库名
    engine = create_engine('postgresql://postgres:330715@localhost:5432/record-system')

    # 标准sql查询语句，此处为测试返回数据库app_RecordMoney_recordmoney表的数据条目，之后可以用python处理字符串的方式动态扩展
    sql = 'Select count(*) from public."app_RecordMoney_recordmoney"'

    # 将sql语句结果读取至Pandas Dataframe
    df = pandas.read_sql_query(sql, engine)

    # 设置上下文菜单
    context = {'data':df}

    return render(request, 'RecordMoney/Display.html', context)