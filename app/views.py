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
from app.plotly_functions import bar_chart
from app.plotly_functions import line_chart
from app.plotly_functions import bar_chart_animation
import os

path = os.path.dirname(__file__)
data = pd.read_csv(path + '/data.csv')

instructions = "La librería utilizada para desplegar las gráficas"\
               " es Plotly, la cual es una herramientas de visualización y"\
               " análisis de datos en línea de manera interactiva."\
               " Plotly proporciona herramientas de gráficos, análisis y"\
               " estadísticas en línea para individuos y colaboración, así"\
               " como bibliotecas de gráficos científicos para Python, R,"\
               " MATLAB, Perl, Julia, Arduino y REST.\n"\
               " En las gráficas de barras podrá seleccionar el año"\
               " a visualizar deslizando el cursor por la barra inferior,"\
               " igualmente podrá activar el zoom desde los botónes"\
               " superiores o marcando la zona a encuadrar con el cursor.\n"\
               "Las gráficas de línes contienen una columna donde se"\
               " especifican los años a los que corresponde el color de cada"\
               " linea, esta columna le permitira seleccionar o deseleccionar"\
               " los años a visualizar dando click en el año deseado."

about = 'Majority Report es una iniciativa académica que surge con el'\
        ' proposito de crear un portal donde los usuarios puedan'\
        ' visualizar de manera interactiva los índices de criminalidad'\
        ' en la ciudad de Medellín. Los datos utilizados para generar las'\
        ' gráficas desplegadas fueron tomados del portal de datos abiertos'\
        ' del Ministerio de Tecnologías de la Información y las'\
        ' Comunicaciones y fueron suministrados'\
        ' por la Secretaría de Seguridad y Convivencia de'\
        ' la Alcaldía de Medellín. Los datos contienen la información de las'\
        ' denuncias efectivamente realizadas por el delito "hurto a personas"'\
        ' desde el año 2003. La última actualización de la base se realizó'\
        ' el 23 de diciembre de 2020.'

contact = 'Mi nombre es Sebastián Valencia Sierra y pueden encontrarme en'\
          ' redes en los siguientes enlaces:'\
          ' Github: https://github.com/sebasvalencia726\n'\
          ' Linledin: https://www.linkedin.com/in/sebastianvalenciasierra/\n'\

def index(request):
    #escribo una cosa aqui
    context = {'title': 'Majority Report Medellín',
               'subtitle': 'Bienvenidos',
               'tab_1_title':"Acerca de",
               'tab_1_text': about,
               'tab_2_title':"Instrucciones",
               'tab_2_text': instructions,
               'tab_3_title':"Contacto",
               'tab_3_text': contact,
               'chart_1_title': "Cantidad de hurtos a personas por sexo de la víctima desde 2003",
               'chart_1':"",
               'chart_2_title':"Cantidad de hurtos a personas mes a mes desde el 2003",
               'chart_2':""}
    context['chart_1'] = bar_chart_animation(data, 'sexo', 'cantidad',
                                             animation_frame='año')
    context['chart_2'] = line_chart(data, 'año', 'mes', 'cantidad')
    context['segment'] = 'index'

    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))


def medellincharts(request):
    #creo key en context que contengan cada una de las fgráficas
    context = {'chart_1_title': "Cantidad de hurtos por año desde el 2003",
               'chart_1':"",
               'chart_2_title':"Cantidad de hurtos por barrio desde el 2003",
               'chart_2':"",
               'chart_3_title': "Cantidad de hurtos por arma utilizada",
               'chart_3':"",
               'chart_4_title': "Cantidad de hurtos por hora durante los días de la semana",
               'chart_4': "",
               'chart_5_title': "Cantidad de hurtos por semana durante el año desde el 2003",
               'chart_5': "",
               'chart_6_title': "Cantidad de hurtos por hora desde el 2003",
               'chart_6': "",
               'chart_7_title': "Cantidad de hurtos por modalidad empleada",
               'chart_7': ""}
    #ex: context['bar_chart_1'] = bar_chart(data, 'seguridad.sexo', 'seguridad.cantidad')
    context['chart_1'] = bar_chart(data, 'año', 'cantidad')
    context['chart_2'] = bar_chart(data, 'nombre_barrio', 'cantidad')
    context['chart_3'] = bar_chart(data, 'arma_medio', 'cantidad')
    context['chart_4'] = line_chart(data, 'dia', 'hora', 'cantidad')
    context['chart_5'] = bar_chart_animation(data, 'semana', 'cantidad',
                                             animation_frame='año')
    context['chart_6'] = bar_chart_animation(data, 'hora', 'cantidad',
                                             animation_frame='año')
    context['chart_7'] = bar_chart(data, 'modalidad', 'cantidad')
    context['segment'] = 'medellincharts.html'

    html_template = loader.get_template( 'medellincharts.html')
    return HttpResponse(html_template.render(context, request))

#@login_required(login_url="/login/")
#def pages(request):
#    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
#    try:

#        load_template      = request.path.split('/')[-1]
#        context['segment'] = load_template

#        html_template = loader.get_template( load_template )
#        return HttpResponse(html_template.render(context, request))

#    except template.TemplateDoesNotExist:

#        html_template = loader.get_template( 'page-404.html' )
#        return HttpResponse(html_template.render(context, request))

#    except:
#
#        html_template = loader.get_template( 'page-500.html' )
#        return HttpResponse(html_template.render(context, request))
