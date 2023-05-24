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

bot_x = largeur_fenetre // 2  # Position initiale du robot (au centre de la fenêtre)
bot_y = hauteur_fenetre // 2
bot_dir = random.choice(['up', 'down', 'left', 'right','up-left','up-right','down-left','down-right'])  # Direction initiale aléatoire
wall_encountered = 0  # Compteur de murs rencontrés
wall_expected = random.randint(3, 4)  # Nombre de murs nécessaires pour se cacher
find_angle = False  # Indicateur pour le mode "cherche un coin"

border_north = pygame.Rect(0, 0,largeur_fenetre, 20)
border_north_c = pygame.Rect(20, 20,largeur_fenetre - 40, 20)
border_south = pygame.Rect(0, hauteur_fenetre - 20,largeur_fenetre, 20)
border_west = pygame.Rect(0, 0, 20, hauteur_fenetre)
border_west_c = pygame.Rect(20, 20, 20, hauteur_fenetre -40)
border_east = pygame.Rect(largeur_fenetre - 20, 0, 20, hauteur_fenetre)
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

h_obstacle_1 = pygame.Rect(OBSTACLE_1[0], OBSTACLE_1[1], 200, 20)
h_obstacle_2 = pygame.Rect(OBSTACLE_2[0], OBSTACLE_2[1], 200, 20)
h_obstacle_3 = pygame.Rect(OBSTACLE_3[0], OBSTACLE_3[1], 200, 20)
h_obstacle_4 = pygame.Rect(OBSTACLE_4[0], OBSTACLE_4[1], 200, 20)



def generate_labyrinth():
    

# Dessin de la bordure
    pygame.draw.rect(window, (255, 255, 255), border_north)
    pygame.draw.rect(window, (255, 255, 255), border_south)
    pygame.draw.rect(window, (255, 255, 255), border_east)
    pygame.draw.rect(window, (255, 255, 255), border_west)

# Coordonnées des murs
    

#initialisation des rectangle horizontaux
    


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
    

    pygame.draw.rect(window, (255, 255, 255), h_obstacle_1)
    pygame.draw.rect(window, (255, 255, 255), v_obstacle_1)

    pygame.draw.rect(window, (255, 255, 255), h_obstacle_2)
    pygame.draw.rect(window, (255, 255, 255), v_obstacle_2)

    pygame.draw.rect(window, (255, 255, 255), h_obstacle_3)
    pygame.draw.rect(window, (255, 255, 255), v_obstacle_3)

    pygame.draw.rect(window, (255, 255, 255), h_obstacle_4)
    pygame.draw.rect(window, (255, 255, 255), v_obstacle_4)  
    return (v_obstacle_1,v_obstacle_2,v_obstacle_3,v_obstacle_4)

# Création de la bordure du jeu
(v_obstacle_1,v_obstacle_2,v_obstacle_3,v_obstacle_4) = generate_labyrinth()


#boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    
    
            # Mouvement du robot
    pygame.draw.circle(window, (0, 0, 0), (bot_x, bot_y), 20)
        # Mode "avance tout droit"
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


        # Vérifier s'il y a une collision avec un mur
    if pygame.Rect(bot_x, bot_y, 20, 20).colliderect(h_obstacle_1) or \
                pygame.Rect(bot_x, bot_y, 20, 20).colliderect(h_obstacle_2) or \
                pygame.Rect(bot_x, bot_y, 20, 20).colliderect(h_obstacle_3) or \
                pygame.Rect(bot_x, bot_y, 20, 20).colliderect(h_obstacle_4) or \
                pygame.Rect(bot_x, bot_y, 20, 20).colliderect(v_obstacle_1) or \
                pygame.Rect(bot_x, bot_y, 20, 20).colliderect(v_obstacle_2) or \
                pygame.Rect(bot_x, bot_y, 20, 20).colliderect(v_obstacle_3) or \
                pygame.Rect(bot_x, bot_y, 20, 20).colliderect(v_obstacle_4) or \
                pygame.Rect(bot_x, bot_y, 20, 20).colliderect(border_east) or \
                pygame.Rect(bot_x, bot_y, 20, 20).colliderect(border_south):
         wall_encountered += 1
         directions_possibles = ['up', 'down', 'left', 'right','up-left','up-right','down-left','down-right']
         directions_possibles.remove(bot_dir)
         bot_dir = random.choice(directions_possibles)
    if pygame.Rect(bot_x, bot_y, 20, 20).colliderect(border_north_c):
        wall_encountered += 1
        bot_y +=5
        directions_possibles = ['up', 'down', 'left', 'right','up-left','up-right','down-left','down-right']
        directions_possibles.remove(bot_dir)
        bot_dir = random.choice(directions_possibles)
    if pygame.Rect(bot_x, bot_y, 20, 20).colliderect(border_west_c):
        wall_encountered += 1
        bot_x +=5
        directions_possibles = ['up', 'down', 'left', 'right','up-left','up-right','down-left','down-right']
        directions_possibles.remove(bot_dir)
        bot_dir = random.choice(directions_possibles)

            # Vérifier si le robot a rencontré suffisamment de murs pour se cacher
    if wall_encountered >= wall_expected:
         ind_angle = True
    
                # Choisir une nouvelle direction aléatoire sans retourner en arrière
        
    
          

    clock.tick(100)
    pygame.draw.circle(window, (255, 0, 0), (bot_x, bot_y), 20)  
    pygame.display.flip()
    


pygame.quit()