# @author Denis Chuprynin <denischuprynin@gmail.com>


import numpy as np
from app.lib.chart.Chart import Chart
import matplotlib.pyplot as plt
from app.lib.chart.ChartServiceException import ChartServiceException
from py_expression_eval import Parser


class ChartService:
    # 2D charts.
    DOT_CHART_TYPE = 'D'
    LINE_CHART_TYPE = 'L'
    PIE_CHART_TYPE = 'P'
    BAR_CHART_TYPE = 'B'

    # 3D charts.
    DOT_CHART_3D_TYPE = 'D3'
    LINE_CHART_3D_TYPE = 'L3'
    WIREFRAME_CHART_TYPE = 'W'
    SURFACE_CHART_3D_TYPE = 'S'

    @staticmethod
    def visualize_chart(chart: Chart) -> None:
        try:
            # 2D charts.
            if chart.chart_type == ChartService.DOT_CHART_TYPE:
                ChartService._visualize_dot_chart(chart)
                return
            if chart.chart_type == ChartService.PIE_CHART_TYPE:
                ChartService._visualize_pie_chart(chart)
                return
            if chart.chart_type == ChartService.BAR_CHART_TYPE:
                ChartService._visualize_bar_chart(chart)
                return
            if chart.chart_type == ChartService.LINE_CHART_TYPE:
                ChartService._visualize_line_chart(chart)
                return

            # 3D charts.
            if chart.chart_type == ChartService.DOT_CHART_3D_TYPE:
                ChartService._visualize_dot_3d_chart(chart)
                return
            if chart.chart_type == ChartService.LINE_CHART_3D_TYPE:
                ChartService._visualize_line_3d_chart(chart)
                return
            if chart.chart_type == ChartService.WIREFRAME_CHART_TYPE:
                ChartService._visualize_wireframe_chart(chart)
                return
            if chart.chart_type == ChartService.SURFACE_CHART_3D_TYPE:
                ChartService._visualize_surface_chart(chart)
                return
        except Exception:
            raise ChartServiceException('Не удалось визуализировать данные')

    @staticmethod
    def _visualize_dot_chart(chart: Chart) -> None:
        x_label = chart.data[0][0].strip(' "\'\t\r\n')
        y_label = chart.data[0][1].strip(' "\'\t\r\n')
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
        ax.scatter(x_values, y_values)
        plt.show(block=False)

    @staticmethod
    def func(pct, allvalues):
        absolute = int(pct / 100. * np.sum(allvalues))
        return "{:.1f}%\n({:d})".format(pct, absolute)

    @staticmethod
    def _visualize_pie_chart(chart: Chart) -> None:
        labels = list()
        sizes = list()
        for item in chart.data:
            labels.append(item[0].strip(' "\'\t\r\n'))
            sizes.append(float(item[1]))

        fig, ax = plt.subplots(figsize=(chart.window_size[0], chart.window_size[1]))
        fig.canvas.set_window_title(chart.window_title)
        fig.suptitle(chart.window_title)
        ax.pie(sizes, labels=labels, autopct=lambda pct: ChartService.func(pct, sizes), startangle=90)
        ax.axis('equal')
        plt.show(block=False)

    @staticmethod
    def _visualize_bar_chart(chart: Chart) -> None:
        field_names_label = chart.data[0][0]
        field_values_label = chart.data[0][1]
        field_names = list()
        field_values = list()
        for item in chart.data[1:]:
            field_names.append(item[0].strip(' "\'\t\r\n'))
            field_values.append(float(item[1]))

        fig, ax = plt.subplots(figsize=(chart.window_size[0], chart.window_size[1]))
        fig.canvas.set_window_title(chart.window_title)
        fig.suptitle(chart.window_title)
        ax.set_title(field_names_label.strip(' "\'\t\r\n'))
        ax.set_ylabel(field_values_label.strip(' "\'\t\r\n'))
        colors = []
        for i in range(0, len(field_names) + 1):
            colors.append(tuple(np.random.choice(range(0, 2), size=3)))
        ax.bar(field_names, field_values, color=colors)
        plt.show(block=False)

    @staticmethod
    def _visualize_line_chart(chart: Chart) -> None:
        x_label = chart.data[0][0].strip(' "\'\t\r\n')
        y_label = chart.data[0][1].strip(' "\'\t\r\n')
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

    @staticmethod
    def _visualize_dot_3d_chart(chart: Chart) -> None:
        x_label = chart.data[0][0].strip(' "\'\t\r\n')
        y_label = chart.data[0][1].strip(' "\'\t\r\n')
        z_label = chart.data[0][2].strip(' "\'\t\r\n')
        x_values = list()
        y_values = list()
        z_values = list()
        for item in chart.data[1:]:
            x_values.append(float(item[0]))
            y_values.append(float(item[1]))
            z_values.append(float(item[2]))

        fig = plt.figure(figsize=(chart.window_size[0], chart.window_size[1]))
        ax = fig.add_subplot(projection='3d')
        fig.canvas.set_window_title(chart.window_title)
        fig.suptitle(chart.window_title)
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        ax.set_zlabel(z_label)
        size = [50] * (len(x_values))

        ax.scatter(x_values, y_values, z_values, s=size)
        plt.show(block=False)

    @staticmethod
    def _visualize_line_3d_chart(chart: Chart) -> None:
        x_label = chart.data[0][0].strip(' "\'\t\r\n')
        y_label = chart.data[0][1].strip(' "\'\t\r\n')
        z_label = chart.data[0][2].strip(' "\'\t\r\n')
        x_values = list()
        y_values = list()
        z_values = list()
        for item in chart.data[1:]:
            x_values.append(float(item[0]))
            y_values.append(float(item[1]))
            z_values.append(float(item[2]))

        fig = plt.figure(figsize=(chart.window_size[0], chart.window_size[1]))
        ax = fig.add_subplot(projection='3d')
        fig.canvas.set_window_title(chart.window_title)
        fig.suptitle(chart.window_title)
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        ax.set_zlabel(z_label)

        ax.plot(x_values, y_values, z_values)
        plt.show(block=False)

    @staticmethod
    def _visualize_wireframe_chart(chart: Chart) -> None:
        if not chart.z_function:
            raise ChartServiceException('Не удалось визуализировать данные')

        x_label = chart.data[0][0].strip(' "\'\t\r\n')
        y_label = chart.data[0][1].strip(' "\'\t\r\n')
        x_values = list()
        y_values = list()
        for item in chart.data[1:]:
            x_values.append(float(item[0]))
            y_values.append(float(item[1]))

        fig = plt.figure(figsize=(chart.window_size[0], chart.window_size[1]))
        ax = fig.add_subplot(projection='3d')
        fig.canvas.set_window_title(chart.window_title)
        fig.suptitle(chart.window_title)
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)

        x_values = np.array(x_values)
        y_values = np.array(y_values)
        x_grid, y_grid = np.meshgrid(x_values, y_values)

        parser = Parser()
        for method in dir(np):
            parser.ops1[method] = getattr(np, method)

        try:
            z_values = parser.parse(chart.z_function).evaluate({'x': x_grid, 'y': y_grid})
            ax.plot_wireframe(x_grid, y_grid, z_values)
        except Exception:
            plt.close(fig)
            raise ChartServiceException('Не удалось визуализировать данные')
        plt.show(block=False)

    @staticmethod
    def _visualize_surface_chart(chart: Chart) -> None:
        if not chart.z_function:
            raise ChartServiceException('Не удалось визуализировать данные')

        x_label = chart.data[0][0].strip(' "\'\t\r\n')
        y_label = chart.data[0][1].strip(' "\'\t\r\n')
        x_values = list()
        y_values = list()
        for item in chart.data[1:]:
            x_values.append(float(item[0]))
            y_values.append(float(item[1]))

        fig = plt.figure(figsize=(chart.window_size[0], chart.window_size[1]))
        ax = fig.add_subplot(projection='3d')
        fig.canvas.set_window_title(chart.window_title)
        fig.suptitle(chart.window_title)
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)

        x_values = np.array(x_values)
        y_values = np.array(y_values)
        x_grid, y_grid = np.meshgrid(x_values, y_values)

        parser = Parser()
        for method in dir(np):
            parser.ops1[method] = getattr(np, method)

        try:
            z_values = parser.parse(chart.z_function).evaluate({'x': x_grid, 'y': y_grid})
            ax.plot_surface(x_grid, y_grid, z_values)
        except Exception:
            plt.close(fig)
            raise ChartServiceException('Не удалось визуализировать данные')
        plt.show(block=False)
