'''
author: lavnastya22
'''

import pygame
from pygame.draw import *

pygame.init()

#create display
FPS = 30
pygame.display.set_caption("Unicorn_1")
screen = pygame.display.set_mode((600, 800))  

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

screen.fill(usu)

#grace, tree, apples, sun
rect(screen, green, [0, 350, 800, 550])

rect(screen, grey, [80, 455, 40, 110])
ellipse(screen, ggreen, [-33, 215, 290, 150])
ellipse(screen, ggreen, [10, 100, 170, 190])
ellipse(screen, ggreen, [12, 310, 190, 150])

ellipse(screen, apple, [140, 410, 40, 40])
ellipse(screen, apple, [110, 138, 42, 38])
ellipse(screen, apple, [190, 285, 42, 38])
ellipse(screen, applee, [-18, 280, 42, 38])

ellipse(screen, sun, [480, -25, 200, 180])

#cauda
ellipse(screen, corn,  [210, 585, 60, 14])
ellipse(screen, yellow,[200, 640, 76, 23])
ellipse(screen, brown, [213, 633, 50, 15])
ellipse(screen, yellow,[238, 630, 50, 15])
ellipse(screen, skinny,[240, 640, 50, 20])
ellipse(screen, corn,  [260, 551, 55, 15])
ellipse(screen, brown, [245, 558, 45, 35])
ellipse(screen, yellow,[220, 595, 45, 15])
ellipse(screen, yellow,[238, 605, 80, 23])
ellipse(screen, brown, [255, 594, 45, 20])
ellipse(screen, skinny,[228, 578, 65, 25])
ellipse(screen, skinny,[226, 605, 40, 20])
ellipse(screen, yellow,[218, 595, 45, 12])
ellipse(screen, byeee, [213, 612, 32, 12])
ellipse(screen, violet,[235, 613, 55, 15])
ellipse(screen, byeee, [213, 620, 50, 15])
ellipse(screen, violet,[235, 622, 55, 14])
ellipse(screen, byeee, [263, 622, 42, 13])
ellipse(screen, purple,[198, 626, 60, 14])
ellipse(screen, violet,[228, 649, 55, 15])
ellipse(screen, byeee, [268, 648, 32, 12])
ellipse(screen, byeee, [245, 656, 50, 15])
ellipse(screen, violet,[220, 662, 55, 14])
ellipse(screen, byeee, [210, 659, 42, 13])
ellipse(screen, purple,[250, 672, 65, 16])
    
#unicorn's body
ellipse(screen, white, [280, 530, 220, 100])  

#unicorn's legs
rect(screen, white, [295, 571, 16, 130])  
rect(screen, white, [338, 555, 17, 130])
rect(screen, white, [422, 576, 18, 130])
rect(screen, white, [465, 554, 15, 130])

#unicorn's neck and head
polygon(screen, white, [[490, 580], [380,550], [450, 445], [490, 480]]) 
ellipse(screen, white, [440, 442, 68, 32])
ellipse(screen, white, [465, 457, 73, 34])

#eye
ellipse(screen, eye, [480, 457, 19, 18]) 
ellipse(screen, black, [488, 461, 9, 9])
line(screen, white, [484, 461], [491,465], 3)

#corn
polygon(screen, corn, [[479, 445], [457, 443], [479, 345]]) 

#griva
ellipse(screen, corn,  [425, 433, 44, 22]) 
ellipse(screen, brown, [420, 461, 45, 20])
ellipse(screen, corn,  [405, 451, 55, 15])
ellipse(screen, brown, [390, 458, 45, 35])
ellipse(screen, yellow,[365, 495, 45, 15])
ellipse(screen, yellow,[383, 505, 80, 23])
ellipse(screen, brown, [400, 494, 45, 20])
ellipse(screen, skinny,[373, 478, 65, 25])
ellipse(screen, skinny,[371, 505, 40, 20]) 
ellipse(screen, yellow,[363, 495, 45, 12])
ellipse(screen, byeee, [358, 512, 32, 12])
ellipse(screen, violet,[380, 513, 55, 15])
ellipse(screen, byeee, [358, 520, 50, 15])
ellipse(screen, violet,[380, 522, 55, 14])
ellipse(screen, byeee, [408, 522, 42, 13])
ellipse(screen, purple,[343, 526, 60, 14])

 
pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
