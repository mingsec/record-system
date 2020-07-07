# -*- encoding: utf-8 -*-


# 请在下面输入需要引入的库
from django import forms
from .models import EventTypes, Projects


class NewRecordTimeForm(forms.Form): 
    '''记录时间的表单'''
    begin_time = forms.DateTimeField(
        label='开始时间', 
        widget=forms.DateTimeInput(
            attrs={'class':'form-control', 'type': 'datetime-local'},
            #format=('%Y/%m/%d %H:%M'),
            
        ),
        input_formats=['%Y-%m-%dT%H:%M']
    )

    end_time = forms.DateTimeField(
        label='结束时间',
        widget=forms.DateTimeInput(
            attrs={'class':'form-control', 'type': 'datetime-local'},
            #format=('%Y-%m-%d %H:%M'),
        ),
        input_formats=['%Y-%m-%dT%H:%M']
    )

    event_type = forms.ModelChoiceField(
        label='请选择活动类型', 
        widget=forms.Select(
            attrs={'class':'form-control'},
        ),
        queryset=EventTypes.objects.all(), 
        empty_label="---请选择---",
    )

    event = forms.IntegerField(
        label='请选择具体活动', 
        widget=forms.Select(
            attrs={'class':'form-control'}, 
            choices=[(0,"---请选择---")],
        ),
    )

    project = forms.ModelChoiceField(
        label='请选择所属项目', 
        widget=forms.Select(
            attrs={'class':'form-control'}
        ),
        queryset=Projects.objects.all(), 
        empty_label="---请选择---",
        required=False,
    )
    
    event_description = forms.CharField(
        label='活动描述', 
        widget=forms.Textarea(
            attrs={'class':'form-control', 'rows':'3', 'placeholder':"请简要描述活动事项"},
        ),
        max_length = 255
    )