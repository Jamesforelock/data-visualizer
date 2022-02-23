# @author Denis Chuprynin <denischuprynin@gmail.com>


import numpy as np
import matplotlib.pyplot as plt
from py_expression_eval import Parser
from app.lib.chart import Surface
from app.lib.chart.SurfaceServiceException import SurfaceServiceException


class SurfaceService:
    WIREFRAME_TYPE = 'W'
    SURFACE_TYPE = 'S'

    @staticmethod
    def visualize_surface(surface: Surface) -> None:
        fig = plt.figure(figsize=(surface.window_size[0], surface.window_size[1]))
        ax = fig.add_subplot(projection='3d')
        fig.canvas.set_window_title(surface.window_title)
        fig.suptitle(surface.window_title)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')

        x_values = np.linspace(surface.x_section['start'], surface.x_section['end'], surface.points_number)
        y_values = np.linspace(surface.y_section['start'], surface.y_section['end'], surface.points_number)
        x_grid, y_grid = np.meshgrid(x_values, y_values)

        parser = Parser()
        for method in dir(np):
            parser.ops1[method] = getattr(np, method)

        try:
            z_values = parser.parse(surface.z_function).evaluate({'x': x_grid, 'y': y_grid})
            if surface.surface_type == SurfaceService.WIREFRAME_TYPE:
                ax.plot_wireframe(x_grid, y_grid, z_values)
            if surface.surface_type == SurfaceService.SURFACE_TYPE:
                ax.plot_surface(x_grid, y_grid, z_values)
        except Exception:
            plt.close(fig)
            raise SurfaceServiceException('Не удалось визуализировать данные')

        plt.show(block=False)

