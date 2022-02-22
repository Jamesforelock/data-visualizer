# @author Denis Chuprynin <denischuprynin@gmail.com>


class Chart:
    def __init__(self, chart_type: str, data: list, window_size: list, window_title: str, z_function=''):
        self.chart_type = chart_type
        self.data = data
        self.window_size = [hundred_pixels / 100 for hundred_pixels in window_size]
        self.window_title = window_title
        self.z_function = z_function
