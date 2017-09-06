'''LIBRARIES'''
import pygame
import sys
import os
import turtle
import pygame.freetype
'''OBJECTS'''

def stats(score):
    #display text, 1, colour (rgb)
    
    text_score = myfont.render("Score: "+str(score), 1, (45, 126, 255))
    screen.blit(text_score, (4, 4))

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
        #self.image = pygame.transform.scale(self.image, (int(50), int(10)))
        self.rect = self.image.get_rect()
        self.rect.y = yloc
        self.rect.x = xloc
        
        # paint the image into the blocks
        self.image.blit(self.blockpic,(0,0),(0,0,imgw,imgh))


    def level1():
        platform_list = pygame.sprite.Group()
        block = Platform(0, 200, 101, 77, os.path.join('images', 'block0.png'))
        platform_list.add(block)
        block = Platform(101, 200, 101, 77, os.path.join('images', 'block1.png'))
        platform_list.add(block)
        block = Platform(202, 200, 101, 77, os.path.join('images', 'block2.png'))
        platform_list.add(block)
        block = Platform(303, 200, 101, 77, os.path.join('images', 'block3.png'))
        platform_list.add(block)
        block = Platform(404, 200, 101, 77, os.path.join('images', 'block4.png'))
        platform_list.add(block)
        block = Platform(505, 200, 101, 77, os.path.join('images', 'block0.png'))
        platform_list.add(block)
        block = Platform(606, 200, 101, 77, os.path.join('images', 'block1.png'))
        platform_list.add(block)
        block = Platform(707, 200, 101, 77, os.path.join('images', 'block2.png'))
        platform_list.add(block)
        block = Platform(808, 200, 101, 77, os.path.join('images', 'block3.png'))
        platform_list.add(block)
        block = Platform(909, 200, 101, 77, os.path.join('images', 'block4.png'))
        platform_list.add(block)
        return platform_list
    def loot1():
        loot_list = pygame.sprite.Group()
        loot = Platform(150, 180, 32, 32, os.path.join('images', 'steak.png'))
        loot_list.add(loot)
        return loot_list
class Player(pygame.sprite.Sprite):
    #spawn
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.momentumX = 0
        self.momentumY = 0
        self.collide_delta = 0
        self.jump_delta = 0
        self.score = 0
        self.damage = 0
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
    def update(self,enemy_list,platform_list,loot_list, evol_list):
        #print('update') #debug
        currentX = self.rect.x
        nextX = currentX + self.momentumX
        self.rect.x = nextX
        currentY = self.rect.y
        nextY = currentY + self.momentumY
        self.rect.y = nextY

        if self.collide_delta < 6 and self.jump_delta < 6:
            self.jump_delta = 6*2
            self.momentumY -=33
            self.collide_delta += 6
            self.jump_delta += 6
    
        enemy_hit_list = pygame.sprite.spritecollide(self, enemy_list, False)
        '''for enemy in enemy_hit_list:
            self.score -= 1
            print(self.score)'''

        loot_hit_list = pygame.sprite.spritecollide(self, loot_list, False)
        for loot in loot_hit_list:
            self.score += 1
            print(self.score)
            loot_list.remove(loot)

        if self.damage == 0:
            for enemy in enemy_hit_list:
                if not self.rect.contains(enemy):
                    self.damage = self.rect.colliderect(enemy)
                    print(self.score)

        if self.damage == 1:
            idx = self.rect.collidelist(enemy_hit_list)
            if idx == -1:
                self.damage = 0
                self.score -= 1
        
        block_hit_list = pygame.sprite.spritecollide(self, platform_list, False)
        if self.momentumX > 0:
            for block in block_hit_list:
                self.rect.y = currentY
                self.rect.x = currentX+9
                self.momentumY = 0
                self.collide_delta = 0
        if self.momentumY > 0:
            for block in block_hit_list:
                self.rect.y = currentY
                self.momentumY = 0
                self.collide_delta = 0
    def jump (self, platform_list):
        self.jump_delta = 0
    def gravity(self):
        self.momentumY += 3.2
        if self.rect.y > 960 and self.momentumY >= 0:
            self.momentumY = 0
            self.rect.y = screenY-20
class PowerUp(pygame.sprite.Sprite):
    def __init__(self,xloc,yloc,imgw,imgh,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([imgw,imgh])
        self.image.convert_alpha()
        self.image.set_colorkey(alpha)
        self.blockpic = pygame.image.load(img).convert()
        self.rect = self.image.get_rect()
        self.rect.y = yloc
        self.rect.x = xloc
        self.image.blit(self.blockpic,(0,0),(0,0,imgw,imgh))
                                                                                
    def evolution1():
        evol_list = pygame.sprite.Group()
        evol = PowerUp(500, 160, 32, 32, os.path.join('images', 'steak.png'))
        evol_list.add(evol)
        return evol_list
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
screenX = 480
screenY = 360
alpha = (0,0,0)
black = (1,1,1)
white = (255,255,255)
fps = 40
afps = 4
clock = pygame.time.Clock()
pygame.init()
pygame.font.init()

font_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "fonts", "Fredoka One.ttf")
font_size = 24
myfont = pygame.font.Font(font_path, font_size)
main = True
screen = pygame.display.set_mode([screenX, screenY])
backdrop = pygame.image.load(os.path.join('images','backgroundwithlogo.png')).convert()
backdropRect = screen.get_rect()
platform_list = Platform.level1()
loot_list = Platform.loot1()
evol_list = PowerUp.evolution1()
player = Player() #Spawn REAL
player.rect.x = 0
player.rect.y = 0
movingsprites = pygame.sprite.Group()
movingsprites.add(player)
forwardX = 300
backwardX = 100
movesteps = 10
enemy = Enemy(500, 90, 'badguy.png')
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
            if event.key == ord('0'):
                print('           o    o  ')
                print('         \        /')
                print('          \      / ')
                print('           \____/  ')
                print('   You found the secret!       ')
            if event.key == ord('p'):
                print('Pika')
                print('Chu')
                print('Pika')
                print('Pi')
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
               player.jump(platform_list)
    if player.rect.x >= forwardX:
        scroll = player.rect.x - forwardX
        player.rect.x = forwardX
        for platform in platform_list:
            platform.rect.x -= scroll
        for enemy in enemy_list:
            enemy.rect.x -= scroll
        for loot in loot_list:
            platform.rect.x -= scroll
        for evol in evol_list:
            evol.rect.x -= scroll
    if player.rect.x <= backwardX:
        scroll = min(1, (backwardX - player.rect.x))
        player.rect.x = backwardX
        for platform in platform_list:
            platform.rect.x += scroll
        for enemy in enemy_list:
            enemy.rect.x += scroll
        for loot in loot_list:
            platform.rect.x += scroll
        for evol in evol_list:
            evol.rect.x += scroll
    screen.blit(backdrop, backdropRect)
    platform_list.draw(screen)
    player.gravity()
    player.update(enemy_list, platform_list, loot_list, evol_list)
    movingsprites.draw(screen)
    enemy_list.draw(screen)
    loot_list.draw(screen)
    evol_list.draw(screen)
    enemy.move()
    stats(player.score)
    pygame.display.flip()
    clock.tick(fps)
