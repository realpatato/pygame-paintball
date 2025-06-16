''' CREATES THE BACKGROUND CLASS '''
''' IMPORTS '''
#needed for draw functions
import pygame

''' BACKGROUND CLASS '''
class Background:
    def __init__(self, color):
        self._color = color
        self._line_points = self.get_line_points()
        self._line_color = self.get_line_color()

    def get_line_points(self):
        ''' Gets the points of the lines that are drawn on the background '''
        #list of the points of the background lines
        line_coords = [
            [(0, 0), (300, 150), (700, 150), (1000, 0)], #top three lines
            [(0, 750), (300, 600), (700, 600), (1000, 750)], #bottom three lines
            [(300, 150), (300, 600)], #in-betweener one
            [(700, 150), (700, 600)]  #in-betweener two
        ]
        return line_coords
    
    def get_line_color(self):
        ''' Gets the color of the lines based on the background color '''
        #empty list, since colors can be a list or a tuple (work the same way)
        line_color = []
        #iterates over each value in the color tuple
        for val in self._color:
            #check if its at lest twenty (prevents negatives since 20 is subtracted)
            if val > 20:
                line_color.append(val-20)
            else:
                line_color.append(0)
        #returns the color back
        return line_color
    
    def draw_background(self, surface):
        ''' Draws the background '''
        #fills the screen
        surface.fill(self._color)
        #draws all of the lines
        pygame.draw.lines(surface, self._line_color, False, self._line_points[0], 5)
        pygame.draw.lines(surface, self._line_color, False, self._line_points[1], 5)
        pygame.draw.line(surface, self._line_color, self._line_points[2][0], self._line_points[2][1], 5)
        pygame.draw.line(surface, self._line_color, self._line_points[3][0], self._line_points[3][1], 5)