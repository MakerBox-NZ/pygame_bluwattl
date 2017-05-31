import pygame
import sys
import os

'''OBJECTS'''



'''SETUP'''
screenX = 960
screenY = 720
green = [0, 255, 0]
fps = 40
afps = 4
clock = pygame.time.Clock()

pygame.init()

main = True

screen = pygame.display.set_mode([screenX, screenY])


'''LOOP'''
#screen.fill()

while main == True:
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False

    screen.fill(green)
    pygame.display.flip
    clock.tick(fps)
