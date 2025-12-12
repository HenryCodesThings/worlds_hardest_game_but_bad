from source import *

pygame.init()
pygame.mixer.init()

#---SETTING UP WINDOW---
width = 1000
height = 600
window_3 = pygame.display.set_mode((width, height))
pygame.display.set_caption('Worlds hardest game but bad level 4')
pygame.display.set_icon(icon)

end_reached_time = None
level_beat = False
lvl_one_beat = False
x = 20
y = 300
ob_x = 394
door_y = 36
ob_height = 36
speed = 2


#---COLORS---
bg = (220, 208, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
#---MAIN LOOP---
running_4 = True
while level_beat == False and running_4 == True:
    pygame.time.delay(5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_4 = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and y > 37:
        y -= speed
    if keys[pygame.K_s] and y < 501:
        y += speed
    if keys[pygame.K_a] and x > 15.5:
        x -= speed
    if keys[pygame.K_d] and x < 923:
        x += speed
    window_3.fill(bg)

    map_rect = pygame.draw.rect(window_3, white, (15, 36.5, 963.5, 520))
    spawn = pygame.draw.rect(window_3, green, (15, 260, 100, 100))
    rect_2 = window_3.blit(cubert, (x, y))
    end = pygame.draw.rect(window_3, green, (878, 36.5, 100, 100))
    pygame.display.update()