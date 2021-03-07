# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from re import X
import pandas as pd
import plotly.express as px
from plotly.offline import plot
import os
path = os.path.dirname(__file__)
bar_chart = __import__('/plotly_functions.py').bar_chart
line_chart = __import__('/plotly_functions.py').line_chart

def index(request):

    data = pd.read_csv(path + '/data.csv')
    context = {'title': 'Majority Report Medellín',
               'subtitle': 'Bienvenidos',
               'tab_1_title':"Acerca de",
               'tab_1_text': 'Esta es una página donde encontrará una forma de visualizar los índices de criminalidad en la ciudad de Medellín de manera interactiva',
               'tab_2_title':"Datos",
               'tab_2_text': "Acá explicamos otra cosa",
               'tab_3_title':"Contacto",
               'tab_3_text': "Estoy inventando",
               'chart_1_title': "Cantidad de hurtos a personas por sexo de la víctima",
               'chart_1':"",
               'chart_2_title':"Cantidad de hurtos a personas desde el año 2003 mes a mes",
               'chart_2':""}
    context['chart_1'] = bar_chart(data, 'sexo', 'cantidad')
    context['chart_2'] = line_chart(data, 'año', 'mes', 'cantidad')
    context['segment'] = 'index'

    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))

def medellincharts(request):
    #leo csv
    data = pd.read_csv('/home/sebastian/Holberton/majorityreportmedellin/app/data.csv')
    #creo key en context que contengan cada una de las fgráficas
    context = {}
    #ex: context['bar_chart_1'] = bar_chart(data, 'seguridad.sexo', 'seguridad.cantidad')
    context['chart_1'] = bar_chart(data, 'seguridad.sexo', 'seguridad.cantidad')
    context['segment'] = 'medellincharts'

    html_template = loader.get_template( 'medellincharts.html' )
    return HttpResponse(html_template.render(context, request))

#@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template

        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))
