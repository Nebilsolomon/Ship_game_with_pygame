import pygame as pg 
import time


class Sound:
    def __init__(self): 
    
        
        
        
        self.collision = pg.mixer.Sound('sounds/collision.wav')
        self.shoot = pg.mixer.Sound('sounds/shoot.wav')
        self.pickup = pg.mixer.Sound('sounds/pickup.wav')
        self.gameover = pg.mixer.Sound('sounds/gameover.wav')
        pg.mixer.music.load('sounds/ride_of_the_valkyries.mp3')
                                             
    def play_background(self): 
        pg.mixer.music.play(-1, 0.0)
        self.music_playing = True
        
    def play_pickup(self): 
        if self.music_playing: self.pickup.play()
    




    def play_shoot(self):
        pg.mixer.init()
        self.shoot.play()
       # pg.mixer.music.stop()
    
    def play_collision(self):
        pg.mixer.init()
        self.collision.play()
    
   


    def play_gameover(self):
        if self.music_playing: 
            self.stop_background()
            self.gameover.play()
            time.sleep(3.0)       # sleep until game over sound has finished
        
    def toggle_background(self):
        if self.music_playing: 
            self.stop_background()
        else:
            self.play_background()
        self.music_playing = not self.music_playing
        
    def stop_background(self): 
        pg.mixer.music.stop()
        self.music_playing = False 
    
        
    
    
