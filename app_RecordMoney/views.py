# 在下方引入需要的库
from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import datetime
import json

from .models import FirstLevelAccountTitles, SecondLevelAccountTitles, ThirdLevelAccountTitles, Accounts, RecordMoney
from .forms import NewRecordMoneyForm, FliteRecordsForm


# 请在下方创建视图 
def ajax_load_FLAT(request):
    """获取一级科目的选项数据"""

    FLAT = FirstLevelAccountTitles.objects.all()

    res = []
    for item in FLAT:
        res.append([item.id, item.first_level_account_titles])

    return JsonResponse({'trading_FLAT':res})

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
    """收支记录的首页,根据选择的时间范围筛选记录进行展示"""

    record_moneys = RecordMoney.objects.filter().order_by("-trading_date", "-record_time")[:10]
    time_filter_label = "最近10条收支记录如下："

    if request.method == 'GET':
        #获取特定时间范围内的收支记录数据
        time_filter = request.GET.get('time_filter')

        today = datetime.date.today()

        # 查询今日数据
        if time_filter == '1':
            record_moneys = RecordMoney.objects.filter(
                trading_date=today
            ).order_by("-trading_date", "-record_time")
            time_filter_label = f"{ today.year }年{ today.month }月{ today.day }日的时间记录如下："
        # 查询本周数据
        elif time_filter == '2':
            record_moneys = RecordMoney.objects.filter(
                trading_week=today.isocalendar()[1]
            ).order_by("-trading_date", "-record_time")
            print(record_moneys)
            time_filter_label = f"{ today.year }年第{ today.isocalendar()[1] }周的时间记录如下："
        # 查询本月数据
        elif time_filter == '3':
            record_moneys = RecordMoney.objects.filter(
                trading_date__month=today.month
            ).order_by("-trading_date", "-record_time")
            time_filter_label = f"{ today.year }年{ today.month }月的时间记录如下："
        # 查询本年数据
        elif time_filter == '4':
            record_moneys = RecordMoney.objects.filter(
                trading_date__year=today.year
            ).order_by("-trading_date", "-record_time")
            time_filter_label = f"{ today.year }年的时间记录如下："

    context = {'record_moneys':record_moneys, 'time_filter_label':time_filter_label}

    return render(request, 'RecordMoney/Index.html', context)

def new_record(request):
    """保存新交易的时间及详细描述等信息"""

    record_moneys = RecordMoney.objects.filter().order_by("-trading_date", "-record_time")[:3]

    new_recordmoney = RecordMoney()

    # 如果是一个POST的请求，则对表单数据进行处理
    if request.method == 'POST':
        # 创建一个 NewRecordTimeForm 的 form 类实体，并用 request 中的表单数据初始化它:
        form = NewRecordMoneyForm(request.POST)

        # 检查数据是否有效，如果有效则进行后续处理
        if form.is_valid():
            # 表单中的数据存储在 form.cleaned_data 字典中，通过读取字典中键的值获取表单中的数据，用于查找数据库记录
            #trading_date = datetime.datetime.strptime(form.cleaned_data['trading_date'], '%Y/%m/%d')
            #FLAT = form.cleaned_data['trading_FLAT']
            SLAT_id = form.cleaned_data['trading_SLAT']
            TLAT_id = form.cleaned_data['trading_TLAT']
        
            # 根据表单中的数据获取数据库记录
            #trading_FLAT = FirstLevelAccountTitles.objects.get(first_level_account_titles=FLAT)
            trading_SLAT = SecondLevelAccountTitles.objects.get(id=SLAT_id)
            trading_TLAT = ThirdLevelAccountTitles.objects.get(id=TLAT_id)
            
            # 给 new_recordtime 记录赋值
            new_recordmoney.trading_date = form.cleaned_data['trading_date']
            new_recordmoney.trading_week = form.cleaned_data['trading_date'].isocalendar()[1]   #返回结束日期的星期
            new_recordmoney.trading_period = form.cleaned_data['trading_period']
            new_recordmoney.trading_FLAT = form.cleaned_data['trading_FLAT']
            new_recordmoney.trading_SLAT = trading_SLAT
            new_recordmoney.trading_TLAT = trading_TLAT
            new_recordmoney.trader = form.cleaned_data['trader']
            new_recordmoney.summary = form.cleaned_data['summary']
            new_recordmoney.amount = form.cleaned_data['amount']
            new_recordmoney.account = form.cleaned_data['account']

            # 保存 new_recordmoney 记录
            new_recordmoney.save()
            
            return HttpResponseRedirect(reverse('nsp_RecordMoney:NewRecord'))

    # 如果是一个GET(或其他方式)的请求，我们将创建一个空的表单
    else:
        form = NewRecordMoneyForm()

    return render(request, 'RecordMoney/NewRecord.html', {'form': form, 'record_moneys':record_moneys})

def records(request):
    """收支记录的查询页面,根据筛选器的筛选结果展示记录"""

    seach_dic = {}
    record_moneys = []

    # 如果是一个POST的请求，则对表单数据进行处理
    if request.method == 'POST':
        # 创建一个 NewRecordTimeForm 的 form 类实体，并用 request 中的表单数据初始化它:
        form = FliteRecordsForm(request.POST)

        # 检查数据是否有效，如果有效则进行后续处理
        if form.is_valid():
            # 表单中的数据存储在 form.cleaned_data 字典中，通过读取字典中键的值获取表单中的数据，用于查找数据库记录
            begin_date = form.cleaned_data['begin_date']
            end_date = form.cleaned_data['end_date']
            trading_FLAT = form.cleaned_data['trading_FLAT']
            trading_SLAT = form.cleaned_data['trading_SLAT']
            trading_TLAT = form.cleaned_data['trading_TLAT']
            account = form.cleaned_data['account']

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
            seach_dic['trading_date__range'] = (begin_date, end_date)

            # 配置账户筛选条件
            if account:
                seach_dic['account'] = account

            # 配置一级科目筛选条件
            if trading_FLAT:
                seach_dic['trading_FLAT'] = trading_FLAT
            # 配置二级科目筛选条件
            if trading_SLAT > 0 :
                seach_dic['trading_SLAT'] = trading_SLAT
            # 配置三级科目筛选条件
            if trading_TLAT > 0 :
                seach_dic['trading_TLAT'] = trading_TLAT
        
        # 查询记录        
        record_moneys = RecordMoney.objects.filter(**seach_dic).order_by("-trading_date", "-record_time")
    else:
        form = FliteRecordsForm() 
    
    context = {'record_moneys':record_moneys, 'form':form}

    return render(request, 'RecordMoney/Records.html', context)