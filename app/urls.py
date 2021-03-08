# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from majorityreportmedellin.app.views import medellincharts
from django.urls import path, re_path
from app import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('', views.medellincharts, name='medellincharts'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
