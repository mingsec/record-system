# -*- encoding: utf-8 -*-


# 请在下面输入需要引入的库
from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import datetime

from .models import EventTypes, Events, Projects, RecordTime
from .forms import NewRecordTimeForm, FliteRecordsForm

# 请在下方创建视图
def ajax_load_event(request):
    """获取活动明细类型的选项数据"""
    event_type_id = request.GET.get('event_type_id')
    events = Events.objects.filter(event_type_id=event_type_id).all()

    res = []
    for item in events:
        res.append([item.id, item.event])
    print(res)
    return JsonResponse({'events':res})

def index(request):
    """时间记录的首页,根据选择的时间范围筛选记录进行展示"""
    record_times = RecordTime.objects.filter().order_by("-end_time", "-record_time")[:10]
    time_filter_label = "最近10条时间记录如下："

    if request.method == 'GET':
        #获取特定时间范围内的收支记录数据
        time_filter = request.GET.get('time_filter')

        today = datetime.date.today()

        # 查询今日数据
        if time_filter == '1':
            record_times = RecordTime.objects.filter(
                event_date=today
            ).order_by("-end_time", "-record_time")
            time_filter_label = f"{ today.year }年{ today.month }月{ today.day }日的时间记录如下："
        # 查询本周数据
        elif time_filter == '2':
            record_times = RecordTime.objects.filter(
                event_week=today.isocalendar()[1]
            ).order_by("-end_time", "-record_time")
            time_filter_label = f"{ today.year }年第{ today.isocalendar()[1] }周的时间记录如下："
        # 查询本月数据
        elif time_filter == '3':
            record_times = RecordTime.objects.filter(
                event_date__month=today.month
            ).order_by("-end_time", "-record_time")
            time_filter_label = f"{ today.year }年{ today.month }月的时间记录如下："
        # 查询本年数据
        elif time_filter == '4':
            record_times = RecordTime.objects.filter(
                event_date__year=today.year
            ).order_by("-end_time", "-record_time")
            time_filter_label = f"{ today.year }年的时间记录如下："

    context = {'record_times':record_times, 'time_filter_label':time_filter_label}

    return render(request, 'RecordTime/Index.html', context)

def NewRecord(request):
    """记录新活动的时间及详细描述等信息"""

    record_times = RecordTime.objects.filter().order_by("-end_time", "-record_time")[:3]

    new_recordtime = RecordTime()

    # 如果是一个 POST 的请求，则对表单数据进行处理
    if request.method == 'POST':
        # 创建一个 NewRecordTimeForm 的 form 类实体，并用 request 中的表单数据初始化它:
        form = NewRecordTimeForm(request.POST)
        # 检查数据是否有效，如果有效则进行后续处理
        if form.is_valid():
            # 表单中的数据存储在form.cleaned_data字典中，通过读取字典中键的值获取b表单中的数据
            begin_time = form.cleaned_data['begin_time']
            end_time = form.cleaned_data['end_time']
            event_id = form.cleaned_data['event'] 

            # 根据表单中的数据获取数据库记录
            event = Events.objects.get(id=event_id)

            # 给new_recordtime记录赋值
            new_recordtime.event_date = end_time.date()
            new_recordtime.event_week = end_time.isocalendar()[1]   #返回结束日期的星期
            new_recordtime.event_type = form.cleaned_data['event_type']
            new_recordtime.event = event
            new_recordtime.project = form.cleaned_data['project']
            new_recordtime.event_description = form.cleaned_data['event_description']
            new_recordtime.begin_time = begin_time
            new_recordtime.end_time = end_time
            new_recordtime.time_duration = int((end_time - begin_time).total_seconds() / 60)
            
            # 保存new_recordtime记录
            new_recordtime.save()

            return HttpResponseRedirect(reverse('nsp_RecordTime:NewRecord'))

    # 如果是一个GET(或其他方式)的请求，我们将创建一个空的表单
    else:
        form = NewRecordTimeForm()

    return render(request, 'RecordTime/NewRecord.html', {'form': form, 'record_times':record_times})

def records(request):
    """收支记录的查询页面,根据筛选器的筛选结果展示记录"""

    seach_dic = {}
    record_times = []

    # 如果是一个POST的请求，则对表单数据进行处理
    if request.method == 'POST':
        # 创建一个 NewRecordTimeForm 的 form 类实体，并用 request 中的表单数据初始化它:
        form = FliteRecordsForm(request.POST)

        # 检查数据是否有效，如果有效则进行后续处理
        if form.is_valid():
            # 表单中的数据存储在 form.cleaned_data 字典中，通过读取字典中键的值获取表单中的数据，用于查找数据库记录
            begin_date = form.cleaned_data['begin_date']
            end_date = form.cleaned_data['end_date']
            event_type = form.cleaned_data['event_type']
            event = form.cleaned_data['event']
            project = form.cleaned_data['project']

            ''' 配置筛选条件 '''
            # 配置时间筛选条件
            # 如果开始日期未空，则设置为今天
            if begin_date == None:
                begin_date = datetime.date.today()
            # 如果结束日期未空，则设置为今天
            if end_date == None:
                end_date = datetime.date.today()           
            # 按日期大小排序
            if begin_date > end_date:
                mid = end_date
                end_date = begin_date
                begin_date = mid
            seach_dic['event_date__range'] = (begin_date, end_date)

            # 配置项目筛选条件
            if project:
                seach_dic['project'] = project

            # 配置活动类型筛选条件
            if event_type:
                seach_dic['event_type'] = event_type
            # 配置具体活动筛选条件
            if event > 0 :
                seach_dic['event'] = event
        
        # 查询记录        
        record_times = RecordTime.objects.filter(**seach_dic).order_by("-event_date", "-record_time")
    else:
        form = FliteRecordsForm() 
    
    context = {'record_times':record_times, 'form':form}

    return render(request, 'RecordTime/Records.html', context)