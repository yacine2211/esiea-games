import pygame


# Gère les lasers
class Laser(pygame.sprite.Sprite):
    def __init__(self, pos, speed ,hauteur):
        super().__init__()
        self.image = pygame.Surface((3, 15))
        self.image.fill('white')
        self.rect = self.image.get_rect(center=pos)
        self.speed = speed
        self.hauteur_contrainte = hauteur

    def delete(self):
        if self.rect.y <= 50 or self.rect.y >= self.hauteur_contrainte + 50:
            self.kill()

    def update(self):
        self.rect.y += self.speed
