import pygame as pg
from src.shape import Rect

class Screen:
    def __init__(self):
        pg.display.set_caption('Flappy Bird')

        self._size = self._width, self._height = 300, 400
        self._screen = pg.display.set_mode(self._size)
        self._surface_list = {}

        self._background = Rect(width=self._width, height=self._height, color=(21,169,237))
        self._floor = Rect(top=self._height-40,width=self._width, height=40, color=(21,209,4))
        self.add_surface(name='background', surface=self._background)
        self.add_surface(name='floor', surface=self._floor)

    def get_surf(self):
        return self._screen

    def get_height(self):
        return self._height

    def get_width(self):
        return self._width

    def get_background(self):
        return self._background

    def get_floor(self):
        return self._floor
        
    def add_surface(self, name, surface):
        self._surface_list.update({name: surface})

    def remove_surface(self, key):
        del self._surface_list[key]

    def render(self):
        for surface in list(self._surface_list.values()):
            self._screen.blit(surface.get_surf(), surface.get_location())

        pg.display.flip()
