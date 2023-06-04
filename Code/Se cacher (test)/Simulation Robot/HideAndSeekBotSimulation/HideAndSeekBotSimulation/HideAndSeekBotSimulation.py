# -*- coding: utf-8 -*-
import pygame
import random
from pygame.locals import *
from random import randint
pygame.init()

#variables
largeur_fenetre = 1000
hauteur_fenetre = 1000

window = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
window = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
clock = pygame.time.Clock()

pygame.display.set_caption("HideAndSeekBotSimulation")

bot_x = 500 # Position initiale du robot (au centre de la fen�tre)
bot_y = 500

bot_dir = random.choice(['up', 'down', 'left', 'right','up-left','up-right','down-left','down-right'])
#bot_dir = 'up' 
old_captor = ''
last_bot_dir = ''
wall_encountered = 0  # Compteur de murs rencontr�s
wall_expected = random.randint(1, 4)  # Nombre de murs n�cessaires pour se cacher
find_angle = False  # Indicateur pour le mode "cherche un coin"

mov = 20
wall_thickness = 20
wall_target = ''
border_north = pygame.Rect(0, 0,largeur_fenetre, wall_thickness)
border_north_c = pygame.Rect(wall_thickness, wall_thickness,largeur_fenetre - 2*wall_thickness, wall_thickness)
border_south = pygame.Rect(0, hauteur_fenetre - wall_thickness,largeur_fenetre, wall_thickness)
border_west = pygame.Rect(0, 0, wall_thickness, hauteur_fenetre)
border_west_c = pygame.Rect(wall_thickness,wall_thickness, wall_thickness, hauteur_fenetre -2*wall_thickness)
border_east = pygame.Rect(largeur_fenetre - wall_thickness, 0, wall_thickness, hauteur_fenetre)
#variables murs
COORD_X_WALL1 = 200
COORD_Y_WALL1 = 300
DIR_WALL1 = randint(0, 3) 
COORD_X_WALL2 = 600
COORD_Y_WALL2 = 300
DIR_WALL2 = randint(0, 3)  

COORD_X_WALL3 = 200
COORD_Y_WALL3 = 800
DIR_WALL3 = randint(0, 3)  

COORD_X_WALL4 = 600
COORD_Y_WALL4 = 800
DIR_WALL4 = randint(0, 3)  

OBSTACLE_1 = [COORD_X_WALL1, COORD_Y_WALL1, DIR_WALL1]
OBSTACLE_2 = [COORD_X_WALL2, COORD_Y_WALL2, DIR_WALL2]
OBSTACLE_3 = [COORD_X_WALL3, COORD_Y_WALL3, DIR_WALL3]
OBSTACLE_4 = [COORD_X_WALL4, COORD_Y_WALL4, DIR_WALL4]

h_obstacle_1 = pygame.Rect(OBSTACLE_1[0], OBSTACLE_1[1], 200, wall_thickness)
h_obstacle_2 = pygame.Rect(OBSTACLE_2[0], OBSTACLE_2[1], 200, wall_thickness)
h_obstacle_3 = pygame.Rect(OBSTACLE_3[0], OBSTACLE_3[1], 200, wall_thickness)
h_obstacle_4 = pygame.Rect(OBSTACLE_4[0], OBSTACLE_4[1], 200, wall_thickness)

isFindingWall = True
find_collision = False
find_angle = False
find_first_wall= False
isHidden = False
captorUp = False
captorLeft = False
captorRight = False
captorDown = False
turned = False


    

def generate_labyrinth():
    

# Dessin de la bordure
    pygame.draw.rect(window, (255, 255, 255), border_north)
    pygame.draw.rect(window, (255, 255, 255), border_south)
    pygame.draw.rect(window, (255, 255, 255), border_east)
    pygame.draw.rect(window, (255, 255, 255), border_west)

# Coordonn�es des murs
    

#initialisation des rectangle horizontaux
    


