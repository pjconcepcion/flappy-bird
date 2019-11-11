import pygame as pg, time, random
from src.canvas import Text
from src.shape import Rect, Circle

class GameManager:

    def __init__(self, screen, player):
        self._screen = screen
        self._player = player
        self._spawn_rate = 1.5
        self._spawn_time = time.time()
        self._pipe_ctr = 0
        self._pipe_list = {}
        self._is_game_over = False
        self._score = 0
        self._score_multiplier = 1
        self._score_multiply = False
        self._scoreText = Text('Score',':',self._score,size=20,left=10,top=self._screen.get_height() - 30)
        self._screen.add_surface('score_text',self._scoreText)
        self._player.set_location(left=10,top=self._screen.get_height() // 2)
        self._player.set_rect(left=10,top=self._screen.get_height() // 2,width=40,height=30)

    def spawn_pipe(self):
        game_area_height = self._screen.get_height() - self._screen.get_floor().get_height()
        width = 70

        pass_left = width + self._screen.get_width() - 10
        pass_top = game_area_height / random.uniform(2.0,4.0)
        pass_height = 100
        pass_area = Rect(left=pass_left,top=pass_top,width=10,height=pass_height,alpha=0)

        top_pipe_left = self._screen.get_width()
        top_pipe_top = 0
        height = pass_top
        top_pipe = Rect(left=top_pipe_left,top=top_pipe_top,width=width,height=height,color=(0,0,0))
        top_inner_pipe = Rect(left=top_pipe_left+5,top=top_pipe_top,width=width-10,height=height-5,color=(24,112,16))

        bottom_pipe_left = self._screen.get_width()
        bottom_pipe_top = pass_top + pass_height
        height = game_area_height - bottom_pipe_top
        bottom_pipe = Rect(left=bottom_pipe_left,top=bottom_pipe_top,width=width,height=height,color=(0,0,0))
        bottom_inner_pipe = Rect(left=bottom_pipe_left+5,top=bottom_pipe_top+5,width=width-10,height=height-5,color=(24,112,16))

        self._screen.add_surface(f'pass_area-{self._pipe_ctr}', pass_area)
        self._screen.add_surface(f'top_pipe-{self._pipe_ctr}', top_pipe)
        self._screen.add_surface(f'bottom_pipe-{self._pipe_ctr}', bottom_pipe)
        self._screen.add_surface(f'top_inner_pipe-{self._pipe_ctr}', top_inner_pipe)
        self._screen.add_surface(f'bottom_inner_pipe-{self._pipe_ctr}', bottom_inner_pipe)

        pass_area = Pipe(pass_area)
        top_pipe = Pipe(top_pipe)
        top_inner_pipe = Pipe(top_inner_pipe)
        bottom_pipe = Pipe(bottom_pipe)
        bottom_inner_pipe = Pipe(bottom_inner_pipe)

        pipe = {
            self._pipe_ctr: {
                f'pass_area-{self._pipe_ctr}': pass_area,
                f'top_pipe-{self._pipe_ctr}': top_pipe,
                f'bottom_pipe-{self._pipe_ctr}': bottom_pipe,
                f'top_inner_pipe-{self._pipe_ctr}': top_inner_pipe,
                f'bottom_inner_pipe-{self._pipe_ctr}': bottom_inner_pipe
            }
        }

        self._pipe_list.update(pipe)
        self._pipe_ctr += 1

    def move_pipe(self):
        for key in list(self._pipe_list):
            is_destroy = False
            for name in list(self._pipe_list[key]):
                is_destroy = self._pipe_list[key][name].move()

            if (is_destroy):
                self._screen.remove_surface(f'top_pipe-{key}')
                self._screen.remove_surface(f'bottom_pipe-{key}')
                self._screen.remove_surface(f'top_inner_pipe-{key}')
                self._screen.remove_surface(f'bottom_inner_pipe-{key}')
                del self._pipe_list[key]

    def check_collision(self):
        for key in list(self._pipe_list):
            for name in list(self._pipe_list[key]):
                pipe = self._pipe_list[key][name]

                if (pipe.get_rect().colliderect(self._player.get_rect())):
                    if (name == f'pass_area-{key}'):
                        self._score += (1 * self._score_multiplier)
                        self._scoreText.set_text(score=self._score)
                        self._screen.remove_surface(name)
                        del self._pipe_list[key][name]                        
                    else:
                        self._is_game_over = True

        if (self._player.get_rect().colliderect(self._screen.get_floor().get_rect())):
            self._is_game_over = True

    def run_background(self):
        if (self._is_game_over == False):
            self._player.on_fall()
            self.check_collision()

            if (time.time() > self._spawn_time):
                self.spawn_pipe()
                self._spawn_rate = random.uniform(1,2.75)
                self._spawn_time = time.time() + self._spawn_rate

            if ((self._score == 30) and self._score_multiply == False):
                self._score_multiplier += 1
                self._score_multiply = True

            self.move_pipe()

            return False
        return True

class Pipe:

    def __init__(self, rect):
        self._pipe = rect
        self._left = self._pipe.get_left_top()['left']

    def move(self):
        self._left -= 5

        if (self._left + self._pipe.get_width() < 0):
            return True

        self._pipe.set_location(left=self._left, top=self._pipe.get_left_top()['top'])
        self._pipe.set_rect(left=self._left, top=self._pipe.get_left_top()['top'], width=self._pipe.get_width(), height=self._pipe.get_height())
        return False

    def get_rect(self):
        return self._pipe.get_rect()

    def get_right(self):
        return self._pipe.get_left_top()['left'] + self._pipe.get_width()


        