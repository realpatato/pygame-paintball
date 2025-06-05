''' IMPORTS '''
#needed for all visual aspects of the program
import pygame
#needed for color selection
import random
#needed for splat creation and drawing
import splat
#needed for background
import background as bg

#starts the module
pygame.init()
#starts the audio module
pygame.mixer.init()

''' WINDOW SET UP '''
#variables for screen size for easy changing
screen_width = 1000
screen_height = 750

#creates a screen with given dimensions
screen = pygame.display.set_mode((screen_width, screen_height))

#set a caption for the window
pygame.display.set_caption("Paintball")

''' VARIABLE SET UP'''
#color code constants, for colors that will never change
WHITE = (255, 255, 255)
GRAY = (175, 175, 175)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PINK = (255, 0, 255)

#list to store the colors, for random selection
colors = [WHITE, RED, GREEN, BLUE, YELLOW, CYAN, PINK]

#empty list to store splats
splats = []

#load in the paintball sound effect
gun_sound = pygame.mixer.Sound("audio/paintball_gun.wav")

#create background object
background = bg.Background(GRAY)

''' GAME LOOP SET UP '''
#clock to manage the frame rate
clock = pygame.time.Clock()

#variable to control if the game loop is running or not
keep_playing = True

''' GAME LOOP '''
#the loop itself, checks if the loop is supposed to be going
while keep_playing:
    #checking for any events (quitting, clicking, key press)
    for event in pygame.event.get():
        #check for mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            #get the mouse position
            mouse_pos = pygame.mouse.get_pos()
            #prevents clicking on scoreboard area
            if mouse_pos[1] < 650:
                print("Hello?")
                #play sound effect
                pygame.mixer.Sound.play(gun_sound)
                #create and add a Splat object to the splat list
                splats.append(splat.Splat(colors[random.randint(0, len(colors) - 1)], mouse_pos))

        #check if the player has quit
        if event.type == pygame.QUIT:
            #set control variable to false
            keep_playing = False
    
    #clear screen before anything else
    background.draw_background(screen)

    ''' DRAW ALL ITEMS HERE '''
    for splat_object in splats:
        splat_object.draw_splat(screen)

    pygame.draw.rect(screen, BLACK, [0, 625, 1000, 750])
    
    #updates the screen
    pygame.display.update()

    #sets the frame rate
    clock.tick(60)

''' ENDING THE PROGRAM '''
#quits the window
pygame.quit()
#ends the program
quit()