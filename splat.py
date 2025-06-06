''' CREATES THE SPLAT CLASS '''
''' IMPORTS '''
#needed in order to draw the splat
import pygame
#needed in order to calaculate points of the circle
import math
#needed in order to create the noise, creating a unique shape
import random

''' SPLAT CLASS '''
class Splat:
    def __init__(self, color, center):
        ''' Initializes Splat object with a color and center, and determines its points '''
        self._color = color
        self._center = center
        self._splat_points = self.get_splat_points()
        self._enemy = None
    
    def get_splat_points(self):
        ''' Determines points by creating random radii and finding sines and cosines '''
        points = []
        angle = 0
        while angle < math.pi*2:
            radius = 5 + random.random() * 20
            x_pos = radius * math.cos(angle) + self._center[0]
            y_pos = radius * math.sin(angle) + self._center[1]
            points.append((x_pos, y_pos))
            angle+=0.1
        return points

    def draw_splat(self, surface):
        ''' Draws a splat on a given surface '''
        pygame.draw.polygon(surface, self._color, self._splat_points)