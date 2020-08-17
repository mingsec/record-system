# 请在下面输入需要引入的库
from django.urls import path
from . import views

app_name='nsp_RecordTime'

urlpatterns = [
    path('Index', views.index, name='RecordTime'),
    path('NewRecord/', views.NewRecord, name='NewRecord'),
    path('Ajax/LoadEvent/', views.ajax_load_event, name='AjaxLoadEvent'),
]