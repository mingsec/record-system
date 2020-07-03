#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   views.py
@Time    :   2020/05/14 11:05:52
@Author  :   Zhu Zefeng 
@Version :   1.0
@Contact :   mingsec@outlook.com
@License :   (C)Copyright 2009-2020, MingsecIndust
@Desc    :   None
'''

# 请在下面输入需要引入的库
from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import datetime

from .models import EventType, Event, Project, RecordTime
from .forms import NewRecordTimeForm

# 请在下方创建视图
def ajax_load_event_type(request):
    """获取活动大类的选项数据"""
    event_types = EventType.objects.all()
    print(event_types)
    res = []
    for item in event_types:
        print(item)
        res.append([item.id, item.event_type])

    return JsonResponse({'event_types':res})

def ajax_load_event(request):
    """获取活动明细类型的选项数据"""
    event_type_id = request.GET.get('event_type_id', None)
    events = Event.objects.filter(event_type_id=event_type_id).all()
    print(events)
    res = []
    for item in events:
        print(item)
        res.append([item.id, item.event])

    return JsonResponse({'events':res})

def index(request):
    """时间记录的首页,根据选择的时间范围选择记录进行展示"""
    record_times = RecordTime.objects.filter().order_by("-record_time")[:10]
    time_filter_label = "最近10条时间记录如下："

    if request.method == 'GET':
        #获取特定时间范围内的收支记录数据
        time_filter = request.GET.get('time_filter')

        today = datetime.date.today()
        current_year = today.year
        current_month = today.month
        current_week = today.isocalendar()[1]
        current_day = today.day
      
        if time_filter == '1':
            record_times = RecordTime.objects.filter(
                event_year=current_year,
                event_month=current_month,
                event_day=current_day
            ).order_by("-record_time")
            time_filter_label = "%s年%s月%s日的时间记录如下：" % (current_year, current_month, current_day)
        elif time_filter == '2':
            record_times = RecordTime.objects.filter(
                event_year=current_year,
                event_week=current_week,
            ).order_by("-record_time")
            time_filter_label = "%s年第%s周的时间记录如下：" % (current_year,current_week )
        elif time_filter == '3':
            record_times = RecordTime.objects.filter(
                event_year=current_year,
                event_month=current_month,
            ).order_by("-record_time")
            time_filter_label = "%s年%s月的时间记录如下：" % (current_year, current_month)
        elif time_filter == '4':
            record_times = RecordTime.objects.filter(
                event_year=current_year,
            ).order_by("-record_time")
            time_filter_label = "%s年的时间记录如下：" % (current_year)

    context = {'record_times':record_times, 'time_filter_label':time_filter_label}

    return render(request, 'RecordTime/Index.html', context)

def NewRecord(request):
    """记录新的活动时间及详细描述"""
    new_recordtime = RecordTime()

    # 如果是一个 POST 的请求，则对表单数据进行处理
    if request.method == 'POST':
        # 创建一个 NewRecordTimeForm 的 form 类实体，并用 request 中的表单数据初始化它:
        form = NewRecordTimeForm(request.POST)
        # 检查数据是否有效，如果有效则进行后续处理
        if form.is_valid():
            # 表单中的数据存储在form.cleaned_data字典中，通过读取字典中键的值获取b表单中的数据
            begin_time = datetime.datetime.strptime(form.cleaned_data['begin_time'].replace('T',' '),'%Y-%m-%d %H:%M')
            end_time = datetime.datetime.strptime(form.cleaned_data['end_time'].replace('T',' '),'%Y-%m-%d %H:%M')
            event_type_id = form.cleaned_data['event_type'] 
            event_id = form.cleaned_data['event'] 
            event_description =form.cleaned_data['event_description']
            project = form.cleaned_data['project']

            # 根据表单中的数据获取数据库记录
            event_type = EventType.objects.get(id=event_type_id)
            event = Event.objects.get(id=event_id)

            # 给new_recordtime记录赋值
            new_recordtime.event_year = end_time.year               #返回结束日期的月份
            new_recordtime.event_month = end_time.month             #返回结束日期的月份
            new_recordtime.event_day = end_time.day                 #返回结束日期的日期
            new_recordtime.event_week = end_time.isocalendar()[1]   #返回结束日期的星期
            new_recordtime.event_type = event_type    
            new_recordtime.event = event
            new_recordtime.event_description = event_description
            new_recordtime.begin_time = begin_time
            new_recordtime.end_time = end_time
            new_recordtime.time_duration = int((end_time - begin_time).total_seconds() / 60)
            new_recordtime.project = project
        
            # 保存new_recordtime记录
            new_recordtime.save()

            return HttpResponseRedirect(reverse('nsp_RecordTime:NewRecord'))

    # 如果是一个GET(或其他方式)的请求，我们将创建一个空的表单
    else:
        form = NewRecordTimeForm()

    return render(request, 'RecordTime/NewRecord.html', {'form': form})