#Determination de la position des murs verticaux
    if OBSTACLE_1[2] == 0:
        v_obstacle_1 = pygame.Rect(OBSTACLE_1[0], OBSTACLE_1[1] - 180, wall_thickness, 200)
    elif OBSTACLE_1[2] == 1:
        v_obstacle_1 = pygame.Rect(OBSTACLE_1[0] + 200-wall_thickness, OBSTACLE_1[1] - 200+wall_thickness, wall_thickness, 200)
    elif OBSTACLE_1[2] == 2:
        v_obstacle_1 = pygame.Rect(OBSTACLE_1[0], OBSTACLE_1[1], wall_thickness, 200)
    else:
        v_obstacle_1 = pygame.Rect(OBSTACLE_1[0] + 200-wall_thickness, OBSTACLE_1[1],wall_thickness, 200)


    if OBSTACLE_2[2] == 0:
        v_obstacle_2 = pygame.Rect(OBSTACLE_2[0], OBSTACLE_2[1] - 200 +wall_thickness, wall_thickness, 200)
    elif OBSTACLE_2[2] == 1:
        v_obstacle_2 = pygame.Rect(OBSTACLE_2[0] + 200-wall_thickness, OBSTACLE_2[1] - 200+wall_thickness, wall_thickness, 200)
    elif OBSTACLE_2[2] == 2:
        v_obstacle_2 = pygame.Rect(OBSTACLE_2[0], OBSTACLE_2[1], wall_thickness, 200)
    else:
        v_obstacle_2 = pygame.Rect(OBSTACLE_2[0] + 200-wall_thickness, OBSTACLE_2[1], wall_thickness, 200)


    if OBSTACLE_3[2] == 0:
        v_obstacle_3 = pygame.Rect(OBSTACLE_3[0], OBSTACLE_3[1] - 200+wall_thickness, wall_thickness, 200)
    elif OBSTACLE_3[2] == 1:
        v_obstacle_3 = pygame.Rect(OBSTACLE_3[0] + 180, OBSTACLE_3[1] - 200+wall_thickness, wall_thickness, 200)
    elif OBSTACLE_3[2] == 2:
        v_obstacle_3 = pygame.Rect(OBSTACLE_3[0], OBSTACLE_3[1], wall_thickness, 200)
    else:
        v_obstacle_3 = pygame.Rect(OBSTACLE_3[0] + 200-wall_thickness, OBSTACLE_3[1],wall_thickness, 200)

    if OBSTACLE_4[2] == 0:
        v_obstacle_4 = pygame.Rect(OBSTACLE_4[0], OBSTACLE_4[1] - 200+wall_thickness, wall_thickness, 200)
    elif OBSTACLE_4[2] == 1:
        v_obstacle_4 = pygame.Rect(OBSTACLE_4[0] + 200-wall_thickness, OBSTACLE_4[1] - 200+wall_thickness, wall_thickness, 200)
    elif OBSTACLE_4[2] == 2:
        v_obstacle_4 = pygame.Rect(OBSTACLE_4[0], OBSTACLE_4[1], wall_thickness, 200)
    else:
        v_obstacle_4 = pygame.Rect(OBSTACLE_4[0] + 200-wall_thickness, OBSTACLE_4[1],wall_thickness, 200)
    

    pygame.draw.rect(window, (255, 255, 255), h_obstacle_1)
    pygame.draw.rect(window, (255, 255, 255), v_obstacle_1)

    pygame.draw.rect(window, (255, 255, 255), h_obstacle_2)
    pygame.draw.rect(window, (255, 255, 255), v_obstacle_2)

    pygame.draw.rect(window, (255, 255, 255), h_obstacle_3)
    pygame.draw.rect(window, (255, 255, 255), v_obstacle_3)

    pygame.draw.rect(window, (255, 255, 255), h_obstacle_4)
    pygame.draw.rect(window, (255, 255, 255), v_obstacle_4)  
    return (v_obstacle_1,v_obstacle_2,v_obstacle_3,v_obstacle_4)

# Cr�ation de la bordure du jeu
(v_obstacle_1,v_obstacle_2,v_obstacle_3,v_obstacle_4) = generate_labyrinth()
direction = randint(0,1)

