from source import *

#---SETTING UP WINDOW---
width = 1000
height = 600
window = pygame.display.set_mode((width, height))
window_2 = pygame.display.set_mode((width, height))
pygame.display.set_caption('Worlds hardest game but bad level 2')
pygame.display.set_icon(icon)
window.blit(startscreen, (0, 0))

end_reached_time = None
level_two_beat = False
lvl_one_beat = False
x = 20
y = 300
ob_x = 394
door_y = 36
ob_height = 36
speed = 2
block_x = 500
block_y = 300
block_speed = 18

direction = "down"
#---COLORS---
bg = (220, 208, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
#---MAIN LOOP---
running_2 = True
speed = 2
while level_two_beat == False and running_2 == True:
    pygame.time.delay(5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_2 = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and y > 37:
        y -= speed
    if keys[pygame.K_s] and y < 501:
        y += speed
    if keys[pygame.K_a] and x > 15.5:
        x -= speed
    if keys[pygame.K_d] and x < 923:
        x += speed
    window_2.fill(bg)
    map_rect = pygame.draw.rect(window, white, (15, 36.5, 963.5, 520))

    center_x = 496.75
    center_y = 296.5
    square_radius = 150

    left_edge = center_x - square_radius  # 346.75
    right_edge = center_x + square_radius  # 646.75
    top_edge = center_y - square_radius  # 146.5
    bottom_edge = center_y + square_radius  # 446.5

    if direction == "down":
        block_y += block_speed
        if block_y >= bottom_edge:
            block_y = bottom_edge
            direction = "left"

    elif direction == "left":
        block_x -= block_speed
        if block_x <= left_edge:
            block_x = left_edge
            direction = "up"

    elif direction == "up":
        block_y -= block_speed
        if block_y <= top_edge:
            block_y = top_edge
            direction = "right"

    elif direction == "right":
        block_x += block_speed
        if block_x >= right_edge:
            block_x = right_edge
            direction = "down"

    block = pygame.draw.rect(window, black,(block_x, block_y, 10, 10))
    button_outline2 = pygame.draw.rect(window, black, (494.75, 294.5, 54, 54))
    button2 = pygame.draw.rect(window, red, (496.75, 296.5, 50, 50))
    spawn = pygame.draw.rect(window, green, (15, 260, 100, 100))
    rect_2 = window.blit(cubert, (x,y))
    door2 = pygame.draw.rect(window, black, (700, door_y, 30, 520))
    end = pygame.draw.rect(window, green, (878, 36.5, 100, 100))
    if rect_2.colliderect(button_outline2):
        door_y = 9999
    if rect_2.colliderect(door2):
        x = 20
        y = 300
    if block.colliderect(rect_2):
        x = 20
        y = 300
        door_y = 36
    if rect_2.colliderect(end) and end_reached_time is None:
        end_reached_time = pygame.time.get_ticks()
    if end_reached_time is not None:
        window.blit(endscreen, (0, 0))
        elapsed_time = pygame.time.get_ticks() - end_reached_time
        if elapsed_time > 3000:
            level_two_beat = True
            running = False
    pygame.display.update()
    if level_two_beat:
        level_three_beat = False
        runpy.run_path(resource_path('level_3.py'))
        running_2 = False
    pygame.display.update()