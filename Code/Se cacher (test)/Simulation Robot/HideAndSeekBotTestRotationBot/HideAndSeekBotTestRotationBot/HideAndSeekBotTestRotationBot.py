import pygame
import math

# Initialisation de Pygame
pygame.init()

# Dimensions de la fen�tre
WIDTH = 800
HEIGHT = 600

# Couleurs (RVB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Cr�ation de la fen�tre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Triangle en mouvement")

# Position et angle du triangle
x = WIDTH // 2
y = HEIGHT // 2
angle = 0

# Variables pour enregistrer les touches enfonc�es
keys = {
    pygame.K_z: False,
    pygame.K_q: False,
    pygame.K_d: False
}

# Facteurs de vitesse
movement_speed = 0.1  # Vitesse de d�placement du triangle
rotation_speed = 0.2  # Vitesse de rotation du triangle

# Fonction pour effectuer une rotation sur un point (x, y) autour d'un autre point (cx, cy)
def rotate(point, angle, cx, cy):
    x, y = point
    rad_angle = math.radians(angle)
    cos_theta = math.cos(rad_angle)
    sin_theta = math.sin(rad_angle)
    new_x = cos_theta * (x - cx) - sin_theta * (y - cy) + cx
    new_y = sin_theta * (x - cx) + cos_theta * (y - cy) + cy
    return (new_x, new_y)

# Fonction pour d�placer le triangle selon son rep�re
def move(distance):
    global x, y
    rad_angle = math.radians(angle)
    new_x = x - distance * math.cos(rad_angle + math.pi / 2)  # D�placement perpendiculaire invers�
    new_y = y - distance * math.sin(rad_angle + math.pi / 2)  # D�placement perpendiculaire invers�
    x, y = new_x, new_y

# Boucle principale du jeu
running = True
while running:
    # Gestion des �v�nements
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

    # V�rifier les touches enfonc�es pour le mouvement et la rotation
    if keys[pygame.K_z]:
        move(movement_speed)  # D�placer le triangle vers l'avant
    if keys[pygame.K_q]:
        angle -= rotation_speed  # Faire pivoter le triangle dans le sens horaire
    if keys[pygame.K_d]:
        angle += rotation_speed  # Faire pivoter le triangle dans le sens anti-horaire

    # Effacer l'�cran
    screen.fill(BLACK)

    # Coordonn�es des sommets du triangle dans son rep�re propre
    triangle_points = [(0, -30), (15, 15), (-15, 15)]

    # Calculer l'ar�te la plus courte
    shortest_edge = min(math.dist(triangle_points[0], triangle_points[1]), math.dist(triangle_points[1], triangle_points[2]), math.dist(triangle_points[2], triangle_points[0]))

    # Calculer le centre de l'ar�te la plus courte
    center_x = (triangle_points[1][0] + triangle_points[2][0]) / 2
    center_y = (triangle_points[1][1] + triangle_points[2][1]) / 2

    # Effectuer la rotation pour obtenir les coordonn�es dans le rep�re de la fen�tre
    rotated_points = [rotate(point, angle, center_x, center_y) for point in triangle_points]

    # Dessiner le triangle
    moved_points = [(point[0] + x, point[1] + y) for point in rotated_points]
    pygame.draw.polygon(screen, WHITE, moved_points)

    # Mettre � jour l'affichage
    pygame.display.flip()

# Quitter Pygame
pygame.quit()