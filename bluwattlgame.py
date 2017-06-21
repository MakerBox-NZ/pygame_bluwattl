'''LIBRARIES'''
import pygame
import sys
import os
'''OBJECTS'''
class Player(pygame.sprite.Sprite):
    #spawn and dab FAKE
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.momentumX = 0
        self.momentumY = 0
        self.images = [ ]
        img = pygame.image.load(os.path.join('images','hero.png')).convert()
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.image.convert_alpha()
        self.image.set_colorkey(alpha)
    def control(self, x, y):
        #print('in control') #debug
        self.momentumX += x
        self.momentumY += y
    def update(self):
        #print('update') #debug
        currentX = self.rect.x
        nextX = currentX + self.momentumX
        self.rect.x = nextX
        currentY = self.rect.y
        nextY = currentY + self.momentumY
        self.rect.y = nextY
'''SETUP'''
screenX = 360 * 4
screenY = 240 * 4
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
player.rect.y = 0
movingsprites = pygame.sprite.Group()
movingsprites.add(player)
movesteps = 10

'''LOOP'''
while main == True:
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False
            if event.key == pygame.K_LEFT or ord('a'):
                print('left stop')
                player.control(movesteps, 0)
            if event.key == pygame.K_RIGHT or ord('d'):
                print('right stop')
                player.control(-movesteps, 0)
            if event.key == pygame.K_UP or ord('w'):
                print('up stop')
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or ord('a'):
                print('left')
                player.control(-movesteps, 0)
            if event.key == pygame.K_RIGHT or ord('d'):
                print('right')
                player.control(movesteps, 0)
            if event.key == pygame.K_UP or ord('w'):
                print('up')

    screen.blit(backdrop, backdropRect)
    player.update()
    movingsprites.draw(screen)
    pygame.display.flip()
    clock.tick(fps)
