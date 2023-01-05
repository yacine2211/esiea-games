import pygame
from Space.laser import Laser


# Gère le joueur (le path est à changé)
class Joueur(pygame.sprite.Sprite):
    def __init__(self, pos, constraint, speed):
        super().__init__()
        self.image = pygame.image.load(
            '/Users/utilisateur1/PycharmProjects/ESIEA_PST/Space/ressource_space/player.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=pos)
        self.speed = speed
        self.max_contrainte = constraint
        self.charger = True
        self.timer_laser = 0
        self.cooldown_laser = 100
        self.laser = pygame.sprite.Group()

    def input(self):
        keys = pygame.key.get_pressed()
        son_tire = pygame.mixer.Sound("/Users/utilisateur1/PycharmProjects/ESIEA_PST/Space/ressource_space/shoot.wav")
        # pygame.mixer.Sound.set_volume(son_tire, 50)
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        elif keys[pygame.K_q]:
            self.rect.x -= self.speed

        if keys[pygame.K_z] and self.charger:
            pygame.mixer.Sound.play(son_tire)
            self.tirer()
            self.charger = False
            self.timer_laser = pygame.time.get_ticks()

    # Un temps de recharge pour pas tirer en continue rapidement
    def recharge(self):
        if not self.charger:
            current_time = pygame.time.get_ticks()
            if current_time - self.timer_laser >= self.cooldown_laser:
                self.charger = True

    # Pour ne pas aller hors limite
    def contrainte(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.max_contrainte:
            self.rect.right = self.max_contrainte

    def tirer(self):
        self.laser.add(Laser(self.rect.center, -5, self.rect.bottom))

    # update la frame
    def update(self):
        self.input()
        self.contrainte()
        self.recharge()
        self.laser.update()
