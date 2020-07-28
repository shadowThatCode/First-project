import pygame
from pygame.locals import *
import random

#intialzing game
pygame.init()
screenWidth, screenHeight = 600, 600
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Snake")

#direction
x = [300] 
y = [300]
posX, posY = None, None
right = True
left = True
up = True
down = True

#size & speed
width = 20
height = 20
speed = 23

#in-game value
apple = [305, 400]
ateApple = False
bodyDistance = 23
delay = pygame.time.Clock()

#Running game
runGame = True
while runGame:
    screen.fill((0, 0, 0))

    #quitting game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False

    keys = pygame.key.get_pressed()
    if keys[K_q]:
        runGame = False  

    #snake body
    for i in range(len(x)-1 and len(y)-1, 0, -1):
        x[i] = x[i-1]
        y[i] = y[i-1]

    for i in range(len(x) and len(y)):
        pygame.draw.rect(screen, (255, 0, 0), (x[i], y[i], width, height))

    #movement
    if keys[K_a] and left or keys[K_LEFT] and left:
        posX = -1
        posY = 0
        down = True
        up = True
        right = False

    if keys[K_d] and right or keys[K_RIGHT] and right:
        posX = 1
        posY = 0
        down = True
        up = True
        left = False
    if keys[K_s] and down or keys[K_DOWN] and down:
        posY = -1
        posX = 0
        left = True
        right = True
        up = False
    if keys[K_w] and up or keys[K_UP] and up:
        posY = 1
        posX = 0
        left = True
        right = True
        down = False

    #constant movement
    if posX == -1 and posY == 0:
        x[0] -= speed
    if posX == 1 and posY == 0:
        x[0] += speed
    if posY == -1 and posX == 0:
        y[0] += speed
    if posY == 1 and posX == 0:
        y[0] -= speed
    
    #Wall
    if x[0] >= screenWidth - 20:
        runGame = False
    if x[0] <= 0:
        runGame = False
    if y[0] >= screenHeight - 20:
        runGame = False
    if y[0] <= 0:
        runGame = False

    #Death by body
    for i in range(len(x)-1 and len(y)-1):
        if x[0] >= x[i+1] - 20 and x[0] <= x[i+1] + 10 and y[0] >= y[i+1] - 20 and y[0] <= y[i+1] + 10:
            runGame = False

    #apple
    if not ateApple:
        pygame.draw.rect(screen, (255, 255, 255), (apple[0], apple[1], 10, 10))
        if x[0] >= apple[0] - 20 and x[0] <= apple[0] + 10 and y[0] <= apple[1] + 10 and y[0] >= apple[1] - 20:
            for i in range(3):
                x.append(x[0])
                y.append(y[0])
            ateApple = True
            
    if ateApple:
        apple[0] = random.randint(1, 580)
        apple[1] = random.randint(1, 580)
        for i in range(len(x) and len(y)):
            if apple[0] - 20 <= x[i] and apple[0] + 10 >= x[i] and  apple[1] + 12 >= y[i] and apple[1] - 20 <= y[i] :
                apple[0] = random.randint(1, 580)
                apple[1] = random.randint(1, 580)
            else:
                ateApple = False

    delay.tick(15)

    pygame.display.update()
pygame.quit()