#boucle principale
running = True
while running:
    def DrawGame():
            
            clock.tick(100)
            window.fill((0,0,0))
            generate_labyrinth()
            pygame.draw.circle(window, (255, 0, 150), (bot_x, bot_y), 20)  
            if bot_dir == 'up' or \
                bot_dir == 'up-left' or \
                bot_dir == 'up-right':
                pygame.draw.rect(window,(50,255,50), US_up)
                pygame.draw.rect(window,(50,255,50), US_left)
                #pygame.draw.rect(window,(50,255,50), US_down)
                pygame.draw.rect(window,(50,255,50), US_right)
            if bot_dir == 'left':
                pygame.draw.rect(window,(50,255,50), US_up)
                pygame.draw.rect(window,(50,255,50), US_left)
                pygame.draw.rect(window,(50,255,50), US_down)
                #pygame.draw.rect(window,(50,255,50), US_right)
            if bot_dir == 'down' or \
            bot_dir == 'down-left' or \
            bot_dir == 'down-right':
                #pygame.draw.rect(window,(50,255,50), US_up)
                pygame.draw.rect(window,(50,255,50), US_left)
                pygame.draw.rect(window,(50,255,50), US_down)
                pygame.draw.rect(window,(50,255,50), US_right)
            if bot_dir == 'right':
                pygame.draw.rect(window,(50,255,50), US_up)
                #pygame.draw.rect(window,(50,255,50), US_left)
                pygame.draw.rect(window,(50,255,50), US_down)
                pygame.draw.rect(window,(50,255,50), US_right)
            if isHidden:
                text_color = (255, 255, 255)
                font = pygame.font.Font(None, 36)
                text_surface = font.render("cache !", True, text_color)
                text_x = (largeur_fenetre - text_surface.get_width()) // 2
                text_y = (hauteur_fenetre - text_surface.get_height()) // 2
                window.blit(text_surface, (text_x, text_y))

            pygame.display.flip()

   

    while find_angle:
        print("boucle find angle")
        US_up = pygame.Rect(bot_x -8 ,bot_y - 30, 15,10)
        US_down = pygame.Rect(bot_x - 8,bot_y +20, 15,10)
        US_left = pygame.Rect(bot_x - 30,bot_y - 8, 10,15)
        US_right = pygame.Rect(bot_x + 20,bot_y -8 ,10,15)  

        while captorUp : 
            US_up = pygame.Rect(bot_x -8 ,bot_y - 30, 15,10)
            US_down = pygame.Rect(bot_x - 8,bot_y +20, 15,10)
            US_left = pygame.Rect(bot_x - 30,bot_y - 8, 10,15)
            US_right = pygame.Rect(bot_x + 20,bot_y -8 ,10,15)  
            print("boucle US_up")
            if turned == True:
                if bot_dir == 'left' :
                    bot_x-=1
                    bot_dir = 'left'
                    if US_up.colliderect(h_obstacle_1) == True or \
                    US_up.colliderect(h_obstacle_2) == True or \
                    US_up.colliderect(h_obstacle_3) == True or \
                    US_up.colliderect(h_obstacle_3)== True or \
                    US_up.colliderect(h_obstacle_4)== True or \
                    US_up.colliderect(v_obstacle_1) == True or \
                    US_up.colliderect(v_obstacle_2) == True or \
                    US_up.colliderect(v_obstacle_3) == True or \
                    US_up.colliderect(v_obstacle_3)== True or \
                    US_up.colliderect(v_obstacle_4)== True or \
                    US_up.colliderect(border_north)== True:
                        print("Le capteur UP detecte un mur")
                    else:
                        bot_dir = 'up'
                        captorUp = False                    
                        bot_y -= mov
                        bot_x -=mov
                        DrawGame()
                        last_bot_dir = 'left'
                        wall_target = 'right'
                        find_collision = True
                        find_angle = False
                        old_captor = 'up'
                    
                        break
                elif bot_dir == 'right':                    
                    bot_x +=1
                    bot_dir = 'right'
                    if US_up.colliderect(h_obstacle_1) == True or \
                    US_up.colliderect(h_obstacle_2) == True or \
                    US_up.colliderect(h_obstacle_3) == True or \
                    US_up.colliderect(h_obstacle_3)== True or \
                    US_up.colliderect(h_obstacle_4)== True or \
                    US_up.colliderect(v_obstacle_1) == True or \
                    US_up.colliderect(v_obstacle_2) == True or \
                    US_up.colliderect(v_obstacle_3) == True or \
                    US_up.colliderect(v_obstacle_3)== True or \
                    US_up.colliderect(v_obstacle_4)== True or \
                    US_up.colliderect(border_north)== True:
                        print("Le capteur UP detecte un mur")
                    else:
                        bot_dir = 'up'
                        captorUp = False
                        bot_y -=mov
                        bot_x +=mov
                        DrawGame()
                        last_bot_dir = 'right'
                        wall_target = 'left'
                        find_collision = True
                        find_angle = False
                        old_captor = 'up'
                    
                        break
                DrawGame()
            elif direction == 1:
                bot_x +=1
                bot_dir = 'right'
                if US_up.colliderect(h_obstacle_1) == True or \
                US_up.colliderect(h_obstacle_2) == True or \
                US_up.colliderect(h_obstacle_3) == True or \
                US_up.colliderect(h_obstacle_3)== True or \
                US_up.colliderect(h_obstacle_4)== True or \
                US_up.colliderect(v_obstacle_1) == True or \
                US_up.colliderect(v_obstacle_2) == True or \
                US_up.colliderect(v_obstacle_3) == True or \
                US_up.colliderect(v_obstacle_3)== True or \
                US_up.colliderect(v_obstacle_4)== True or \
                US_up.colliderect(border_north)== True:
                    print("Le capteur UP detecte un mur")
                else:
                    bot_dir = 'up'
                    captorUp = False
                    bot_y -=mov
                    bot_x +=mov
                    DrawGame()
                    last_bot_dir = 'right'
                    wall_target = 'left'
                    find_collision = True
                    find_angle = False
                    old_captor = 'up'
                    
                    break
            else:
                bot_x-=1
                bot_dir = 'left'
                if US_up.colliderect(h_obstacle_1) == True or \
                US_up.colliderect(h_obstacle_2) == True or \
                US_up.colliderect(h_obstacle_3) == True or \
                US_up.colliderect(h_obstacle_3)== True or \
                US_up.colliderect(h_obstacle_4)== True or \
                US_up.colliderect(v_obstacle_1) == True or \
                US_up.colliderect(v_obstacle_2) == True or \
                US_up.colliderect(v_obstacle_3) == True or \
                US_up.colliderect(v_obstacle_3)== True or \
                US_up.colliderect(v_obstacle_4)== True or \
                US_up.colliderect(border_north)== True:
                    print("Le capteur UP detecte un mur")
                else:
                    bot_dir = 'up'
                    captorUp = False                    
                    bot_y -= mov
                    bot_x -=mov
                    DrawGame()
                    last_bot_dir = 'left'
                    wall_target = 'right'
                    find_collision = True
                    find_angle = False
                    old_captor = 'up'
                    
                    break
                DrawGame()
            if US_left.colliderect(v_obstacle_1) or \
                US_left.colliderect(v_obstacle_2) or \
                US_left.colliderect(v_obstacle_3) or \
                US_left.colliderect(v_obstacle_4) or \
                US_left.colliderect(border_west) or\
                US_right.colliderect(v_obstacle_1) or \
                US_right.colliderect(v_obstacle_2) or \
                US_right.colliderect(v_obstacle_3) or \
                US_right.colliderect(v_obstacle_4) or \
                US_right.colliderect(border_east):
                isHidden = True;
                print("est cache")
                find_angle = False;
                while isHidden:
                    
                    DrawGame()
            DrawGame()

        while captorDown:    
            US_up = pygame.Rect(bot_x -8 ,bot_y - 30, 15,10)
            US_down = pygame.Rect(bot_x - 8,bot_y +20, 15,10)
            US_left = pygame.Rect(bot_x - 30,bot_y - 8, 10,15)
            US_right = pygame.Rect(bot_x + 20,bot_y -8 ,10,15)  
            if turned == True:
                if bot_dir == 'left' :
                    bot_x-=1
                    bot_dir = 'left'
                    DrawGame()
                    if US_down.colliderect(h_obstacle_1) == True or \
                    US_down.colliderect(h_obstacle_2) == True or \
                    US_down.colliderect(h_obstacle_3) == True or \
                    US_down.colliderect(h_obstacle_3)== True or \
                    US_down.colliderect(h_obstacle_4)== True or \
                    US_down.colliderect(v_obstacle_1) == True or \
                    US_down.colliderect(v_obstacle_2) == True or \
                    US_down.colliderect(v_obstacle_3) == True or \
                    US_down.colliderect(v_obstacle_3)== True or \
                    US_down.colliderect(v_obstacle_4)== True or \
                    US_down.colliderect(border_south)== True:
                        print("Le capteur DOWN detecte un mur")
                    else :
                        bot_dir = 'down'
                        bot_y +=mov
                        bot_x -= mov
                        DrawGame()
                        captorDown = False
                        last_bot_dir = 'left'
                        wall_target = 'right'
                        find_collision = True
                        find_angle = False
                        old_captor = 'down'
                    
                        break
                elif bot_dir == 'right':
                    bot_x +=1
                    bot_dir = 'right'
                    DrawGame()
                    if US_down.colliderect(h_obstacle_1) == True or \
                    US_down.colliderect(h_obstacle_2) == True or \
                    US_down.colliderect(h_obstacle_3) == True or \
                    US_down.colliderect(h_obstacle_3)== True or \
                    US_down.colliderect(h_obstacle_4)== True or \
                    US_down.colliderect(v_obstacle_1) == True or \
                    US_down.colliderect(v_obstacle_2) == True or \
                    US_down.colliderect(v_obstacle_3) == True or \
                    US_down.colliderect(v_obstacle_3)== True or \
                    US_down.colliderect(v_obstacle_4)== True or \
                    US_down.colliderect(border_south)== True:
                        print("Le capteur DOWN detecte un mur")
                    else:
                        bot_dir = 'down'
                        bot_y +=mov
                        bot_x +=mov
                        DrawGame()
                        captorDown = False
                        last_bot_dir = 'right'
                        wall_target = 'left'
                        find_collision = True
                        find_angle = False
                        old_captor = 'down'
                    
                        break
                DrawGame()
                if US_down.colliderect(h_obstacle_1) == True or \
                US_down.colliderect(h_obstacle_2) == True or \
                US_down.colliderect(h_obstacle_3) == True or \
                US_down.colliderect(h_obstacle_3)== True or \
                US_down.colliderect(h_obstacle_4)== True or \
                US_down.colliderect(v_obstacle_1) == True or \
                US_down.colliderect(v_obstacle_2) == True or \
                US_down.colliderect(v_obstacle_3) == True or \
                US_down.colliderect(v_obstacle_3)== True or \
                US_down.colliderect(v_obstacle_4)== True or \
                US_down.colliderect(border_south)== True:
                    print("Le capteur DOWN detecte un mur")
            elif direction == 1:
                bot_x +=1
                bot_dir = 'right'
                if US_down.colliderect(h_obstacle_1) == True or \
                US_down.colliderect(h_obstacle_2) == True or \
                US_down.colliderect(h_obstacle_3) == True or \
                US_down.colliderect(h_obstacle_3)== True or \
                US_down.colliderect(h_obstacle_4)== True or \
                US_down.colliderect(v_obstacle_1) == True or \
                US_down.colliderect(v_obstacle_2) == True or \
                US_down.colliderect(v_obstacle_3) == True or \
                US_down.colliderect(v_obstacle_3)== True or \
                US_down.colliderect(v_obstacle_4)== True or \
                US_down.colliderect(border_south)== True:
                    print("Le capteur DOWN detecte un mur")
                else:
                    bot_dir = 'down'
                    bot_y +=mov
                    bot_x +=mov
                    DrawGame()
                    captorDown = False
                    last_bot_dir = 'right'
                    wall_target = 'left'
                    find_collision = True
                    find_angle = False
                    old_captor = 'down'
                    
                    break
            else:
                bot_x-=1
                bot_dir = 'left'
                if US_down.colliderect(h_obstacle_1) == True or \
                US_down.colliderect(h_obstacle_2) == True or \
                US_down.colliderect(h_obstacle_3) == True or \
                US_down.colliderect(h_obstacle_3)== True or \
                US_down.colliderect(h_obstacle_4)== True or \
                US_down.colliderect(v_obstacle_1) == True or \
                US_down.colliderect(v_obstacle_2) == True or \
                US_down.colliderect(v_obstacle_3) == True or \
                US_down.colliderect(v_obstacle_3)== True or \
                US_down.colliderect(v_obstacle_4)== True or \
                US_down.colliderect(border_south)== True:
                    print("Le capteur DOWN detecte un mur")
                else :
                    bot_dir = 'down'
                    bot_y +=mov
                    bot_x -= mov
                    DrawGame()
                    captorDown = False
                    last_bot_dir = 'left'
                    wall_target = 'right'
                    find_collision = True
                    find_angle = False
                    old_captor = 'down'
                    
                    break
            if US_left.colliderect(v_obstacle_1) or \
                US_left.colliderect(v_obstacle_2) or \
                US_left.colliderect(v_obstacle_3) or \
                US_left.colliderect(v_obstacle_4) or \
                US_left.colliderect(border_west) or\
                US_right.colliderect(v_obstacle_1) or \
                US_right.colliderect(v_obstacle_2) or \
                US_right.colliderect(v_obstacle_3) or \
                US_right.colliderect(v_obstacle_4) or \
                US_right.colliderect(border_east):
                isHidden = True;
                print("est cache")
                find_angle = False;
                while isHidden:
                    
                    DrawGame()
            DrawGame()
            

        while captorLeft: 
            US_up = pygame.Rect(bot_x -8 ,bot_y - 30, 15,10)
            US_down = pygame.Rect(bot_x - 8,bot_y +20, 15,10)
            US_left = pygame.Rect(bot_x - 30,bot_y - 8, 10,15)
            US_right = pygame.Rect(bot_x + 20,bot_y -8 ,10,15)  
            if turned == True:
                if bot_dir == 'up' :
                    bot_y-=1
                    bot_dir = 'up'
                    if US_left.colliderect(v_obstacle_1) == True or \
                    US_left.colliderect(v_obstacle_2) == True or \
                    US_left.colliderect(v_obstacle_3) == True or \
                    US_left.colliderect(v_obstacle_3)== True or \
                    US_left.colliderect(v_obstacle_4)== True or \
                    US_left.colliderect(h_obstacle_1) == True or \
                    US_left.colliderect(h_obstacle_2) == True or \
                    US_left.colliderect(h_obstacle_3) == True or \
                    US_left.colliderect(h_obstacle_3)== True or \
                    US_left.colliderect(h_obstacle_4)== True or \
                    US_left.colliderect(border_west)== True:
                        print("Le capteur LEFT detecte un mur")
                        DrawGame()
                    else: 
                        bot_dir = 'left'
                        bot_x -=mov
                        bot_y -=mov
                        DrawGame()
                        captorLeft = False
                        last_bot_dir = 'up'
                        wall_target = 'down'
                        find_collision = True
                        find_angle = False
                        old_captor = 'left'
                    
                    break
                elif bot_dir == 'down':
                    bot_y +=1
                    bot_dir = 'down'
                    if US_left.colliderect(v_obstacle_1) == True or \
                    US_left.colliderect(v_obstacle_2) == True or \
                    US_left.colliderect(v_obstacle_3) == True or \
                    US_left.colliderect(v_obstacle_3)== True or \
                    US_left.colliderect(v_obstacle_4)== True or \
                    US_left.colliderect(h_obstacle_1) == True or \
                    US_left.colliderect(h_obstacle_2) == True or \
                    US_left.colliderect(h_obstacle_3) == True or \
                    US_left.colliderect(h_obstacle_3)== True or \
                    US_left.colliderect(h_obstacle_4)== True or \
                    US_left.colliderect(border_west)== True:
                        print("Le capteur LEFT detecte un mur")
                    else:
                        bot_dir = 'left'
                        bot_x -=mov
                        bot_y +=mov
                        DrawGame()
                        captorLeft = False
                        last_bot_dir = 'down'
                        wall_target = 'up'
                        find_collision = True
                        find_angle = False
                        old_captor = 'left'
                    
                        break
                DrawGame()
            elif direction == 0:
                bot_y +=1
                bot_dir = 'down'
                if US_left.colliderect(v_obstacle_1) == True or \
                US_left.colliderect(v_obstacle_2) == True or \
                US_left.colliderect(v_obstacle_3) == True or \
                US_left.colliderect(v_obstacle_3)== True or \
                US_left.colliderect(v_obstacle_4)== True or \
                US_left.colliderect(h_obstacle_1) == True or \
                US_left.colliderect(h_obstacle_2) == True or \
                US_left.colliderect(h_obstacle_3) == True or \
                US_left.colliderect(h_obstacle_3)== True or \
                US_left.colliderect(h_obstacle_4)== True or \
                US_left.colliderect(border_west)== True:
                    print("Le capteur LEFT detecte un mur")
                else:
                    bot_dir = 'left'
                    bot_x -=mov
                    bot_y +=mov
                    DrawGame()
                    captorLeft = False
                    last_bot_dir = 'down'
                    wall_target = 'up'
                    find_collision = True
                    find_angle = False
                    old_captor = 'left'
                    
                    break
            else:
                bot_y-=1
                bot_dir = 'up'
                if US_left.colliderect(v_obstacle_1) == True or \
                US_left.colliderect(v_obstacle_2) == True or \
                US_left.colliderect(v_obstacle_3) == True or \
                US_left.colliderect(v_obstacle_3)== True or \
                US_left.colliderect(v_obstacle_4)== True or \
                US_left.colliderect(h_obstacle_1) == True or \
                US_left.colliderect(h_obstacle_2) == True or \
                US_left.colliderect(h_obstacle_3) == True or \
                US_left.colliderect(h_obstacle_3)== True or \
                US_left.colliderect(h_obstacle_4)== True or \
                US_left.colliderect(border_west)== True:
                    print("Le capteur LEFT detecte un mur")              
                else: 
                    bot_dir = 'left'
                    bot_x -=mov
                    bot_y -=mov
                    DrawGame()
                    captorLeft = False
                    last_bot_dir = 'up'
                    wall_target = 'down'
                    find_collision = True
                    find_angle = False
                    old_captor = 'left'
                    
                    break
            if US_up.colliderect(h_obstacle_1) or \
                US_up.colliderect(h_obstacle_2) or \
                US_up.colliderect(h_obstacle_3) or \
                US_up.colliderect(h_obstacle_4) or \
                US_up.colliderect(border_north) or\
                US_down.colliderect(h_obstacle_1) or \
                US_down.colliderect(h_obstacle_2) or \
                US_down.colliderect(h_obstacle_3) or \
                US_down.colliderect(h_obstacle_4) or \
                US_down.colliderect(border_south):
                isHidden = True;
                print("est cache")
                find_angle = False;
                while isHidden:
                   
                    DrawGame()
            DrawGame()
            

        while captorRight: 
            US_up = pygame.Rect(bot_x -8 ,bot_y - 30, 15,10)
            US_down = pygame.Rect(bot_x - 8,bot_y +20, 15,10)
            US_left = pygame.Rect(bot_x - 30,bot_y - 8, 10,15)
            US_right = pygame.Rect(bot_x + 20,bot_y -8 ,10,15)  
            if turned == True:
                if bot_dir == 'up' :
                    bot_dir = 'up'
                    bot_y -=1
                    if US_right.colliderect(v_obstacle_1) == True or \
                    US_right.colliderect(v_obstacle_2) == True or \
                    US_right.colliderect(v_obstacle_3) == True or \
                    US_right.colliderect(v_obstacle_3)== True or \
                    US_right.colliderect(v_obstacle_4)== True or \
                    US_right.colliderect(h_obstacle_1) == True or \
                    US_right.colliderect(h_obstacle_2) == True or \
                    US_right.colliderect(h_obstacle_3) == True or \
                    US_right.colliderect(h_obstacle_3)== True or \
                    US_right.colliderect(h_obstacle_4)== True or \
                    US_right.colliderect(border_east)== True:
                        print("Le capteur RIGHT detecte un mur")
                        DrawGame()
                    else:
                        bot_dir = 'right'
                        bot_x +=mov
                        bot_y -=mov
                        DrawGame()
                        captorRight = False
                        last_bot_dir = 'up'
                        wall_target = 'down'
                        find_collision = True
                        find_angle = False
                        old_captor = 'right'
                    
                        break
                elif bot_dir == 'down':
                    bot_dir = 'down'
                    bot_y +=1
                    if US_right.colliderect(v_obstacle_1) == True or \
                    US_right.colliderect(v_obstacle_2) == True or \
                    US_right.colliderect(v_obstacle_3) == True or \
                    US_right.colliderect(v_obstacle_3)== True or \
                    US_right.colliderect(v_obstacle_4)== True or \
                    US_right.colliderect(h_obstacle_1) == True or \
                    US_right.colliderect(h_obstacle_2) == True or \
                    US_right.colliderect(h_obstacle_3) == True or \
                    US_right.colliderect(h_obstacle_3)== True or \
                    US_right.colliderect(h_obstacle_4)== True or \
                    US_right.colliderect(border_east)== True:
                        print("Le capteur RIGHT detecte un mur")
                        DrawGame()
                    else:
                        bot_dir = 'right'
                        bot_x +=mov
                        bot_y +=mov
                        DrawGame()
                        captorRight = False
                        last_bot_dir = 'down'
                        wall_target = 'up'
                        find_collision = True
                        find_angle = False
                        old_captor = 'right'

                        break
                DrawGame()
            elif direction == 0:
                bot_dir = 'down'
                bot_y +=1
                if US_right.colliderect(v_obstacle_1) == True or \
                US_right.colliderect(v_obstacle_2) == True or \
                US_right.colliderect(v_obstacle_3) == True or \
                US_right.colliderect(v_obstacle_3)== True or \
                US_right.colliderect(v_obstacle_4)== True or \
                US_right.colliderect(h_obstacle_1) == True or \
                US_right.colliderect(h_obstacle_2) == True or \
                US_right.colliderect(h_obstacle_3) == True or \
                US_right.colliderect(h_obstacle_3)== True or \
                US_right.colliderect(h_obstacle_4)== True or \
                US_right.colliderect(border_east)== True:
                    print("Le capteur RIGHT detecte un mur")
                    DrawGame()
                else:
                    bot_dir = 'right'
                    bot_x +=mov
                    bot_y +=mov
                    DrawGame()
                    captorRight = False
                    last_bot_dir = 'down'
                    wall_target = 'up'
                    find_collision = True
                    find_angle = False
                    old_captor = 'right'

                    break
            else:
                bot_dir = 'up'
                bot_y -=1
                if US_right.colliderect(v_obstacle_1) == True or \
                US_right.colliderect(v_obstacle_2) == True or \
                US_right.colliderect(v_obstacle_3) == True or \
                US_right.colliderect(v_obstacle_3)== True or \
                US_right.colliderect(v_obstacle_4)== True or \
                US_right.colliderect(border_east)== True:
                    print("Le capteur RIGHT detecte un mur")
                    DrawGame()
                else:
                    bot_dir = 'right'
                    bot_x +=mov
                    bot_y -=mov
                    DrawGame()
                    captorRight = False
                    last_bot_dir = 'up'
                    wall_target = 'down'
                    find_collision = True
                    find_angle = False
                    old_captor = 'right'
                    
                    break
            if US_up.colliderect(h_obstacle_1) or \
                US_up.colliderect(h_obstacle_2) or \
                US_up.colliderect(h_obstacle_3) or \
                US_up.colliderect(h_obstacle_4) or \
                US_up.colliderect(border_north) or\
                US_down.colliderect(h_obstacle_1) or \
                US_down.colliderect(h_obstacle_2) or \
                US_down.colliderect(h_obstacle_3) or \
                US_down.colliderect(h_obstacle_4) or \
                US_down.colliderect(border_south):
                isHidden = True;
                print("est cache")
                find_angle = False;
                while isHidden:
                    
                    DrawGame()
            DrawGame()



    while find_collision:
        print("boucle collision")
        US_up = pygame.Rect(bot_x -8 ,bot_y - 30, 15,10)
        US_down = pygame.Rect(bot_x - 8,bot_y +20, 15,10)
        US_left = pygame.Rect(bot_x - 30,bot_y - 8, 10,15)
        US_right = pygame.Rect(bot_x + 20,bot_y -8 ,10,15) 
        
        if find_first_wall == False:
            if US_up.colliderect(h_obstacle_1) or \
            US_up.colliderect(h_obstacle_2) or \
            US_up.colliderect(h_obstacle_3) or \
            US_up.colliderect(h_obstacle_4) or \
            US_up.colliderect(v_obstacle_1) or \
            US_up.colliderect(v_obstacle_2) or \
            US_up.colliderect(v_obstacle_3) or \
            US_up.colliderect(v_obstacle_4) or \
            US_up.colliderect(border_north):
                find_collision = False
                bot_y -= 2
                find_angle = True
                find_first_wall = True
                captorUp = True
            elif US_down.colliderect(h_obstacle_1) or \
                US_down.colliderect(h_obstacle_2) or \
                US_down.colliderect(h_obstacle_3) or \
                US_down.colliderect(h_obstacle_4) or \
                US_down.colliderect(v_obstacle_1) or \
                US_down.colliderect(v_obstacle_2) or \
                US_down.colliderect(v_obstacle_3) or \
                US_down.colliderect(v_obstacle_4) or \
                US_down.colliderect(border_south):
                find_collision = False
                bot_y += 2
                find_angle = True
                find_first_wall = True
                captorDown = True
            elif US_left.colliderect(v_obstacle_1) or \
                US_left.colliderect(v_obstacle_2) or \
                US_left.colliderect(v_obstacle_3) or \
                US_left.colliderect(v_obstacle_4) or \
                US_left.colliderect(h_obstacle_1) or \
                US_left.colliderect(h_obstacle_2) or \
                US_left.colliderect(h_obstacle_3) or \
                US_left.colliderect(h_obstacle_4) or \
                US_left.colliderect(border_west):
                find_collision = False
                bot_x -=2
                find_first_wall = True
                find_angle = True
                captorLeft = True
            elif US_right.colliderect(v_obstacle_1) or \
                US_right.colliderect(v_obstacle_2) or \
                US_right.colliderect(v_obstacle_3) or \
                US_right.colliderect(v_obstacle_4) or \
                US_right.colliderect(h_obstacle_1) or \
                US_right.colliderect(h_obstacle_2) or \
                US_right.colliderect(h_obstacle_3) or \
                US_right.colliderect(h_obstacle_4) or \
                US_right.colliderect(border_east):
                find_collision = False
                find_first_wall = True
                bot_x += 2
                find_angle = True      
                captorRight = True

            if last_bot_dir == 'left' or \
                last_bot_dir == 'down-left' or\
                last_bot_dir == 'up-left' :
                bot_x -=1
                bot_dir = 'left'
            elif last_bot_dir == 'right' or \
                last_bot_dir == 'down-right' or\
                last_bot_dir == 'up-right' :
                bot_x += 1
                bot_dir = 'right'
            elif last_bot_dir == 'up':
                bot_y -=1
                bot_dir = 'up'
            elif last_bot_dir == 'down':
                bot_y +=1
                bot_dir = 'down'
            DrawGame()
        else:

            if US_up.colliderect(h_obstacle_1) or \
            US_up.colliderect(h_obstacle_2) or \
            US_up.colliderect(h_obstacle_3) or \
            US_up.colliderect(h_obstacle_4) or \
            US_up.colliderect(v_obstacle_1) or \
            US_up.colliderect(v_obstacle_2) or \
            US_up.colliderect(v_obstacle_3) or \
            US_up.colliderect(v_obstacle_4) or \
            US_up.colliderect(border_north):
                find_collision = False
                bot_y -= 2
                find_angle = True
                find_first_wall = True
                captorUp = True
                if last_bot_dir == 'down' and\
                    old_captor == 'right':
                    bot_dir = 'right'   
                elif last_bot_dir == 'down' and\
                    old_captor == 'left':
                    bot_dir = 'left'
            elif US_down.colliderect(h_obstacle_1) or \
                US_down.colliderect(h_obstacle_2) or \
                US_down.colliderect(h_obstacle_3) or \
                US_down.colliderect(h_obstacle_4) or \
                US_down.colliderect(v_obstacle_1) or \
                US_down.colliderect(v_obstacle_2) or \
                US_down.colliderect(v_obstacle_3) or \
                US_down.colliderect(v_obstacle_4) or \
                US_down.colliderect(border_south):
                find_collision = False
                bot_y += 2
                find_angle = True
                
                captorDown = True
                if last_bot_dir == 'up' and\
                    old_captor == 'left':
                    bot_dir = 'left'   
                elif last_bot_dir == 'down' and\
                    old_captor == 'left':
                    bot_dir = 'left'
            elif US_left.colliderect(v_obstacle_1) or \
                US_left.colliderect(v_obstacle_2) or \
                US_left.colliderect(v_obstacle_3) or \
                US_left.colliderect(v_obstacle_4) or \
                US_left.colliderect(h_obstacle_1) or \
                US_left.colliderect(h_obstacle_2) or \
                US_left.colliderect(h_obstacle_3) or \
                US_left.colliderect(h_obstacle_4) or \
                US_left.colliderect(border_west):
                find_collision = False
                bot_x -=2
                find_angle = True
                find_first_wall = True
                captorLeft = True
                if last_bot_dir == 'right' and\
                    old_captor == 'up':
                    bot_dir = 'up'   
                elif last_bot_dir == 'right' and\
                    old_captor == 'down':
                    bot_dir = 'down'
            elif US_right.colliderect(v_obstacle_1) or \
                US_right.colliderect(v_obstacle_2) or \
                US_right.colliderect(v_obstacle_3) or \
                US_right.colliderect(v_obstacle_4) or \
                US_right.colliderect(h_obstacle_1) or \
                US_right.colliderect(h_obstacle_2) or \
                US_right.colliderect(h_obstacle_3) or \
                US_right.colliderect(h_obstacle_4) or \
                US_right.colliderect(border_east):
                find_collision = False
                bot_x += 2
                find_angle = True
                find_first_wall = True
                captorRight = True
                if last_bot_dir == 'left' and\
                    old_captor == 'up':
                    bot_dir = 'up'   
                if last_bot_dir == 'left' and\
                    old_captor == 'down':
                    bot_dir = 'down' 

            if wall_target == 'left':
                bot_x -=1                
            elif wall_target == 'right':
                bot_x += 1
            elif wall_target == 'up':
                bot_y -=1               
            elif wall_target == 'down':
                bot_y +=1  
            turned = True
            DrawGame()




    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 


    while isFindingWall :
        US_up = pygame.Rect(bot_x -8 ,bot_y - 30, 15,10)
        US_down = pygame.Rect(bot_x - 8,bot_y +20, 15,10)
        US_left = pygame.Rect(bot_x - 30,bot_y - 8, 10,15)
        US_right = pygame.Rect(bot_x + 20,bot_y -8 ,10,15)  
        print("findinwall")
        
        if bot_dir == 'up':
            bot_y -= 1
        elif bot_dir == 'down':
             bot_y += 1
        elif bot_dir == 'left':
             bot_x -= 1
        elif bot_dir == 'right':
             bot_x += 1
        elif bot_dir == 'up-left':
             bot_x -=1
             bot_y -=1
        elif bot_dir == 'up-right':
             bot_x += 1
             bot_y -= 1
        elif bot_dir == 'down-left':
             bot_x -= 1
             bot_y +=1
        elif bot_dir == 'down-right':
             bot_x += 1
             bot_y += 1
            
        if US_up.colliderect(h_obstacle_1) or \
            US_up.colliderect(h_obstacle_2) or \
            US_up.colliderect(h_obstacle_3) or \
            US_up.colliderect(h_obstacle_4) or \
            US_up.colliderect(border_north):
            wall_encountered += 1
            if wall_encountered == wall_expected - 1 :
                 directions_possibles = [ 'down', 'left', 'right']
            else :
                 directions_possibles = [ 'down', 'left', 'right','down-left','down-right']
            last_bot_dir = bot_dir;
            bot_dir = random.choice(directions_possibles)
            bot_y += 5
             

        if US_down.colliderect(h_obstacle_1) or \
            US_down.colliderect(h_obstacle_2) or \
            US_down.colliderect(h_obstacle_3) or \
            US_down.colliderect(h_obstacle_4) or \
            US_down.colliderect(border_south):
            wall_encountered += 1
            if wall_encountered == wall_expected - 1 :
                directions_possibles = ['up', 'left', 'right']
            else :
                directions_possibles = ['up', 'left', 'right','up-left','up-right']
            last_bot_dir = bot_dir;
            bot_dir = random.choice(directions_possibles)
            bot_y -= 5
            

        if US_left.colliderect(v_obstacle_1) or \
            US_left.colliderect(v_obstacle_2) or \
            US_left.colliderect(v_obstacle_3) or \
            US_left.colliderect(v_obstacle_4) or \
            US_left.colliderect(border_west):
            wall_encountered += 1
            if wall_encountered == wall_expected - 1 :
                directions_possibles = ['up', 'down', 'right']
            else:
                directions_possibles = ['up', 'down', 'right','up-right','down-right']
            last_bot_dir = bot_dir;
            bot_dir = random.choice(directions_possibles)
            bot_x += 5
            

        if US_right.colliderect(v_obstacle_1) or \
            US_right.colliderect(v_obstacle_2) or \
            US_right.colliderect(v_obstacle_3) or \
            US_right.colliderect(v_obstacle_4) or \
            US_right.colliderect(border_east):
            wall_encountered += 1
            if wall_encountered == wall_expected - 1 :
                directions_possibles = ['up', 'down', 'left']
            else :
                directions_possibles = ['up', 'down', 'left','up-left','down-left']
            last_bot_dir = bot_dir;
            bot_dir = random.choice(directions_possibles)
            bot_x -= 5
            

                # V�rifier si le robot a rencontr� suffisamment de murs pour se cacher
        if wall_encountered >= wall_expected:
             isFindingWall = False
             bot_dir = last_bot_dir
             find_collision = True  
        DrawGame()
        

        
        
    
    


pygame.quit()