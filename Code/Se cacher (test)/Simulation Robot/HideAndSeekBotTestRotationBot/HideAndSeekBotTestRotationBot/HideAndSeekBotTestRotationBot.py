import pygame
import random
import math

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
WIDTH = 800
HEIGHT = 600

# Couleurs (RVB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Création de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Triangle en mouvement")

# Position et angle du triangle
x = WIDTH // 2
y = HEIGHT // 2
angle = 0

# Variables pour enregistrer les touches enfoncées
keys = {
    pygame.K_z: False,
    pygame.K_q: False,
    pygame.K_d: False
}

# Facteurs de vitesse
movement_speed = 0.1  # Vitesse de déplacement du triangle
rotation_speed = 0.1  # Vitesse de rotation du triangle

# Dimensions des bordures
border_thickness = 10

# Dimensions des parois en forme de L
wall_size = 100
wall_thickness = 10

# Génération des parois du labyrinthe
walls = []
for i in range(4):
    if i == 0:
        # Paroi supérieure
        wall_x = border_thickness
        wall_y = border_thickness
        wall_width = WIDTH - 2 * border_thickness
        wall_height = wall_thickness
    elif i == 1:
        # Paroi inférieure
        wall_x = border_thickness
        wall_y = HEIGHT - border_thickness - wall_height
        wall_width = WIDTH - 2 * border_thickness
        wall_height = wall_thickness
    elif i == 2:
        # Paroi gauche
        wall_x = border_thickness
        wall_y = border_thickness + wall_thickness
        wall_width = wall_thickness
        wall_height = HEIGHT - 2 * border_thickness - 2 * wall_thickness
    elif i == 3:
        # Paroi droite
        wall_x = WIDTH - border_thickness - wall_width
        wall_y = border_thickness + wall_thickness
        wall_width = wall_thickness
        wall_height = HEIGHT - 2 * border_thickness - 2 * wall_thickness

    walls.append(pygame.Rect(wall_x, wall_y, wall_width, wall_height))

# Fonction pour effectuer une rotation sur un point (x, y) autour d'un autre point (cx, cy)
def rotate(point, angle, cx, cy):
    x, y = point
    rad_angle = math.radians(angle)
    cos_theta = math.cos(rad_angle)
    sin_theta = math.sin(rad_angle)
    new_x = cos_theta * (x - cx) - sin_theta * (y - cy) + cx
    new_y = sin_theta * (x - cx) + cos_theta * (y - cy) + cy
    return (new_x, new_y)

# Fonction pour déplacer le triangle selon son repère
def move(distance):
    global x, y
    rad_angle = math.radians(angle)
    new_x = x + distance * math.sin(rad_angle)  # Déplacement perpendiculaire
    new_y = y - distance * math.cos(rad_angle)  # Déplacement perpendiculaire
    if not collides_with_walls(new_x, new_y):
        x, y = new_x, new_y

# Fonction pour vérifier les collisions avec les parois du labyrinthe
def collides_with_walls(new_x, new_y):
    for wall in walls:
        if wall.collidepoint(new_x, new_y):
            return True
    return False

# Boucle principale du jeu
running = True
while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                keys[pygame.K_z] = True
            elif event.key == pygame.K_q:
                keys[pygame.K_q] = True
            elif event.key == pygame.K_d:
                keys[pygame.K_d] = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_z:
                keys[pygame.K_z] = False
            elif event.key == pygame.K_q:
                keys[pygame.K_q] = False
            elif event.key == pygame.K_d:
                keys[pygame.K_d] = False

    # Mouvement et rotation
    if keys[pygame.K_z]:
        move(movement_speed)
    if keys[pygame.K_q]:
        angle -= rotation_speed
    if keys[pygame.K_d]:
        angle += rotation_speed

    # Effacer l'écran
    screen.fill(BLACK)

    # Dessiner les bordures
    pygame.draw.rect(screen, WHITE, (0, 0, WIDTH, border_thickness))  # Bordure supérieure
    pygame.draw.rect(screen, WHITE, (0, 0, border_thickness, HEIGHT))  # Bordure gauche
    pygame.draw.rect(screen, WHITE, (WIDTH - border_thickness, 0, border_thickness, HEIGHT))  # Bordure droite
    pygame.draw.rect(screen, WHITE, (0, HEIGHT - border_thickness, WIDTH, border_thickness))  # Bordure inférieure

    # Dessiner les parois du labyrinthe
    for wall in walls:
        pygame.draw.rect(screen, WHITE, wall)

    # Coordonnées des sommets du triangle dans son repère propre
    triangle_points = [(0, -30), (15, 15), (-15, 15)]

    # Calculer le centre de l'arête la plus courte
    center_x = (triangle_points[1][0] + triangle_points[2][0]) / 2
    center_y = (triangle_points[1][1] + triangle_points[2][1]) / 2

    # Effectuer la rotation pour obtenir les coordonnées dans le repère de la fenêtre
    rotated_points = [rotate(point, angle, center_x, center_y) for point in triangle_points]

    # Dessiner le triangle
    moved_points = [(point[0] + x, point[1] + y) for point in rotated_points]
    pygame.draw.polygon(screen, WHITE, moved_points)

    # Mettre à jour l'affichage
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
