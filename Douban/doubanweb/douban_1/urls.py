#!/user/bin/env python3
#-*-coding:utf-8 -*-
from django.urls import path
from . import views
app_name = 'douban_1'



urlpatterns = [
    path('',views.index,name = 'index'),

]