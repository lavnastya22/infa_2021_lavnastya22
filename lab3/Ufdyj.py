'''
author: lavnastya22
'''

import pygame
from pygame.draw import *

pygame.init()

#create display
FPS = 30
pygame.display.set_caption("Unicorn_2")
sc = pygame.display.set_mode((600, 800))    

#colours
usu = (0, 255, 255)
green = (0, 255, 0)
ggreen = (0, 128, 0)
apple = (255, 204, 170)
applee = (255, 170, 170)
grey = (230, 230, 230)
sun = (255, 221, 85)
white = (255, 255, 255)
corn = (233, 175, 175)
brown = (233, 198, 175)
skinny = (255, 238, 170)
yellow = (229, 255, 128)
byeee = (175, 233, 221)
violet = (244, 215, 227)
purple = (221, 175, 233)
eye = (229, 128, 255)
black = (0, 0, 0)

sc.fill(usu)

#grace
rect(sc, green, [0, 350, 800, 550])

#sun
for i in range (230):
    circle(sc, (255-i*255/230, 221+34*i/230, 85+170*i/230), [450, 120,], i, 2)
i+=1


##unicorn, x,y - coordinates, Z - proportionality
def unicorn (x,y, z, flip):

    #creat surface
    surf = sc.convert_alpha(pygame.Surface((10, 10)))
    surf.fill([0,0,0,0])

    #cauda
    ellipse(surf, corn,  [12, 240, 60, 14])
    ellipse(surf, yellow,[2,  295, 76, 23])
    ellipse(surf, brown, [15, 288, 50, 15])
    ellipse(surf, yellow,[40, 285, 50, 15])
    ellipse(surf, skinny,[42, 295, 50, 20])
    ellipse(surf, corn,  [62, 206, 55, 15])
    ellipse(surf, brown, [47, 214, 45, 35])
    ellipse(surf, yellow,[22, 251, 45, 15])
    ellipse(surf, yellow,[40, 261, 80, 23])
    ellipse(surf, brown, [57, 250, 45, 20])
    ellipse(surf, skinny,[30, 234, 65, 25])
    ellipse(surf, skinny,[28, 261, 40, 20])
    ellipse(surf, yellow,[20, 251, 45, 12])
    ellipse(surf, violet,[37, 269, 55, 15])
    ellipse(surf, byeee, [15, 268, 32, 12])
    ellipse(surf, byeee, [15, 276, 50, 15])
    ellipse(surf, violet,[37, 278, 55, 14])
    ellipse(surf, byeee, [65, 278, 42, 13])
    ellipse(surf, purple,[0,  282, 60, 14])
    ellipse(surf, violet,[30, 304, 55, 15])
    ellipse(surf, byeee, [70, 303, 32, 12])
    ellipse(surf, byeee, [47, 311, 50, 15])
    ellipse(surf, violet,[22, 317, 55, 14])
    ellipse(surf, byeee, [12, 314, 42, 13])
    ellipse(surf, purple,[52, 322, 65, 16])

    #unicorn's body
    ellipse(surf, white, [82, 185, 220, 100])
    
    #unicorn's legs
    rect(surf, white, [97, 226, 16, 130])       
    rect(surf, white, [140, 210, 17, 130])
    rect(surf, white, [224, 231, 18, 130])
    rect(surf, white, [267, 209, 15, 130])

    #unicorn's neck and head
    polygon(surf, white, [[292, 235], [182,205], [252, 100], [292, 135]]) 
    ellipse(surf, white, [242, 97, 68, 32])
    ellipse(surf, white, [267, 112, 73, 34])

    #eye
    ellipse(surf, eye, [282, 112, 19, 18])
    ellipse(surf, black, [291, 116, 8, 8])
    line(surf, white, [287, 115], [293,118], 3)

    #corn
    polygon(surf, corn, [[281, 100], [259, 98], [281, 0]]) 

    #griva
    ellipse(surf, corn,  [227, 88, 44, 22])      
    ellipse(surf, brown, [222, 116, 45, 20])
    ellipse(surf, corn,  [207, 106, 55, 15])
    ellipse(surf, brown, [192, 113, 45, 35])
    ellipse(surf, yellow,[167, 150, 45, 15])
    ellipse(surf, yellow,[185, 160, 80, 23])
    ellipse(surf, brown, [202, 149, 45, 20])
    ellipse(surf, skinny,[175, 133, 65, 25])
    ellipse(surf, skinny,[173, 160, 40, 20]) 
    ellipse(surf, yellow,[165, 150, 45, 12])
    ellipse(surf, byeee, [160, 167, 32, 12])
    ellipse(surf, violet,[182, 168, 55, 15])
    ellipse(surf, byeee, [160, 175, 50, 15])
    ellipse(surf, violet,[182, 177, 55, 14])
    ellipse(surf, byeee, [210, 177, 42, 13])
    ellipse(surf, purple,[145, 181, 60, 14])

    #flip
    if flip == True:
        surf = pygame.transform.flip(surf, True, False)

    #scale
    surf = pygame.transform.scale(surf, (3*z, 4*z))

    
    sc.blit(surf, (x, y))


##three, x,y - coordinates, a,b - linear size
def three (x,y,a,b):

    #creat surface
    three = sc.convert_alpha(pygame.Surface((10, 10)))
    three.fill([0,0,0,0])

    #tree
    rect(three, grey, [113, 355, 40, 110])
    ellipse(three, ggreen, [43,  0, 170, 190])
    ellipse(three, green, [43,  0, 170, 190], 3)
    ellipse(three, ggreen, [0, 115, 290, 150])
    ellipse(three, green, [0, 115, 290, 150], 3)
    ellipse(three, ggreen, [45, 210, 190, 150])
    ellipse(three, green, [45, 210, 190, 150], 3)

    #apples
    ellipse(three, apple, [173, 310, 40, 40])
    ellipse(three, green, [173, 310, 40, 40], 3)
    ellipse(three, apple, [143, 38, 42, 38])
    ellipse(three, green, [143, 38, 42, 38], 3)
    ellipse(three, apple, [223, 185, 42, 38])
    ellipse(three, green, [223, 185, 42, 38], 3)
    ellipse(three, applee, [15, 180, 42, 38])
    ellipse(three, green, [15, 180, 42, 38],3)

    #scale
    three = pygame.transform.scale(three, (a, b))

    sc.blit(three, (x, y))


unicorn (130, 450, 180, False)
unicorn (280, 280, 90,  False)
unicorn (240, 370, 135, True)
unicorn (390, 280, 60,  True)

three (20,   20, 600, 750)
three (120, 270, 400, 350)
three (-50, 100, 320, 800)
three (50,  320, 390, 520)
three (-15, 470, 360, 490)


pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
