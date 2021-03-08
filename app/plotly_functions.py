#!/usr/bin/python3
"""function to generate plot div objects"""
from re import X
import pandas as pd
import plotly.express as px
from plotly.offline import plot

def bar_chart_animation(df, x_data, y_data, color=None, animation_frame=None):
    """Funtion to return plotly object and displays a bar chart

    Args:
        df (data frame): dataframe to be used
        x_data (str): column to display as x axis
        y_data (str): column to display as y axis
        color (str, optional): Bar colors, defaults to None.
        animation_frame (str): Data to be display as animation.

    Returns:
        Object: plot_div  object
    """
    if color is not None:
        index_list = list(set([animation_frame, x_data, color]))
        pivot_data = df.pivot_table(index=index_list,
                                    values=y_data,
                                    aggfunc='sum').reset_index()
    else:
        index_list = list(set([animation_frame, x_data]))
        pivot_data = df.pivot_table(index=index_list,
                                    values=y_data,
                                    aggfunc='sum').reset_index()

    fig = px.bar(pivot_data,
                x=x_data,
                y=y_data,
                color=color,
                template="plotly_white",
                color_discrete_sequence=px.colors.qualitative.Pastel,
                category_orders={"dia": ["lunes",
                                         "martes",
                                         "miércoles",
                                         "jueves",
                                         "viernes",
                                         "sábado",
                                         "domingo"]},
                animation_frame=animation_frame)
    fig["layout"].pop("updatemenus")
    plot_div = plot(fig, output_type='div')
    return plot_div

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
                color_discrete_sequence=px.colors.qualitative.Pastel,
                category_orders={"dia": ["lunes",
                                         "martes",
                                         "miércoles",
                                         "jueves",
                                         "viernes",
                                         "sábado",
                                         "domingo"]})
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
                color_discrete_sequence=px.colors.qualitative.Pastel,
                category_orders={"dia": ["lunes",
                                         "martes",
                                         "miércoles",
                                         "jueves",
                                         "viernes",
                                         "sábado",
                                         "domingo"]})

    plot_div = plot(fig, output_type='div')
    return plot_div
