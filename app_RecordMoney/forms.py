# -*- encoding: utf-8 -*-


# 在下方引入需要的库
from django import forms
from .models import Accounts, FirstLevelAccountTitles
import datetime


class NewRecordMoneyForm(forms.Form): 
    trading_date = forms.DateField(
        label='交易日期',
        #default=datetime.date.today(),
        widget=forms.DateInput(
            attrs={'class':'form-control', 'type':'date'},
            format=(r'%Y-%m-%d'),
        ),
    )

    trading_period = forms.ChoiceField(
        label='所属期间',
        widget=forms.Select(
            attrs={'class':'form-control'},
        ),
        choices=[(2020,"2020年"), (2019,"2019年")],
        initial=(2020,"2020年"),
    )

    trading_FLAT = forms.ModelChoiceField(
        label='一级科目',
        widget=forms.Select(
            attrs={'class':'form-control'},
        ),
        queryset=FirstLevelAccountTitles.objects.all(), 
        empty_label="---请选择---",
    )

    # 由于下拉框的选项值需要从前端动态加载，所以不能选择 ChoiceField ，
    # 否则验证无法通过，即 choices 中的 value 与前端提供的不一致
    trading_SLAT = forms.IntegerField(
        label='二级科目',
        widget=forms.Select(
            attrs={'class':'form-control'},
            choices=[(0, "---请选择---")]
        ),
    )

    # 由于下拉框的选项值需要从前端动态加载，所以不能选择 ChoiceField ，
    # 否则验证无法通过，即 choices 中的 value 与前端提供的不一致
    trading_TLAT = forms.IntegerField(
        label='三级科目', 
        widget=forms.Select(
            attrs={'class':'form-control'},
            choices=[(0, "---请选择---")]
        ), 
    )

    trader = forms.CharField(
        label='交易商家',
        widget=forms.TextInput(
            attrs={'class':'form-control', 'placeholder':"请输入商家名称"}
        ),
        max_length=20
    )

    summary = forms.CharField(
        label='摘要', 
        widget=forms.Textarea(
            attrs={'class':'form-control', 'rows':'3', 'placeholder':"请简要描述交易事项..."}
        ),
        max_length = 255
    )
    
    amount = forms.DecimalField(
        label='金额(元)',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder':"系统自动保留2位小数"}
        ),
        decimal_places=2
    )

    account = forms.ModelChoiceField(
        label = '交易账户',
        widget=forms.Select(
            attrs={'class':'form-control'}
        ),
        queryset=Accounts.objects.all(), 
        empty_label="---请选择---",
    )


class FliterRecordsForm(forms.Form):
    begin_date = forms.DateField(
        label='开始日期',
        #default=datetime.date.today(),
        widget=forms.DateInput(
            attrs={'class':'form-control', 'type':'date'},
            #format=(r'%Y-%m-%d'),
        ),
    )

    end_date = forms.DateField(
        label='结束日期',
        #default=datetime.date.today(),
        widget=forms.DateInput(
            attrs={'class':'form-control', 'type':'date'},
            #format=(r'%Y-%m-%d'),
        ),
    )

    trading_FLAT = forms.ModelChoiceField(
        label='一级科目',
        widget=forms.Select(
            attrs={'class':'form-control'},
        ),
        queryset=FirstLevelAccountTitles.objects.all(), 
        empty_label="---请选择---",
    )

    # 由于下拉框的选项值需要从前端动态加载，所以不能选择 ChoiceField ，
    # 否则验证无法通过，即 choices 中的 value 与前端提供的不一致
    trading_SLAT = forms.IntegerField(
        label='二级科目',
        widget=forms.Select(
            attrs={'class':'form-control'},
            choices=[(0, "---请选择---")]
        ),
    )

    # 由于下拉框的选项值需要从前端动态加载，所以不能选择 ChoiceField ，
    # 否则验证无法通过，即 choices 中的 value 与前端提供的不一致
    trading_TLAT = forms.IntegerField(
        label='三级科目', 
        widget=forms.Select(
            attrs={'class':'form-control'},
            choices=[(0, "---请选择---")]
        ), 
    ) 