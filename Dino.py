import pygame
import time
import random
import threading
from pygame.locals import *

pygame.init()
pygame.mixer.init()
pygame.font.init()
pygame.display.init()
WIDTH, HEIGHT = 1280, 720
ICON_SURF = pygame.image.load("GameData/Sprites/dino0000.png")
pygame.display.set_icon(ICON_SURF)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Dinosaur Game')
screen.fill((255, 255, 255))
dinopos = [100, 500]
keys = [False, False, False]

# Loading game files

FONT = pygame.font.SysFont("monospace", 16)
DINO1 = pygame.image.load("GameData/Sprites/dinorun0000.png")
DINO2 = pygame.image.load("GameData/Sprites/dinorun0001.png")
DINODUCK0 = pygame.image.load("GameData/Sprites/dinoduck0000.png")
DINODUCK1 = pygame.image.load("GameData/Sprites/dinoduck0001.png")
DINOJUMP = pygame.image.load("GameData/Sprites/dinoJump0000.png")
BIRD0 = pygame.image.load("GameData/Sprites/berd.png")
BIRD1 = pygame.image.load("GameData/Sprites/berd2.png")
CACTUSSMALL = pygame.image.load("GameData/Sprites/cactusSmall0000.png")
CACTUSBIG = pygame.image.load("GameData/Sprites/cactusBig0000.png")
CACTUSHORD = pygame.image.load("GameData/Sprites/cactusSmallMany0000.png")
DINOICON = pygame.image.load("GameData/Sprites/dino0000.png")
DINODEAD = pygame.image.load("GameData/Sprites/dinoDead0000.png")
CLOUD = pygame.image.load("GameData/Sprites/cloud0000.png")

JUMPSFX = "GameData/Sound effects/jump.ogg"
DEATHSFX = "GameData/Sound effects/death.ogg"

pygame.mixer.music.load(JUMPSFX)


# Values

losetext = FONT.render("You Lose", 1, (100, 100, 100))
cactusbig_y = 508
cactushord_y = 508
cactussmall_y = 508
bird_low_y = 500
bird_mid_y = 422
bird_high_y = 370
obsPos = []
obsList = []
lastObs = 40
speed = 0
score = 76
dinotexture = DINO1
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

# colors
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
    for x in range(len(obsList)):
        screen.blit(obsList[x], obsPos[x])
    screen.blit(dinotexture, dinopos)
    screen.blit(scoretext, (1150, 20))
    pygame.display.flip()

def lose():
    screen.fill((255, 255, 255))
    screen.blit(losetext, (WIDTH/2, HEIGHT/2))
    pygame.time.delay(2000)
    running = False
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


def addscore():
    global score
    threading.Timer(0.5, addscore).start()
    score += 1
    #print(score)


addscore()


def obsSpawn():
    """
    gets random obs than puts it in an obsList and after it puts his [x,y] in obsPos
    :return:
    """
    global score
    global lastObs
    # print(score, lastObs)
    if (score - lastObs) > score/15:
        num = random.randint(0, 100)
        if num <= 25:
            obsList.append(CACTUSSMALL)
            obsPos.append([WIDTH, cactussmall_y])
            lastObs = score
        elif 25 < num <= 45:
            obsList.append(CACTUSBIG)
            obsPos.append([WIDTH, cactusbig_y])
            lastObs = score
        elif 45 < num <= 60:
            obsList.append(CACTUSHORD)
            obsPos.append([WIDTH, cactushord_y])
            lastObs = score
        elif 60 < num <= 75 and score > 250: # high
            obsList.append(BIRD0)
            obsPos.append([WIDTH, bird_high_y])
            lastObs = score
            print(60, 75)
        elif 75 < num <= 88 and score > 250: # low
            obsList.append(BIRD0)
            obsPos.append([WIDTH, bird_low_y])
            lastObs = score
            print(75, 88)
        elif 88 < num <= 100 and score > 250:
            # middle
            obsList.append(BIRD0)
            obsPos.append([WIDTH, bird_mid_y])
            lastObs = score
            print(88, 100)


while running:
    scoretext = FONT.render("Score " + str(score), 1, (100, 100, 100))
    # score += 1

    #print(int(score))

    # cloudspawn()
    # if cloudx <= 0:
    #    cloudx -= 1
    # if countcloud:
    #    lastcloud += 1
    obsSpawn()
    if not jumping and not duck:
        dinotexture = DINO1
        updatescreen()
        dinotexture = DINO2
        updatescreen()
    if duck:
        dinotexture = DINODUCK0
        updatescreen()
        dinotexture = DINODUCK1
        updatescreen()

    # moves obstacles forward and deletes them off screen
    for x in range(len(obsPos)):
        if obsList[x] == BIRD0 and obsPos[x][1] == bird_low_y:
            if(obsPos[x][0] - 96 < dinopos[0] < obsPos[x][0] + 92 and dinopos[1]+112 < bird_low_y):
                lose()
        elif obsList[x] == BIRD0 and obsPos[x][1] == bird_mid_y:
            if obsPos[x][0] - 96 < dinopos[0] < obsPos[x][0] + 92 and dinopos[1]+112 < bird_mid_y :
                lose()
        elif obsList[x] == BIRD0 and obsPos[x][1] == bird_high_y:
            if obsPos[x][0] - 96 < dinopos[0] < obsPos[x][0] + 92 and bird_high_y + 80 < dinopos[1]+112 < bird_high_y :
                lose()
        elif obsList[x] == CACTUSBIG:
            if(obsPos[x][0] - 60 < dinopos[0] < obsPos[x][0] + 92 and dinopos[1]+112 < cactusbig_y) :
                lose()
        elif obsList[x] == CACTUSHORD:
            if (obsPos[x][0] - 120 < dinopos[0] < obsPos[x][0] + 92 and dinopos[1]+112 < cactushord_y) :
                lose()
        elif obsList[x] == CACTUSSMALL:
            if (obsPos[x][0] - 40 < dinopos[0] < obsPos[x][0] + 92 and dinopos[1]+112 < cactussmall_y) :
                lose()
        # moves obs forward and deletes them
        if obsPos[x][0] < 5:
            obsPos.pop(x)
            obsList.pop(x)
        elif obsPos[x][0] > -20:
            obsPos[x][0] -= score/15



    updatescreen()
    for event in pygame.event.get():
        # Check if X is pressed
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        # Check for event KEYDOWN

        if event.type == pygame.KEYDOWN:
            if event.key == K_F11:
                keys[0] = True
            # Full screen key - F11
            if event.key == K_UP or event.key == K_SPACE:
                keys[1] = True
            # Duck key - K_DOWN
            if event.key == K_DOWN:
                keys[2] = True

        # Check for EVENT KEYUP
        if event.type == pygame.KEYUP:
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
            pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN, pygame.NOFRAME)
            # print(pygame.display.get_wm_info())
            # isFull = True
            # elif isFull:
            # pygame.display.set_mode((width, height))
            # isFull = False
            print('Toggled Full screen')
        if keys[1]:
            jumping = True
            #print('Jump')
            dinotexture = DINOJUMP
            pygame.mixer.music.play()
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
            #print('Duck')
            duck = True
            dinopos[1] = 544
            # updatescreen()
        if not keys[2]:
            duck = False
            dinopos[1] = 500
