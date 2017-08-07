'''LIBRARIES'''
import pygame
import sys
import os
import turtle
'''OBJECTS'''
class Platform(pygame.sprite.Sprite):
    '''
    Create a platform
    '''
    # x location, y location, image width, image height, image file    
    def __init__(self,xloc,yloc,imgw,imgh,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([imgw,imgh])
        self.image.convert_alpha()
        self.image.set_colorkey(alpha)
        self.blockpic = pygame.image.load(img).convert()
        self.rect = self.image.get_rect()
        self.rect.y = yloc
        self.rect.x = xloc
        
        # paint the image into the blocks
        self.image.blit(self.blockpic,(0,0),(0,0,imgw,imgh))


    def level1():
        platform_list = pygame.sprite.Group()
        block = Platform(0, 200, 768, 218, os.path.join('images', 'block0.png'))
        platform_list.add(block)

        return platform_list
class Player(pygame.sprite.Sprite):
    #spawn
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.momentumX = 0
        self.momentumY = 0
        self.score = 0
        self.images = [ ]
        img = pygame.image.load(os.path.join('images','hero.png')).convert()
        self.images.append(img)
        self.image = self.images[0]
        self.image = pygame.transform.scale(self.image, (int(100), int(100)))
        self.rect = self.image.get_rect()
        self.image.convert_alpha()
        self.image.set_colorkey(alpha)
    def control(self, x, y):
        #print('in control') #debug
        self.momentumX += x
        self.momentumY += y
    def update(self,enemy_list):
        #print('update') #debug
        currentX = self.rect.x
        nextX = currentX + self.momentumX
        self.rect.x = nextX
        currentY = self.rect.y
        nextY = currentY + self.momentumY
        self.rect.y = nextY
        enemy_hit_list = pygame.sprite.spritecollide(self, enemy_list, False)
        for enemy in enemy_hit_list:
            self.score -= 1
            print(self.score)
class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('images', img))
        self.image.convert_alpha()
        self.image.set_colorkey(alpha)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0
    def move(self):
        if self.counter >= 0 and self.counter <= 30:
            self.rect.x += 2
        elif self.counter >= 30 and self.counter <= 60:
            self.rect.x -= 2
        else:
            self.counter = 0
            print('reset')

        self.counter += 1
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
platform_list = Platform.level1()
player = Player() #Spawn REAL
player.rect.x = 0
player.rect.y = 0
movingsprites = pygame.sprite.Group()
movingsprites.add(player)
movesteps = 10
enemy = Enemy(100, 50, 'badguy.png')
enemy_list = pygame.sprite.Group()
enemy_list.add(enemy)
'''LOOP'''
while main == True:
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
                main = False
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                
               player.control(movesteps, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'): 
               player.control(-movesteps, 0)
            if event.key == ord(')'):
                print('           o    o  ')
                print('         \        /')
                print('          \      / ')
                print('           \____/  ')
                print('   You found the secret!       ')
            if event.key == pygame.K_UP or event.key == ord('w'):
               pass
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
               pass
               player.control(-movesteps, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
               pass
               player.control(movesteps, 0)
            if event.key == pygame.K_UP or event.key == ord('w'):
               pass

    screen.blit(backdrop, backdropRect)
    platform_list.draw(screen)
    player.update(enemy_list)
    movingsprites.draw(screen)
    enemy_list.draw(screen)
    enemy.move()
    pygame.display.flip()
    clock.tick(fps)
