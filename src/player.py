import pygame as pg

class Player:

    def __init__(self):
        self._size = self._width, self._height = 40, 30
        self._location = self._left, self._top = 10,10
        self._color = (0,0,0)
        self._player = pg.image.load('assets/flappy-bird.png')
        self._player = pg.transform.scale(self._player, self._size)
        self._rect = pg.Rect(self._location, self._size)
        self._hasRotate = False
        self._speed = 3
        
    def get_surf(self):
        return self._player

    def get_location(self):
        return self._location

    def get_rect(self):
        return self._rect

    def get_right(self):
        return self._left + self._width

    def set_location(self, left=0, top=0):
        self._location = self._left, self._top = left, top

    def set_rect(self, left=0, top=0, width=0, height=0):
        self._rect = pg.Rect(left, top, width, height)

    def on_fall(self):
        self._top += self._speed

        self.set_location(self._left, self._top)
        self.set_rect(self._left, self._top, self._width, self._height)

    def on_jump(self):
        self._top -= 30

        self.set_location(self._left, self._top)
        self.set_rect(self._left, self._top, self._width, self._height)
