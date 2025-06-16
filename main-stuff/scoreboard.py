''' CREATES THE SCOREBOARD CLASS '''
''' IMPORTS '''
#need for surface creation
import pygame

''' SCOREBOARD CLASS '''
class Scoreboard:
    def __init__(self, score):
        self._sprites = self.parse_spritesheet()
        self._text = "SCORE:" + str(score)
    
    def get_sprite_names(self):
        ''' Gets the '''
        return ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "S", "C", "O", "R", "E", ":"]

    def parse_spritesheet(self):
        ''' Parses the text spritesheet and stores the sprites'''
        #defines height since the height is the same everytime
        height = 16
        #creates a list of the widths, since they vary
        widths = [
            20, 12, 20, 20, 20, 20, 20, 20, 20, 20, #0-9
            18, 18, 22, 18, 18, 14 #SCORE:
        ]
        sprite_names = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
            "S", "C", "O", "R", "E", ":"
        ]
        #creates an empty dictionary to hold the sprites
        sprites={}
        #load in the spritesheet
        spritesheet = pygame.image.load("sprites/text.png")
        #iterates of each sprite
        for i in range(len(sprite_names)):
            #creates a blank surface for the sprite to be drawn on
            surface = pygame.Surface((widths[i], height), pygame.SRCALPHA)
            #offset starts at zero
            offset = 0
            #loops over the widths of the characters before the new one
            for k in range(0, i):
                #adds those widths to the offset
                offset += widths[k]
            #draws the spritesheet in a spot where only the character is
            surface.blit(spritesheet, (-(offset), 0))
            #gets the size of the character in order to scale
            surface_size = surface.get_size()
            #scales the text since its super small otherwise
            surface = pygame.transform.scale(surface, (3 * surface_size[0], 3 * surface_size[1]))
            #adds sprite to the surface with the correct name
            sprites[sprite_names[i]] = surface
        #returns the sprites
        return sprites

    def update_score(self, score):
        self._text = "SCORE:" + str(score)

    def draw_self(self, surface):
        ''' Draws the scoreboard '''
        #offset for each character
        offset = 0
        #iterates over each character in the text
        for i in range(len(self._text)):
            #gets the final index
            char_index = 0 - (i + 1)
            #gets the character at that index
            char = self._text[char_index]
            #gets its size
            char_size = self._sprites[char].get_size()
            #adds the x size to the offset
            offset += char_size[0]
            #draws the character given the offset
            surface.blit(self._sprites[char], (1000 - offset, 678))