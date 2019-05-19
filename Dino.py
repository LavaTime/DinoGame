import pygame
import time
import random
from pygame.locals import *

pygame.init()
pygame.display.init()
width, height = 1280, 720
icon_surf = pygame.image.load("GameData/Sprites/dino0000.png")
pygame.display.set_icon(icon_surf)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Dinosaur Game')
screen.fill((255, 255, 255))
dinopos = [100, 500]
keys = [False, False, False]

# Loading sprites

dino1 = pygame.image.load("GameData/Sprites/dinorun0000.png")
dino2 = pygame.image.load("GameData/Sprites/dinorun0001.png")
dinoduck0 = pygame.image.load("GameData/Sprites/dinoduck0000.png")
dinoduck1 = pygame.image.load("GameData/Sprites/dinoduck0001.png")
dinojump = pygame.image.load("GameData/Sprites/dinoJump0000.png")
berd0 = pygame.image.load("GameData/Sprites/berd.png")
berd1 = pygame.image.load("GameData/Sprites/berd2.png")
cactussmall = pygame.image.load("GameData/Sprites/cactusSmall0000.png")
cactusbig = pygame.image.load("GameData/Sprites/cactusBig0000.png")
cactushord = pygame.image.load("GameData/Sprites/cactusSmallMany0000.png")
dinoicon = pygame.image.load("GameData/Sprites/dino0000.png")
dinodead = pygame.image.load("GameData/Sprites/dinoDead0000.png")
cloud = pygame.image.load("GameData/Sprites/cloud0000.png")

#Values

dinotexture = dino1
running = True
jumping = False
duck = False
groundStart = (0, 588)
groundStop = (1280, 588)
mincloud = 300
maxcloud = 20
cloudx = 300
mintimeclouds = 60
lastcloud = 0
countcloud = True

#colors
black = (0, 0, 0)
white = (255, 255, 255)
grey = (83, 83, 83)

def updatescreen():
    """
Used to refresh the screen after some changes, Fills the screen with the color, draws the line, blits the entities, and
then flips (updates) the screen
    :rtype: None
    """
    screen.fill((255, 255, 255))
    pygame.draw.line(screen, grey, groundStart, groundStop)
    screen.blit(dinotexture, dinopos)
    pygame.display.flip()

'''def cloudspawn():
    global lastcloud
    if lastcloud >= mintimeclouds:
        lastcloud = 0
        ranspawn = random.randint(0, 2)
        if ranspawn <= 1:
            cloudheight = random.randint(mincloud, maxcloud)
            screen.blit(cloud, (cloudx, cloudheight))
            updatescreen()
            countcloud = True
'''

while running:
    #cloudspawn()
    #if cloudx <= 0:
    #    cloudx -= 1
    #if countcloud:
    #    lastcloud += 1

    if not jumping and not duck:
        dinotexture = dino1
        updatescreen()
        dinotexture = dino2
        updatescreen()
    if duck:
        dinotexture = dinoduck0
        updatescreen()
        dinotexture = dinoduck1
        updatescreen()
    updatescreen()
    for event in pygame.event.get():
        # Check if X is pressed
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        # Check for event KEYDOWN

        if event.type == pygame.KEYDOWN:
            # Full screen key - F11
            if event.key == K_F11:
                keys[0] = True
            # Jump key(s) - Space and K_up
            if event.key == K_UP or event.key == K_SPACE:
                keys[1] = True
            # Duck key - K_DOWN
            if event.key == K_DOWN:
                keys[2] = True

        # Check for EVENT KEYUP
        if event.type == pygame.KEYUP:
            # Full screen key - F11
            if event.key == K_F11:
                keys[0] = False
            # Jump key(s) - Space and K_up
            if event.key == K_UP or event.key == K_SPACE:
                keys[1] = False
            # Duck key - K_DOWN
            if event.key == K_DOWN:
                keys[2] = False

        if keys[0]:
            # print(pygame.display.get_wm_info())
            # isFull = False
            # if not isFull:
            pygame.display.set_mode((width, height), pygame.FULLSCREEN, pygame.NOFRAME)
            # print(pygame.display.get_wm_info())
                # isFull = True
            # elif isFull:
                # pygame.display.set_mode((width, height))
                # isFull = False
            print('Toggled Full screen')
        if keys[1]:
            jumping = True
            print('Jump')
            dinotexture = dinojump
            for i in range(60):
                dinopos[1] -= 2.5
                # screen.fill(0)
                # screen.blit(dino1, dinopos)
                # pygame.display.flip()
                updatescreen()
            time.sleep(0.1)
            for i in range(60):
                dinopos[1] += 2.5
                # screen.fill(0)     Remove later - used instead of updatescreen()
                # screen.blit(dino1, dinopos)
                # pygame.display.flip()
                updatescreen()
            jumping = False
            # Continue later - Jump animation - 30 FPS (Frames per second)
        if keys[2]:
            print('Duck')
            duck = True
            dinopos[1] = 544
            # updatescreen()
        if not keys[2]:
            duck = False
            dinopos[1] = 500
