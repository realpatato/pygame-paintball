''' CREATES THE ENEMY CLASS '''
''' IMPORTS '''
#needed for sprite handling
import pygame

class Enemy:
    def __init__(self, color, rand_scale_mult, x, y):
        ''' Initializes enemy with a sprite, plus an x and y position '''
        self._sprite = self.gen_sprite(color, (rand_scale_mult * 410, rand_scale_mult * 540))
        #rect is needed for getting a collide point
        self._rect = self._sprite.get_rect(topleft = (x, y))
        #need in order to find active pixels on the sprite
        self._mask = pygame.mask.from_surface(self._sprite)
        self._scale_mult = rand_scale_mult
        self._connected_splats = []
        self._spawning = True
    
    def gen_sprite(self, color, size):
        ''' Replaces the default color of the sprite with the enemy's color '''
        #loads the default sprite
        sprite = pygame.image.load("sprites/paintballer.png")
        #gets the pixel array of the sprite
        sprite_pixels = pygame.PixelArray(sprite)
        #replaces default color with enemy's color
        sprite_pixels.replace((77, 109, 243), color)
        #deletes the pixel array to unlock the surface
        del sprite_pixels
        #scales the sprite
        sprite = pygame.transform.scale(sprite, size)
        #returns the sprite
        return sprite
    
    def get_max_height(self):
        ''' Gets the max height that the sprite can go to '''
        return self._scale_mult * 300
    
    def mod_y(self, num):
        ''' Adds a given value to the x position '''
        self._rect.y += num
    
    def draw_self(self, surface):
        ''' Draws the enemy to the screen '''
        surface.blit(self._sprite, self._rect)