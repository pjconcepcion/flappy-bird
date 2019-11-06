import pygame as pg

class Text:

    def __init__(self, title='', separator='', score='',size=15, color=(255,255,255), left=0, top=0):
        self._title = title
        self._separator = separator
        self._score = score
        self._size = size
        self._color = color
        self._text = f'{self._title}{self._separator} {self._score}'
        self._font = pg.font.Font('assets/arial.ttf', size)
        self._text_surf = self._font.render(self._text, True, self._color)
        self._rect = self._text_surf.get_rect()
        self._location = self._left, self._top = left, top

    def get_location(self):
        return self._location

    def get_surf(self):
        return self._text_surf

    def set_text(self, title = '', separator = '', score = ''):
        self._title = title if title != '' else self._title
        self._separator = separator if separator != '' else self._separator
        self._score = score if score != '' else self._score

        self._text = f'{self._title}{self._separator} {self._score}'
        self._text_surf = self._font.render(self._text, True, self._color)

    def set_color(self, color):
        self._color = color

    def set_size(self, size):
        self._font = pg.font.Font('assets/arial.ttf', size)