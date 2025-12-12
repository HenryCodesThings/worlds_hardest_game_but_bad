import pygame
import runpy

pygame.init()
pygame.mixer.init()
speed = 2
x = 20
y = 300
running = True
#---COLORS---
bg = (220, 208, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)

#---IMAGES---
icon = pygame.image.load("dist/images/whgbb icon.png")
endscreen = pygame.image.load("dist/images/whgbb endscreen.png")
startscreen = pygame.image.load("dist/images/whgbb start screen.png")
cubert = pygame.image.load("dist/images/whgbb cubert.png")

def movement(x, y, speed):
    pygame.time.delay(5)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and y > 37:
        y -= speed
    if keys[pygame.K_s] and y < 501:
        y += speed
    if keys[pygame.K_a] and x > 15.5:
        x -= speed
    if keys[pygame.K_d] and x < 923:
        x += speed

    return x, y
def kys_NOW(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    return running