# -*- coding: utf-8 -*-

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

#creation de la bordure du jeu
border_north = pygame.Rect(0,0,1000,20)
border_south = pygame.Rect(0,980,1000,20)
border_west = pygame.Rect(0,0,20,1000)
border_east = pygame.Rect(980,0,20,1000)

pygame.draw.rect(window,(250,250,250),border_north)
pygame.draw.rect(window,(250,250,250),border_south)
pygame.draw.rect(window,(250,250,250),border_east)
pygame.draw.rect(window,(250,250,250),border_west)

#coordonnée mur
COORD_X_WALL1 = randint(120,881)
COORD_Y_WALL1 = randint(120,881)
DIR_WALL1 = randint(0,4)
mur1 = [COORD_X_WALL1,COORD_Y_WALL1,DIR_WALL1]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False

    pygame.display.flip()

pygame.quit()