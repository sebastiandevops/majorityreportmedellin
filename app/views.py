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

def bar_chart(df, x_data, y_data, color=None):
    """Funtion to return plotly object and displays a bar chart

    Args:
        df (data frame): dataframe to be used
        x_data (str): column to display as x axis
        y_data (str): column to display as y axis
        color (str, optional): Bar colors, defaults to None.

    Returns:
        Object: plot_div  object
    """
    if color is not None:
        pivot_data = df.pivot_table(index=[x_data, color],
                                    values=y_data,
                                    aggfunc='sum').reset_index()
    else:
        pivot_data = df.pivot_table(index=x_data,
                                    values=y_data,
                                    aggfunc='sum').reset_index()

    fig = px.bar(pivot_data,
                x=x_data,
                y=y_data,
                color=color,
                template="plotly_white",
                color_discrete_sequence=px.colors.qualitative.Pastel)

    plot_div = plot(fig, output_type='div')
    return plot_div


def line_chart(df, x_data, color, y_data):
    """Funtion to return plotly object and displays a line chart

    Args:
        df (data frame): dataframe to be used
        x_data (str): column to display as x axis
        color (str): y axis to display.
        y_data (str): column to display as y axis


    Returns:
        Object: plot_div  object
    """
    pivot_data = df.pivot_table(index=[x_data, color],
                                values=y_data,
                                aggfunc='sum')

    pivot_data.index.set_names([x_data, color], inplace=True)
    graph = pivot_data.reset_index()
    fig = px.line(graph,
                x=color,
                y=y_data,
                color=x_data,
                template="plotly_white",
                color_discrete_sequence=px.colors.qualitative.Pastel)

    plot_div = plot(fig, output_type='div')
    return plot_div


def index(request):

    data = pd.read_csv('/home/sebastian/Holberton/majorityreportmedellin/app/data.csv')
    context = {'title': 'Majority Report Medellín',
               'subtitle': 'Bienvenidos',
               'tab_1_title':"Acerca de",
               'tab_1_text': 'Esta es una página donde encontrará una forma de visualizar los índices de criminalidad en la ciudad de Medellín de manera interactiva',
               'tab_2_title':"Datos",
               'tab_2_text': "Acá explicamos otra cosa",
               'tab_3_title':"Contacto",
               'tab_3_text': "Estoy inventando",
               'chart_1_title': "Gráfica 1 super bacana",
               'chart_1':"",
               'chart_2_title':"Gráfica 2 más genial",
               'chart_2':""}
    context['chart_1'] = bar_chart(data, 'seguridad.sexo', 'seguridad.cantidad')
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
