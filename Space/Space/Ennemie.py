import pygame


# Gère les ennemies : le path est à changer
class Alien(pygame.sprite.Sprite):
    def __init__(self, couleur, x, y):
        super().__init__()
        fichier = '/Users/utilisateur1/PycharmProjects/ESIEA_PST/Space/ressource_space/Ennemie/' + couleur + '.png'
        self.image = pygame.image.load(fichier).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))

        if couleur == 'blue':
            self.value = 300
        elif couleur == 'green':
            self.value = 200
        elif couleur == 'orange':
            self.value = 100

    def update(self, direction):
        self.rect.x += direction
