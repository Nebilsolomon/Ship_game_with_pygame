import pygame as pg
from pygame.sprite import Sprite, Group
from util import Util


class Lasers:
    def __init__(self, game): 
        self.game = game 
        self.lasers = Group() 
        
    def add(self):
        self.lasers.add(Laser(game=self.game))
        
        
    def update(self): 
        for laser in self.lasers:
            laser.update()
            
        for laser in self.lasers.copy():
            if laser.rect.bottom <= 0:
                self.lasers.remove(laser)
        self.draw()
             
    def draw(self): 
        for laser in self.lasers:
            laser.draw()


class Laser(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.ship = game.ship
        self.settings = game.settings
        self.rect = pg.Rect(0, 0, self.settings.laser_width,
            self.settings.laser_height)
        self.rect.centerx = self.ship.rect.centerx
        self.rect.top = self.ship.rect.top

        self.y = float(self.rect.y)
        # self.color = self.settings.laser_color
        self.color = Util.random_color(min_rgb=20, max_rgb=255)
        self.speed_factor = self.settings.laser_speed_factor
        
    def update(self): 
        self.y -= self.speed_factor
        self.rect.y = self.y
    
    def draw(self): pg.draw.rect(self.screen, self.color, self.rect) 
