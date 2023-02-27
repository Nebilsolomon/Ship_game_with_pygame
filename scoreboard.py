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
        self.prep_score(score= 0)
        self.prep_high_score(high_score= 0)
    





    def prep_high_score(self, high_score):
        self.high_score_image = self.font.render("High Score: " + str(high_score), True, (255, 255, 255))
        self.high_score_rect = self.score_text.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_text_rect.top
        self.screen.blit(self.high_score_image, self.high_score_rect)


    def prep_score(self, score):
        
       
        
        self.score_text = self.font.render("Score: " + str(score), True, (255, 255, 255))
        self.score_text_rect = self.score_text.get_rect()
        self.score_text_rect.right = self.screen_rect.right - 50
        self.score_text_rect.top = 10

        # Draw the score text onto the screen
        self.screen.blit(self.score_text, self.score_text_rect)
    



    
    def num_ships(self, num_ship):
        
       
        
        self.ship_text = self.font.render("Ship: " + str(num_ship), True, (255, 255, 255))
        self.ship_text_rect = self.ship_text.get_rect()
        self.ship_text_rect.left = self.screen_rect.left + 50
        self.ship_text_rect.top = 10

        # Draw the score text onto the screen
        self.screen.blit(self.ship_text, self.ship_text_rect)



    def show_num_ship(self, num_ship):
        self.num_ships(num_ship)
        self.screen.blit(self.ship_text, self.ship_text_rect)
        pg.display.update()


    def show_high_score(self,high_score):
       # self.show_num_ship(3)
        self.prep_high_score( high_score)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        pg.display.update()





    def show_score(self, score):
        self.prep_score(score)
        self.screen.blit(self.score_text, self.score_text_rect)
        pg.display.update()

       


       # self.screen.blit(self.score_image, self.score_rect)
