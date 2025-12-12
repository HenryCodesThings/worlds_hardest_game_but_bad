from source import *

#---SETTING UP WINDOW---
width = 1000
height = 600
window_3 = pygame.display.set_mode((width, height))
pygame.display.set_caption('Worlds hardest game but bad level 3')
pygame.display.set_icon(icon)

direction = "right"
direction2 = "down"
filler_dot_speed = 13
thing_speed = 1
filler_dot_y = 37
thing_x = 650
end_reached_time = None
level_beat = False
lvl_one_beat = False
ob_x = 394
door_y = 36
ob_height = 36
block_x = 500
block_y = 300
block_speed = 18

#---MAIN LOOP---
running_3 = True
speed = 2
while level_beat == False and running_3 == True:
    pygame.time.delay(5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_3 = False
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
    if direction == "right":
        thing_x += thing_speed
        if thing_x >= 740:
            direction = "left"
    elif direction == "left":
        thing_x -= thing_speed
        if thing_x <= 600:
            direction = "right"


    if direction2 == "down":
        filler_dot_y += filler_dot_speed
        if filler_dot_y >= 540:
            direction2 = "up"
    elif direction2 == "up":
        filler_dot_y -= filler_dot_speed
        if filler_dot_y <= 37:
            direction2 = "down"
    map_rect = pygame.draw.rect(window_3, white, (15, 36.5, 963.5, 520))
    filler_dot = pygame.draw.rect(window_3, blue, (200, filler_dot_y, 10, 10))
    thing = pygame.draw.rect(window_3, blue,(thing_x, 300, 10, 10))
    thing_2 = pygame.draw.rect(window_3, blue,(thing_x, 400, 10, 10))
    spawn = pygame.draw.rect(window_3, green, (15, 260, 100, 100))
    rect_2 = window_3.blit(cubert, (x,y))
    end = pygame.draw.rect(window_3, green, (878, 36.5, 100, 100))
    wall = pygame.draw.rect(window_3, black, (510, 36.5, 10, 160))
    wall2 = pygame.draw.rect(window_3, black, (440, 100, 10, 160))
    wall3 = pygame.draw.rect(window_3, black, (440, 260, 160, 10))
    wall4 = pygame.draw.rect(window_3, black, (510, 190, 160, 10))
    wall5 = pygame.draw.rect(window_3, black, (670, 190, 10, 160))
    wall6 = pygame.draw.rect(window_3, black, (600, 260, 10, 160))
    wall7 = pygame.draw.rect(window_3, black, (600, 396, 10, 160))
    wall8 = pygame.draw.rect(window_3, black, (740, 190, 10, 367))
    if rect_2.colliderect(wall) or rect_2.colliderect(wall2) or rect_2.colliderect(wall3) or rect_2.colliderect(wall4) or rect_2.colliderect(wall5) or rect_2.colliderect(wall6) or rect_2.colliderect(wall7) or rect_2.colliderect(wall8):
        x = 20
        y = 300
    if rect_2.colliderect(thing) or rect_2.colliderect(thing_2) or rect_2.colliderect(filler_dot):
        x = 20
        y = 300
    if rect_2.colliderect(end) and end_reached_time is None:
        end_reached_time = pygame.time.get_ticks()
    if end_reached_time is not None:
        window_3.blit(endscreen, (0, 0))
        elapsed_time = pygame.time.get_ticks() - end_reached_time
        if elapsed_time > 3000:
            level_beat = True
            running = False
    pygame.display.update()
    if level_beat:
        level_four_beat = False
        runpy.run_path('dist/level_4.py')
        running_3 = False
    pygame.display.update()
