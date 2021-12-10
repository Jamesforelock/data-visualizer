# @author Denis Chuprynin <denischuprynin@gmail.com>


import numpy as np
from app.chart.Chart import Chart
import matplotlib.pyplot as plt


class ChartService:
    PIE_CHART_TYPE = 'P'
    BAR_CHART_TYPE = 'B'
    LINE_CHART_TYPE = 'L'

    @staticmethod
    def visualize_chart(chart: Chart) -> None:
        if chart.chart_type == ChartService.PIE_CHART_TYPE:
            ChartService._visualize_pie_chart(chart)
            return
        if chart.chart_type == ChartService.BAR_CHART_TYPE:
            ChartService._visualize_bar_chart(chart)
            return
        if chart.chart_type == ChartService.LINE_CHART_TYPE:
            ChartService._visualize_line_chart(chart)

    @staticmethod
    def _visualize_pie_chart(chart: Chart) -> None:
        labels = list()
        sizes = list()
        for item in chart.data:
            labels.append(item[0])
            sizes.append(float(item[1]))

        fig, ax = plt.subplots(figsize=(chart.window_size[0], chart.window_size[1]))
        fig.canvas.set_window_title(chart.window_title)
        fig.suptitle(chart.window_title)
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        plt.show(block=False)

    @staticmethod
    def _visualize_bar_chart(chart: Chart) -> None:
        field_names_label = chart.data[0][0]
        field_values_label = chart.data[0][1]
        field_names = list()
        field_values = list()
        for item in chart.data[1:]:
            field_names.append(item[0])
            field_values.append(float(item[1]))

        fig, ax = plt.subplots(figsize=(chart.window_size[0], chart.window_size[1]))
        fig.canvas.set_window_title(chart.window_title)
        fig.suptitle(chart.window_title)
        ax.set_title(field_names_label)
        ax.set_ylabel(field_values_label)
        colors = []
        for i in range(0, len(field_names) + 1):
            colors.append(tuple(np.random.choice(range(0, 2), size=3)))
        ax.bar(field_names, field_values, color=colors)
        plt.show(block=False)

    @staticmethod
    def _visualize_line_chart(chart: Chart) -> None:
        x_label = chart.data[0][0]
        y_label = chart.data[0][1]
        x_values = list()
        y_values = list()
        for item in chart.data[1:]:
            x_values.append(float(item[0]))
            y_values.append(float(item[1]))

        fig, ax = plt.subplots(figsize=(chart.window_size[0], chart.window_size[1]))
        fig.canvas.set_window_title(chart.window_title)
        fig.suptitle(chart.window_title)
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        ax.plot(x_values, y_values)
        plt.show(block=False)
