import pygame as pg

class Shape:
    def __init__(self, left=0, top=0, width=0, height=0, color = (0,0,0),alpha=255):
        self._location = self._left, self._top = left, top
        self._size = self._width, self._height = width, height
        self._color = color
        self._surf = pg.Surface(self._size)
        self._surf.fill(self._color)
        self._surf.set_alpha(alpha)

    def get_surf(self):
        return self._surf

    def get_location(self):
        return self._location

    def get_left_top(self):
        return {'left': self._left, 'top': self._top}

    def get_size(self):
        return self._size

    def get_rect(self):
        return self._rect

    def get_height(self):
        return self._height

    def get_width(self):
        return self._width

    def set_location(self, left = 0, top = 0):
        self._location = self._left, self._top = left, top

    def set_rect(self, left = 0, top = 0, width = 0, height = 0):
        self._rect = pg.Rect(left, top, width, height)

class Rect(Shape):
    def __init__(self, left=0, top=0, width=0, height=0, color=(0,0,0),alpha=255):
        super().__init__(left, top, width, height, color, alpha)
        self._rect = pg.Rect(left,top, width, height)

class Circle(Shape):
    def __init__(self, left=0, top=0, width=0, height=0, color=(0,0,0), radius=10,draw_color=(0,0,0)):
        super().__init__(left, top, width, height, color)
        self._radius = radius
        self._center =  [width//2, height//2]
        self._draw_color = draw_color
        self._rect = pg.draw.circle(self._surf, self._draw_color, self._center, self._radius)