import pygame as pg, sys, time
from vector import Vector
from sound import Sound
from colors import DARK_GREY, LIGHT_GREY, LIGHT_RED




class Scoreboard():
    def __init__(self, game):
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = self.screen.get_rect()
      
        self.font = pg.font.Font(None, 36)
        self.prep_score()
        
      
      
      #  self.text_color = (30, 30, 30)
       # self.font = pg.font.Font(None, 36)
       # self.prep_score()
       
    

    def prep_score(self):
        
       
        
        self.score_text = self.font.render("Score: " + str(self.settings.score ), True, (255, 255, 255))
        self.score_text_rect = self.score_text.get_rect()
        self.score_text_rect.right = self.screen_rect.right - 50
        self.score_text_rect.top = 10

        # Draw the score text onto the screen
        self.screen.blit(self.score_text, self.score_text_rect)







     #   score_text = font.render("Score: " + str(score), True, (255, 255, 255))

       # score_str = str(self.settings.score)
        #self.score_image = self.font.render(score_str, True, self.text_color, LIGHT_RED)
        #self.score_rect = self.score_image.get_rect() 
        #self.score_rect.right = self.screen_rect.right - 50 
        #self.score_rect.top = 20

    def show_score(self):
        self.prep_score()
        self.settings.score += 1 
        print(self.settings.score)
        self.screen.blit(self.score_text, self.score_text_rect)
#        pg.display.update()

       


       # self.screen.blit(self.score_image, self.score_rect)
