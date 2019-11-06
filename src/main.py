import pygame as pg
from src.screen import Screen
from src.player import Player
from src.game_manager import GameManager

class Main:
    FPS = 30

    def __init__(self):
        self.running = True
        self.is_game_over = False
        pg.init()
        print('Starting...')

    def initialize(self):
        self._screen = Screen()
        self._player = Player()
        self._game_manager = GameManager(self._screen, self._player)
        self._screen.add_surface('Player', self._player)

    def on_loop(self):
        self.is_game_over = self._game_manager.run_background()

    def on_render(self):
        self._screen.render()

    def on_event(self, event):
        if (event.type == pg.QUIT):
            self.running = False
        elif (event.type == pg.KEYDOWN):
            if (event.key == pg.K_SPACE and self.is_game_over == False):
                self._player.on_jump()
            elif (event.key == pg.K_r and self.is_game_over == True):
                self.start()
            elif (event.key == pg.K_ESCAPE and self.is_game_over == True):
                self.running = False

    def on_quit(self):
        print('Quitting')
        pg.quit()

    def start(self):
        self.initialize()
        while (self.running):
            for event in pg.event.get():
                self.on_event(event)

            self.on_loop()
            self.on_render()
            
            pg.time.delay(self.FPS)
        self.on_quit()