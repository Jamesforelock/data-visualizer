# @author Denis Chuprynin <denischuprynin@gmail.com>


class Surface:
    def __init__(self, surface_type: str, window_size: list, window_title: str, x_section: list,
                 y_section: list, points_number: int, z_function: str):
        self.surface_type = surface_type
        self.window_size = [hundred_pixels / 100 for hundred_pixels in window_size]
        self.window_title = window_title
        self.x_section = {
            'start': x_section[0],
            'end': x_section[1]
        }
        self.y_section = {
            'start': y_section[0],
            'end': y_section[1]
        }
        self.points_number = points_number
        self.z_function = z_function
