from random import choice
import pygame, sys
from Space.Joueur import Joueur
from Space import Obstacle
from Space.Ennemie import Alien
from Space.laser import Laser

# Les paths sont à changer
pygame.init()
clock = pygame.time.Clock()
ecran_largeur = 800
ecran_hauteur = 600
ecran = pygame.display.set_mode((ecran_largeur, ecran_hauteur))
son_alien = pygame.mixer.Sound("/Users/utilisateur1/PycharmProjects/ESIEA_PST/Space/ressource_space/invaderkilled.wav")
son_dead = pygame.mixer.Sound("/Users/utilisateur1/PycharmProjects/ESIEA_PST/Space/ressource_space/explosion.wav")
son_back = pygame.mixer.Sound("/Users/utilisateur1/PycharmProjects/ESIEA_PST/Space/ressource_space/spaceinvaders1.mpeg")
pygame.mixer.Sound.play(son_back)
pygame.mixer.Sound.set_volume(son_back, 100)
pygame.mixer.Sound.set_volume(son_alien, 50)
pygame.mixer.Sound.set_volume(son_dead, 50)


class Game:
    def __init__(self):
        player_sprite = Joueur((ecran_largeur / 2, ecran_hauteur), ecran_largeur, 5)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        self.shape = Obstacle.shape
        self.taille_block = 8
        self.blocks = pygame.sprite.Group()
        self.num_obstacle = 2
        self.obstacle_x_pos = [num * (ecran_largeur / self.num_obstacle) for num in range(self.num_obstacle)]
        self.mul_obstacle(x_pos=ecran_largeur / 15, y_pos=500, *self.obstacle_x_pos)

        self.alien = pygame.sprite.Group()
        self.alien_setup(rows=7, cols=12)
        self.alien_direction = 1
        self.alien_las = pygame.sprite.Group()

        self.score = 0
        self.font = pygame.font.Font('/Users/utilisateur1/PycharmProjects/ESIEA_PST/Space/ressource_space/font.ttf', 20)

        self.over = True

    def obstacle(self, x_pos, y_pos, x_offset):
        for index_row, row in enumerate(self.shape):
            for index_col, col in enumerate(row):
                if col == 'x':
                    x = x_pos + index_col * self.taille_block + x_offset
                    y = y_pos + index_row * self.taille_block
                    block = Obstacle.obstacle(self.taille_block, (183, 229, 246), x, y)
                    self.blocks.add(block)

    def mul_obstacle(self, *offset, x_pos, y_pos):
        for x_offset in offset:
            self.obstacle(x_pos, y_pos, x_offset)

    def alien_setup(self, rows, cols, x_dist=60, y_dist=48, x_offset=70, y_offset=100):
        for index_row, row in enumerate(range(rows)):
            for index_col, col in enumerate(range(cols)):
                x = index_col * x_dist + x_offset
                y = index_row * y_dist + y_offset
                if index_row == 0:
                    alien_sprite = Alien('blue', x, y)
                elif 1 <= index_row <= 2:
                    alien_sprite = Alien('green', x, y)
                else:
                    alien_sprite = Alien('orange', x, y)
                self.alien.add(alien_sprite)

    def alien_dir(self):
        all_ennemie = self.alien.sprites()
        for alien in all_ennemie:
            if alien.rect.right >= ecran_largeur:
                self.alien_direction = -1
                self.alien_descend(1)
            elif alien.rect.left <= 0:
                self.alien_direction = 1
                self.alien_descend(1)

    def alien_descend(self, distance):
        if self.alien:
            for alien in self.alien.sprites():
                alien.rect.y += distance

    def alien_laser(self):
        if self.alien.sprites():
            random_ennemie = choice(self.alien.sprites())
            laser_sprite = Laser(random_ennemie.rect.center, 6, ecran_hauteur)
            laser_sprite.image.fill('yellow')
            self.alien_las.add(laser_sprite)

    def collision(self):
        if self.player.sprite.laser:

            for lasers in self.player.sprite.laser:
                if pygame.sprite.spritecollide(lasers, self.blocks, True):
                    lasers.kill()

                alien_toucher = pygame.sprite.spritecollide(lasers, self.alien, True)
                if alien_toucher:
                    pygame.mixer.Sound.play(son_alien)
                    for alien in alien_toucher:
                        self.score += alien.value
                    lasers.kill()

        if self.alien_las:
            for lasers in self.alien_las:
                if pygame.sprite.spritecollide(lasers, self.blocks, True):
                    lasers.kill()

                if pygame.sprite.spritecollide(lasers, self.player, False):
                    lasers.kill()
                    pygame.mixer.Sound.play(son_dead)
                    self.over = False

        if self.alien:
            for alien in self.alien:
                pygame.sprite.spritecollide(alien, self.blocks, True)
                if pygame.sprite.spritecollide(alien, self.player, False):
                    pygame.quit()
                    sys.exit()

    def score_disp(self):
        surface_score = self.font.render(f'score: {self.score}', False, 'white')
        score_rect = surface_score.get_rect(topleft=(0, 0))
        ecran.blit(surface_score, score_rect)

    def victoire(self):
        if not self.alien.sprites():
            ecran.fill((0, 0, 0))
            victoire_surf = self.font.render('GG mon amie =^D', False, 'white')
            victoire_rect = victoire_surf.get_rect(center=(ecran_largeur / 2, ecran_hauteur / 2))
            ecran.blit(victoire_surf, victoire_rect)

    def Loser(self):
        if not self.over:
            keys = pygame.key.get_pressed()
            ecran.fill((0, 0, 0))
            loser_surf = self.font.render('Tragique mais ta perdu', False, 'white')
            loser_surf_2 = self.font.render('Fais échape pour fermer la fenetre', False, 'white')
            loser_surf_3 = self.font.render('Fais Entrer pour rejouer', False, 'white')
            loser_rect = loser_surf.get_rect(center=(ecran_largeur / 2, ecran_hauteur / 3))
            loser_rect_2 = loser_surf.get_rect(center=(ecran_largeur / 2.7, ecran_hauteur / 1.2))
            loser_rect_3 = loser_surf.get_rect(center=(ecran_largeur / 2, ecran_hauteur / 2))

            ecran.blit(loser_surf, loser_rect)
            ecran.blit(loser_surf_2, loser_rect_2)
            ecran.blit(loser_surf_3, loser_rect_3)

            pygame.mixer.Sound.stop(son_dead)
            pygame.mixer.Sound.stop(son_alien)
            pygame.mixer.Sound.stop(son_back)

            if keys[pygame.K_RETURN]:
                main()
            elif keys[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()

    def run(self):
        self.player.sprite.laser.draw(ecran)
        self.player.update()
        self.player.draw(ecran)
        self.blocks.draw(ecran)
        self.alien.draw(ecran)
        self.alien.update(self.alien_direction)
        self.alien_dir()
        self.alien_las.update()
        self.alien_las.draw(ecran)
        self.collision()
        self.score_disp()
        self.victoire()
        self.Loser()


def main():
    game = Game()
    Laser_Alien = pygame.USEREVENT + 1
    pygame.time.set_timer(Laser_Alien, 100)
    pygame.mixer.Sound.play(son_back)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == Laser_Alien:
                game.alien_laser()

        ecran.fill((30, 30, 30))
        game.run()
        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main()
