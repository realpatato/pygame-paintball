''' IMPORTS '''
#needed for all visual aspects of the program
import pygame
#needed for color selection
import random
#needed for splat creation and drawing
import splat
#needed for background
import background as bg
#needed for enemies
import enemy

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
colors = [BLACK, RED, GREEN, BLUE, YELLOW, CYAN, PINK]

#empty list to store splats
splats = []

#load in the paintball sound effect
gun_sound = pygame.mixer.Sound("audio/paintball_gun.wav")

#create background object
background = bg.Background(WHITE)

#timer variable (starts at 179 so an enemy is instantly created)
timer = 179

''' GAME LOOP SET UP '''
#clock to manage the frame rate
clock = pygame.time.Clock()

#variable to control if the game loop is running or not
keep_playing = True

''' GAME LOOP '''
#the loop itself, checks if the loop is supposed to be going
while keep_playing:
    #advance the timer
    timer += 1
    #checks if its been ~3 seconds
    if timer == 180:
        #gets a random scale multiplier
        rand_scale_mult = random.random() + 0.25
        #basically changes the color and scale of the enemy
        enemy1 = enemy.Enemy(colors[random.randint(1, len(colors) - 1)], (rand_scale_mult * 410, rand_scale_mult * 540), 0, 0)
        #resets timer
        timer = 0

    #checking for any events (quitting, clicking, key press)
    for event in pygame.event.get():
        #check for mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            #get the mouse position
            mouse_pos = pygame.mouse.get_pos()
            #prevents clicking on scoreboard area
            if mouse_pos[1] < 650:
                #play sound effect
                pygame.mixer.Sound.play(gun_sound)
                #create and add a Splat object to the splat list
                splats.append(splat.Splat(colors[random.randint(0, len(colors) - 1)], mouse_pos))

        #check if the player has quit
        if event.type == pygame.QUIT:
            #set control variable to false
            keep_playing = False
    
    #draw background before anything else
    background.draw_background(screen)
    
    #draws the enemy
    enemy1.draw_enemy(screen)

    ''' DRAW ALL ITEMS HERE '''
    #iterates over all the splats
    for splat_object in splats:
        #draws each one to the screen
        splat_object.draw_splat(screen)

    #draws box for where the score goes
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