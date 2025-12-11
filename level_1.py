from source import *
import pygame

#---MUSIC---
pygame.mixer.music.load("audio/Hip Shop - Toby Fox (youtube).mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

#---SETTING UP WINDOW---
width = 1000
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Worlds hardest game but bad')
pygame.display.set_icon(icon)
window.blit(startscreen, (0, 0))

#---VARIABLES---
time_since_button = None
end_reached_time = None
level_beat = False
ob_x = 394
door_y = 36
ob_height = 36

#---START SCREEN LOOP---
#TODO make start screen look more pleasing (like the one in deltarune)
waiting_to_start = True
while waiting_to_start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_1] and waiting_to_start:
        waiting_to_start = False
    if keys[pygame.K_2] and waiting_to_start:
        pygame.mixer.music.load("audio/Need A Hand! With Lyrics (Reupload) - Deltarune Chapter 4 OST - goldenflowers (youtube).wav")
        pygame.mixer.music.play(-1)
        runpy.run_path("level_2.py")
        pygame.quit()
    if keys[pygame.K_3] and waiting_to_start:
        pygame.mixer_music.load("audio/Need A Hand! With Lyrics (Reupload) - Deltarune Chapter 4 OST - goldenflowers (youtube).wav")
        pygame.mixer.music.play(-1)
        runpy.run_path("level_3.py")
        pygame.quit()
    window.blit(startscreen, (0, 0))
    pygame.display.update()

#---MAIN LOOP---
pygame.display.set_caption('Worlds hardest game but bad level 1')
pygame.mixer_music.load("audio/Need A Hand! With Lyrics (Reupload) - Deltarune Chapter 4 OST - goldenflowers (youtube).wav")
pygame.mixer.music.play(-1)
running = True
while running:

    running = kys_NOW(running)
    x, y = movement(x,y,speed)
    window.fill(bg)
    #---EVERYTHING DRAWN ONTO SCREEN---
    #TODO make these look less... terrible
    map_rect = pygame.draw.rect(window, white, (15, 36.5, 963.5, 520))
    end = pygame.draw.rect(window, green, (878, 36.5, 100, 100))
    spawn = pygame.draw.rect(window, green, (15, 260, 100, 100))
    button_outline = pygame.draw.rect(window, black, (339, 36, 54, 54))
    button = pygame.draw.rect(window, red, (341, 38, 50, 50))
    obsticle = pygame.draw.rect(window, black, (ob_x, ob_height, 30, 300))
    obsticle2 = pygame.draw.rect(window, black, (308, ob_height, 30, 300))
    door = pygame.draw.rect(window, black, (610, door_y, 30, 520))
    rect_2 = window.blit(cubert, (x,y))
    #---COLLISION---
    if rect_2.colliderect(obsticle) or rect_2.colliderect(obsticle2) or rect_2.colliderect(door):
        x = 20
        y = 300
        door_y = 36
    if rect_2.colliderect(button_outline):
        if time_since_button is None:
            door_y = 9999
            time_since_button = pygame.time.get_ticks()

        if time_since_button is not None:
            elapsed_time = pygame.time.get_ticks() - time_since_button
        if elapsed_time > 5000:
            door_y = 36
            time_since_button = None
    if rect_2.colliderect(end) and end_reached_time is None:
        end_reached_time = pygame.time.get_ticks()
    if end_reached_time is not None:
        window.blit(endscreen, (0, 0))
        elapsed_time = pygame.time.get_ticks() - end_reached_time
        if elapsed_time > 3000:
            level_beat = True
            running = False
    pygame.display.update()
    if level_beat:
        next_level_beat = False
        running = False
        import level_2