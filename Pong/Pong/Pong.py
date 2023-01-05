import pygame
import sys
import random

pygame.init()
clock = pygame.time.Clock()

# Fenetre
ecran_largeur = 1200
ecran_taille = 640
ecran = pygame.display.set_mode((ecran_largeur, ecran_taille))
pygame.display.set_caption('ESIEA GAMES - Pong')

# Rectangle - Pong
balle = pygame.Rect(ecran_largeur / 2 - 15, ecran_taille / 2 - 15, 30, 30)
joueur = pygame.Rect(ecran_largeur - 20, ecran_taille / 2 - 70, 10, 130)
joueur2 = pygame.Rect(10, ecran_taille / 2 - 70, 10, 130)

# Vitesse - Animation
vit_balleX = 7 * random.choice((-1, 1))
vit_balleY = 7 * random.choice((-1, 1))
vit_joueur = 0
"vit_joueur2 = 7  #Le bot ce faible e_e"
vit_joueur2 = 0

# Couleur
couleur = pygame.Color('white')
gris = (200, 200, 200)
background = (5, 48, 63)
decompte_couleur = (160, 168, 20)

# Score
score_joueur = 0
score_joueur2 = 0
font_score = pygame.font.Font("ressource_pong/font.ttf", 25)

# Timer
score_timer = True

# Son
son_pong = pygame.mixer.Sound("ressource_pong/pong.ogg")
son_score = pygame.mixer.Sound("ressource_pong/score.ogg")


def spawn_balle():
    global vit_balleX, vit_balleY, score_timer
    time = pygame.time.get_ticks()
    balle.center = (ecran_largeur / 2, ecran_taille / 2)

    # Timer qui spawn la balle avec un décompte !
    if time - score_timer < 700:
        decompte = font_score.render("3", False, decompte_couleur)
        ecran.blit(decompte, (ecran_largeur / 2 - 10, ecran_taille / 2 + 60))
    if 700 < time - score_timer < 1300:
        decompte = font_score.render("2", False, decompte_couleur)
        ecran.blit(decompte, (ecran_largeur / 2 - 10, ecran_taille / 2 + 60))
    if 1300 < time - score_timer < 2100:
        decompte = font_score.render("1", False, decompte_couleur)
        ecran.blit(decompte, (ecran_largeur / 2 - 10, ecran_taille / 2 + 60))

    if time - score_timer < 2100:
        vit_balleX = 0
        vit_balleY = 0
    else:
        vit_balleY = 7 * random.choice((-1, 1))
        vit_balleX = 7 * random.choice((-1, 1))
        score_timer = None


def Collision_balle():
    global vit_balleX, vit_balleY, score_joueur, score_joueur2, score_timer
    balle.x += vit_balleX
    balle.y += vit_balleY
    # Gère les collisions des deux joueur
    if balle.top <= 0 or balle.bottom >= ecran_taille:
        vit_balleY = vit_balleY * -1
    if balle.left <= 0 or balle.right >= ecran_largeur:
        vit_balleX = vit_balleX * -1
    if balle.left <= 0:
        score_joueur += 1
        pygame.mixer.Sound.play(son_score)
        score_timer = pygame.time.get_ticks()
    if balle.right >= ecran_largeur:
        score_joueur2 += 1
        pygame.mixer.Sound.play(son_score)
        score_timer = pygame.time.get_ticks()

    # Belle reprise de la balle ^^
    if balle.colliderect(joueur) and vit_balleX > 0:
        pygame.mixer.Sound.play(son_pong)
        if abs(balle.right - joueur.left) < 10:
            vit_balleX *= -1
        if abs(balle.bottom - balle.top) < 10 and vit_balleY > 0:
            vit_balleY = vit_balleY * -1
        elif abs(balle.top - balle.bottom) < 10 and vit_balleY < 0:
            vit_balleY = vit_balleY * -1

    if balle.colliderect(joueur2) and vit_balleX < 0:
        pygame.mixer.Sound.play(son_pong)
        if abs(balle.left - joueur2.right) < 10:
            vit_balleX *= -1
        if abs(balle.bottom - balle.top) < 10 and vit_balleY > 0:
            vit_balleY *= -1
        elif abs(balle.top - balle.bottom) < 10 and vit_balleY < 0:
            vit_balleY *= -1


# Bouger le joueur

def Animation_Joueur():
    global vit_joueur
    joueur.y += vit_joueur
    if joueur.top <= 0:
        joueur.top = 0
    if joueur.bottom >= ecran_taille:
        joueur.bottom = ecran_taille

# Meme principe mais avec un bot

def sans_amis():
    global vit_joueur2
    joueur2.y += vit_joueur2
    # Le bot ce faible e_e
    if joueur2.top < balle.y:
        joueur2.top += vit_joueur2
    if joueur2.bottom > balle.y:
        joueur2.bottom -= vit_joueur2
    if joueur2.top <= 0:
        joueur2.top = 0
    if joueur2.bottom >= ecran_taille:
        joueur2.bottom = ecran_taille


# Loop du jeu
while 1:
    # Les Inputs
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Touche du jeu - J1
        if evenement.type == pygame.KEYDOWN:
            if evenement.key == pygame.K_z:
                vit_joueur += 7
            if evenement.key == pygame.K_s:
                vit_joueur -= 7
        if evenement.type == pygame.KEYUP:
            if evenement.key == pygame.K_z:
                vit_joueur -= 7
            if evenement.key == pygame.K_s:
                vit_joueur += 7
        """
        # Touche du jeu - J2
        if evenement.type == pygame.KEYDOWN:
            if evenement.key == pygame.K_s:
                vit_joueur2 += 7
            if evenement.key == pygame.K_z:
                vit_joueur2 -= 7
        if evenement.type == pygame.KEYUP:
            if evenement.key == pygame.K_s:
                vit_joueur2 -= 7
            if evenement.key == pygame.K_z:
                vit_joueur2 += 7
        """
        # Quitter le jeu
        if evenement.type == pygame.KEYUP:
            if evenement.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    Collision_balle()
    Animation_Joueur()
    sans_amis()

    # Dessiner les joueurs / Balles / Background / Text
    ecran.fill(background)
    pygame.draw.ellipse(ecran, couleur, balle)
    pygame.draw.rect(ecran, couleur, joueur)
    pygame.draw.rect(ecran, couleur, joueur2)
    pygame.draw.aaline(ecran, couleur, (ecran_largeur / 2, 0), (ecran_largeur / 2, ecran_taille))

    score_joueur_display = font_score.render(f"{score_joueur}", False, gris)
    ecran.blit(score_joueur_display, (620, 200))
    score_joueur2_display = font_score.render(f"{score_joueur2}", False, gris)
    ecran.blit(score_joueur2_display, (560, 200))

    if score_timer:
        spawn_balle()

    # Update la window
    pygame.display.flip()
    clock.tick(60)  # FPS
