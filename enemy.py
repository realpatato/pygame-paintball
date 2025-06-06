''' CREATES THE ENEMY CLASS '''
''' IMPORTS '''
#needed for sprite handling
import pygame

class Enemy:
    def __init__(self, color, x, y):
        ''' Initializes enemy with a sprite, plus an x and y position '''
        self._sprite = self.gen_sprite(color)
        self._x = x
        self._y = y
    
    def gen_sprite(self, color):
        ''' Replaces the default color of the sprite with the enemy's color '''
        #loads the default sprite
        sprite = pygame.image.load("sprites/paintballer.png")
        #gets the pixel array of the sprite
        sprite_pixels = pygame.PixelArray(sprite)
        #replaces default color with enemy's color
        sprite_pixels.replace((77, 109, 243), color)
        #deletes the pixel array to unlock the surface
        del sprite_pixels
        #returns the sprite
        return sprite
    
    def draw_enemy(self, surface):
        ''' Draws the enemy to the screen '''
        surface.blit(self._sprite, (self._x, self._y))