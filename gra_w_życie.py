import pygame, sys, os
from pygame.locals import *


pygame.init()
plansza = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Gra w życie')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (129, 187, 129)
GRAY = (225, 225, 225)

tab = [[False for x in range(-1,40)] for y in range(-1,40)]
tab2 = [[False for x in range(-1,40)] for y in range(-1,40)]
zliczona = [[False for x in range(-1,40)] for y in range(-1,40)]

lecimy = False


FPS1=60
FPS=5

zegar = pygame.time.Clock()


licznik = 0




while True:
    plansza.fill(BLACK)

    
    
    
            


    if lecimy == True:
        tab2 = tab
        for x in range(-1, 40):
            for y in range(-1, 40):
                    licznik = 0
                    if x==0 and y==0:
                        if tab2[1][0] == True:
                            licznik+=1
                        if tab2[1][1] == True:
                            licznik+=1
                        if tab2[0][1] == True:
                            licznik+=1
                    if x==0 and y==39:
                        if tab2[0][38] == True:
                            licznik+=1
                        if tab2[1][38] == True:
                            licznik+=1
                        if tab2[1][39] == True:
                            licznik+=1
                    if x==39 and y==0:
                        if tab2[38][0] == True:
                            licznik+=1
                        if tab2[38][1] == True:
                            licznik+=1
                        if tab2[39][1] == True:
                            licznik+=1
                    if x==39 and y==39:
                        if tab2[38][39] == True:
                            licznik+=1
                        if tab2[38][38] == True:
                            licznik+=1
                        if tab2[39][38] == True:
                            licznik+=1
                    elif x==0 and y<39:
                        if tab2[0][y+1] == True:
                            licznik+=1
                        if tab2[1][y+1] == True:
                            licznik+=1
                        if tab2[0][y-1] == True:
                            licznik+=1
                        if tab2[1][y-1] == True:
                            licznik+=1
                        if tab2[1][y] == True:
                            licznik+=1
                    elif x==39:
                        if tab2[39][y+1] == True:
                            licznik+=1
                        if tab2[38][y+1] == True:
                            licznik+=1
                        if tab2[39][y-1] == True:
                            licznik+=1
                        if tab2[38][y-1] == True:
                            licznik+=1
                        if tab2[38][y] == True:
                            licznik+=1
                    elif y==0:
                        if tab2[x-1][0] == True:
                            licznik+=1
                        if tab2[x-1][1] == True:
                            licznik+=1
                        if tab2[x+1][0] == True:
                            licznik+=1
                        if tab2[x+1][1] == True:
                            licznik+=1
                        if tab2[x][1] == True:
                            licznik+=1
                    elif y==39:
                        if tab2[x-1][39] == True:
                            licznik+=1
                        if tab2[x-1][38] == True:
                            licznik+=1
                        if tab2[x+1][39] == True:
                            licznik+=1
                        if tab2[x+1][38] == True:
                            licznik+=1
                        if tab2[x][38] == True:
                            licznik+=1
                    else:
                        if tab2[x+1][y+1] == True:
                            licznik+=1
                        if tab2[x+1][y] == True:
                            licznik+=1
                        if tab2[x+1][y-1] == True:
                            licznik+=1
                        if tab2[x][y-1] == True:
                            licznik+=1
                        if tab2[x-1][y-1] == True:
                            licznik+=1
                        if tab2[x-1][y] == True:
                            licznik+=1
                        if tab2[x-1][y+1] == True:
                            licznik+=1
                        if tab2[x][y+1] == True:
                            licznik+=1
                            
                    zliczona[x][y]=licznik

        for x in range(-1, 40):
            for y in range(-1, 40):
                if tab2[x][y] == False:
                    if zliczona[x][y] == 3:
                        tab[x][y] = True
                    else:
                        tab[x][y] = False
                if tab2[x][y] == True:
                    if zliczona[x][y] == 2 or zliczona[x][y] == 3:
                        tab[x][y] = True
                    else:
                        tab[x][y] = False
            
                            
                        
    for x in range(-1, 40):
        for y in range(-1, 40):
            if tab[x][y] == True:
                pygame.draw.rect(plansza, WHITE, (x*20, y*20, 20, 20))

            else:
                pygame.draw.rect(plansza, BLACK, (x*20, y*20, 20, 20))
    
    
    for i in range(-1, 41):
        pygame.draw.line(plansza, WHITE, (i*20, 0), (i*20, 800), 1)
        pygame.draw.line(plansza, WHITE, (0, i*20), (800, i*20), 1)
                   
                        
                    
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN and lecimy == False:
            x, y = pygame.mouse.get_pos()
            x = int(x / 20)
            y = int(y / 20)
            tab[x][y] = True
        if event.type == KEYDOWN:
            if event.key == K_1:
                lecimy = True
            




    if lecimy==True:
        zegar.tick(FPS)
    else:
        zegar.tick(FPS1)
    pygame.display.update()
