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
#needed for scoreboard
import scoreboard as sb

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
#empty list to store enemies
enemies = []
#empty list to store all drawn objects
draw_objects = []

#load in the paintball sound effect
gun_sound = pygame.mixer.Sound("audio/paintball_gun.wav")

#create background object
background = bg.Background(WHITE)

#timer variable (starts at 179 so an enemy is instantly created)
timer = 0
#timer variable to control if timer should count down
do_timer = True

#variable to hold score
score = 0
#variable to hold the score board
scoreboard = sb.Scoreboard(score)

''' FUNCTIONS '''
def spawn_enemy():
    #gets a random scale multiplier
    rand_scale_mult = random.random() + 0.25
    #basically changes the color and scale of the enemy
    enemies.append(enemy.Enemy(colors[random.randint(1, len(colors) - 1)], rand_scale_mult, random.randint(0, 750), 650))
    #adds the enemy to the list to be drawn
    draw_objects.append(enemies[len(enemies) - 1])

''' GAME LOOP SET UP '''
#clock to manage the frame rate
clock = pygame.time.Clock()

#variable to control if the game loop is running or not
keep_playing = True

#spawn an enemy before starting
spawn_enemy()

''' GAME LOOP '''
#the loop itself, checks if the loop is supposed to be going
while keep_playing:
    #checks if it SHOULD advance the timer
    if do_timer:
        #advance the timer
        timer += 1
    
    #checks if its been ~3 seconds
    if timer == 160:
        #makes the enemy despawn
        enemies[0]._spawning = False
        #resets the timer
        timer = 0
        #pauses the timer
        do_timer = False

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
                for i in range(0, len(enemies)):
                    #ensures it starts at the very end, and goes to the front
                    index = 0 - (i + 1)
                    #gets the object from the list with index
                    enemy_object = enemies[index]
                    #checking for where the mouse is in the sprite rect
                    pos_in_enemy_mask = (mouse_pos[0] - enemy_object._rect.x, mouse_pos[1] - enemy_object._rect.y)
                    #checks if the mouse is with the sprite basically
                    if enemy_object._rect.collidepoint(*mouse_pos) and enemy_object._mask.get_at(pos_in_enemy_mask):
                        #create and add a Splat object to the splat list with enemy
                        splats.append(splat.Splat(colors[random.randint(0, len(colors) - 1)], mouse_pos))
                        #adds the object to the enemies list of connected splats
                        enemy_object._connected_splats.append(splats[len(splats) - 1])
                        #makes enemy go away after they get shot
                        enemy_object._spawning = False
                        #adds points to the score based on how long it took for you to click
                        score  += (160 - timer) * 20
                        #updates the scoreboard with the points
                        scoreboard.update_score(score)
                        #sets timer to 0 
                        timer = 0
                        #pauses the timer
                        do_timer = False
                        #breaks out of the loop since an enemy has already been found
                        break
                    else:
                        #create and add a Splat object to the splat list with no enemy
                        splats.append(splat.Splat(colors[random.randint(0, len(colors) - 1)], mouse_pos))
                #adds the splat to the list of draw objects
                draw_objects.append(splats[len(splats) - 1])

        #check if the player has quit
        if event.type == pygame.QUIT:
            #set control variable to false
            keep_playing = False
    
    #moves the enemies before drawing them
    for enemy_object in enemies:
        #checks if the enemy is spawning in and if the y position is high enough
        if enemy_object._spawning == True and enemy_object._rect.y > (650 - enemy_object.get_max_height()):
            #make the position higher up on the screen
            enemy_object.mod_y(-5)
            #iterates over each connected splat
            for splat_object in enemy_object._connected_splats:
                #has any splats move up with the enemy
                splat_object.mod_y(-5)
        #checks if the enemy needs to be going away
        elif enemy_object._spawning == False:
            #makes the enemy go lower down on the screen
            enemy_object.mod_y(5)
            #iterates over each connected splat
            for splat_object in enemy_object._connected_splats:
                #has any splats move down with the enemy
                splat_object.mod_y(5)
            #if the y is low enough on the screen
            if enemy_object._rect.y > 700:
                #remove the enemy from the list
                enemies.remove(enemy_object)
                #remove the enemy from the draw list too
                draw_objects.remove(enemy_object)
                #spawns a new enemy since the old one is gone
                spawn_enemy()
                #unpause the timer once the enemy has been spawned in
                do_timer = True
                #iterates over the splats connected to the enemy
                for splat_object in enemy_object._connected_splats:
                    #removes it from the splats list
                    splats.remove(splat_object)
                    #removes it from the drawn objects
                    draw_objects.remove(splat_object)
    
    #draw background before anything else
    background.draw_background(screen)

    ''' DRAW ALL ITEMS HERE '''
    #draws the game objects
    for object in draw_objects:
        object.draw_self(screen)

    #draws box for where the score goes
    pygame.draw.rect(screen, BLACK, [0, 654, 1000, 750])
    #draws the scoreboard
    scoreboard.draw_self(screen)
    
    #updates the screen
    pygame.display.update()

    #sets the frame rate
    clock.tick(60)

''' ENDING THE PROGRAM '''
#quits the window
pygame.quit()
#ends the program
quit()