import pygame as pg, sys, time
from vector import Vector
from sound import Sound
from settings import Settings 
from ship import Ship
from laser import Lasers
from alien import Aliens
from scoreboard import Scoreboard


class Game:
    def __init__(self): 
        pg.init()
        self.settings = Settings()
        self.window_height, self.window_width = self.settings.screen_height, self.settings.screen_width
        self.screen = pg.display.set_mode((self.window_width, self.window_height), 0, 32)
        pg.display.set_caption('Alien Invasion')
        self.finished = False
        
        
       
                
        self.sound = Sound()
        self.sound.play_background()
        self.ship = Ship(game=self)
        self.lasers = Lasers(game=self)
        self.ship.set_lasers(lasers=self.lasers)
        self.ship.set_sound(sound= self.sound)
        self.aliens = Aliens(game=self)
        self.aliens.set_sound(sound= self.sound)
        self.sb = Scoreboard(game= self)

    def handle_events(self):
        keys_dir = {pg.K_w: Vector(0, -1), pg.K_UP: Vector(0, -1), 
                    pg.K_s: Vector(0, 1), pg.K_DOWN: Vector(0, 1),
                    pg.K_a: Vector(-1, 0), pg.K_LEFT: Vector(-1, 0),
                    pg.K_d: Vector(1, 0), pg.K_RIGHT: Vector(1, 0)}
        
        for event in pg.event.get():
            if event.type == pg.QUIT: self.game_over()
            elif event.type == pg.KEYDOWN:
                key = event.key
                if key in keys_dir:
                    self.ship.v += self.settings.ship_speed * keys_dir[key]
                elif key == pg.K_SPACE:
                    self.ship.open_fire()
            elif event.type == pg.KEYUP:
                key = event.key
                if key in keys_dir:
                    self.ship.v = Vector()
                elif key == pg.K_SPACE:
                    self.ship.cease_fire()

    def restart(self): pass 


    def game_over(self):
        self.finished = True
        self.sound.play_gameover()
        self.sound.stop_background()
        pg.quit()
        sys.exit()

    def play_again(self): pass
        
    def play(self):
        while not self.finished:
            self.sb.show_score()

            self.handle_events() 
                
            self.screen.fill(self.settings.bg_color)
            self.ship.update()
            self.lasers.update()
            self.aliens.update()
            self.sb.show_score()

            pg.display.update()
            
            time.sleep(0.02)


def main():
    g = Game()
    g.play()
    
    
if __name__ == '__main__':
    main()

 