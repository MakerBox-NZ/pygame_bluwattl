'''LIBRARIES'''
import pygame
import sys
import os
'''OBJECTS'''
class Player(pygame.sprite.Sprite):
    #spawn and dab FAKE
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = [ ]
        img = pygame.image.load(os.path.join('images','hero.png')).convert()
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.image.convert_alpha()
        self.image.set_colorkey(alpha)
'''SETUP'''
screenX = 240
screenY = 360
alpha = (0,0,0)
black = (1,1,1)
white = (255,255,255)
fps = 40
afps = 4
clock = pygame.time.Clock()
pygame.init()
main = True
screen = pygame.display.set_mode([screenX, screenY])
backdrop = pygame.image.load(os.path.join('images','background.png')).convert()
backdropRect = screen.get_rect()
player = Player() #Spawn REAL
player.rect.x = 0
player.rect.x = 0
movingsprites = pygame.sprite.Group()
movingsprites.add(player)

'''LOOP'''
while main == True:
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False
                if event.key == pygame.K_LEFT:
                    print('left stop')
                if event.key == pygame.K_RIGHT:
                    print('right stop')
                if event.key == pygame.K_UP:
                    print('up stop')
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        print('left')
                    if event.key == pygame.K_RIGHT:
                        print('right')
                    if event.key == pygame.K_UP:
                        print('up')
    screen.blit(backdrop, backdropRect)
    movingsprites.draw(screen)
    pygame.display.flip()
    clock.tick(fps)
