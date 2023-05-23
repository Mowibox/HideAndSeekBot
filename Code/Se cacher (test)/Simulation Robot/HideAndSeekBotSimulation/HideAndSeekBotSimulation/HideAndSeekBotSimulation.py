import pygame
import random
from pygame.locals import *
from random import randint

largeur_fenetre = 1000
hauteur_fenetre = 1000

pygame.init()

window = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
clock = pygame.time.Clock()
pygame.display.set_caption("HideAndSeekBotSimulation")

# Création de la bordure du jeu
border_north = pygame.Rect(0, 0, largeur_fenetre, 20)
border_south = pygame.Rect(0, hauteur_fenetre - 20, largeur_fenetre, 20)
border_west = pygame.Rect(0, 0, 20, hauteur_fenetre)
border_east = pygame.Rect(largeur_fenetre - 20, 0, 20, hauteur_fenetre)

# Dessin de la bordure
pygame.draw.rect(window, (250, 250, 250), border_north)
pygame.draw.rect(window, (250, 250, 250), border_south)
pygame.draw.rect(window, (250, 250, 250), border_east)
pygame.draw.rect(window, (250, 250, 250), border_west)

# Coordonnées des murs
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

#initialisation des rectangle horizontaux
h_obstacle_1 = pygame.Rect(OBSTACLE_1[0], OBSTACLE_1[1], 200, 20)
h_obstacle_2 = pygame.Rect(OBSTACLE_2[0], OBSTACLE_2[1], 200, 20)
h_obstacle_3 = pygame.Rect(OBSTACLE_3[0], OBSTACLE_3[1], 200, 20)
h_obstacle_4 = pygame.Rect(OBSTACLE_4[0], OBSTACLE_4[1], 200, 20)


#Determination de la position des murs verticaux
if OBSTACLE_1[2] == 0:
    v_obstacle_1 = pygame.Rect(OBSTACLE_1[0], OBSTACLE_1[1] - 180, 20, 200)
elif OBSTACLE_1[2] == 1:
    v_obstacle_1 = pygame.Rect(OBSTACLE_1[0] + 180, OBSTACLE_1[1] - 180, 20, 200)
elif OBSTACLE_1[2] == 2:
    v_obstacle_1 = pygame.Rect(OBSTACLE_1[0], OBSTACLE_1[1], 20, 200)
else:
    v_obstacle_1 = pygame.Rect(OBSTACLE_1[0] + 180, OBSTACLE_1[1], 20, 200)


if OBSTACLE_2[2] == 0:
    v_obstacle_2 = pygame.Rect(OBSTACLE_2[0], OBSTACLE_2[1] - 180, 20, 200)
elif OBSTACLE_2[2] == 1:
    v_obstacle_2 = pygame.Rect(OBSTACLE_2[0] + 180, OBSTACLE_2[1] - 180, 20, 200)
elif OBSTACLE_2[2] == 2:
    v_obstacle_2 = pygame.Rect(OBSTACLE_2[0], OBSTACLE_2[1], 20, 200)
else:
    v_obstacle_2 = pygame.Rect(OBSTACLE_2[0] + 180, OBSTACLE_2[1], 20, 200)


if OBSTACLE_3[2] == 0:
    v_obstacle_3 = pygame.Rect(OBSTACLE_3[0], OBSTACLE_3[1] - 180, 20, 200)
elif OBSTACLE_3[2] == 1:
    v_obstacle_3 = pygame.Rect(OBSTACLE_3[0] + 180, OBSTACLE_3[1] - 180, 20, 200)
elif OBSTACLE_3[2] == 2:
    v_obstacle_3 = pygame.Rect(OBSTACLE_3[0], OBSTACLE_3[1], 20, 200)
else:
    v_obstacle_3 = pygame.Rect(OBSTACLE_3[0] + 180, OBSTACLE_3[1], 20, 200)

if OBSTACLE_4[2] == 0:
    v_obstacle_4 = pygame.Rect(OBSTACLE_4[0], OBSTACLE_4[1] - 180, 20, 200)
elif OBSTACLE_4[2] == 1:
    v_obstacle_4 = pygame.Rect(OBSTACLE_4[0] + 180, OBSTACLE_4[1] - 180, 20, 200)
elif OBSTACLE_4[2] == 2:
    v_obstacle_4 = pygame.Rect(OBSTACLE_4[0], OBSTACLE_4[1], 20, 200)
else:
    v_obstacle_4 = pygame.Rect(OBSTACLE_4[0] + 180, OBSTACLE_4[1], 20, 200)

# Dessin des obstacles
pygame.draw.rect(window, (255, 255, 255), h_obstacle_1)
pygame.draw.rect(window, (255, 255, 255), v_obstacle_1)

pygame.draw.rect(window, (255, 255, 255), h_obstacle_2)
pygame.draw.rect(window, (255, 255, 255), v_obstacle_2)

pygame.draw.rect(window, (255, 255, 255), h_obstacle_3)
pygame.draw.rect(window, (255, 255, 255), v_obstacle_3)

pygame.draw.rect(window, (255, 255, 255), h_obstacle_4)
pygame.draw.rect(window, (255, 255, 255), v_obstacle_4)


#boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    pygame.display.flip()

pygame.quit()