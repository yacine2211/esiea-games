background_image = "ciel.webp"

#import libraries
import pygame
import time
import random


pygame.init() # initialise les sous-modules du package PyGame
screen = pygame.display.set_mode((640,455)) # renvoie un objet de la classe Surface représentant la fenêtre.

pygame.display.set_caption("SNAKE")
background = pygame.image.load(background_image).convert()# la fonction pygame.image.load télécharge l’image d’arrière plan à partir de notre disque. Quant à la fonction convert(), qui est membre de l’objet Surface, elle convertit l’image au même format que notre affichage.

score = 0
snake_speed = 10
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
run = True
direction = 'right'
fruit = [random.randrange(0,640,10), random.randrange(0,450,10)]

# position de la tête du serpent
snake_head = [250, 200]

# corps du serpent
snake_body = [[250, 200], [240, 200], [230, 200], [220, 200]]

# FPS(frames per second)
fps = pygame.time.Clock()

def gameover():
    screen.blit(text, textRect)# affiche le game over
    screen.blit(text1, textRect1)# affiche le score
    pygame.display.flip()
    time.sleep(5)# attend 5 seconde avant de passer à la suite
    pygame.quit()# quitter Pygame, c’est en quelque sorte l’opposé de la fonction pygame.init()
    quit()# quitter Python.

#main structure 
while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                if direction == 'right':
                    direction = 'right'
                else:
                    direction = 'left'
            if event.key == pygame.K_d:
                if direction == 'left':
                    direction = 'left'
                else:
                    direction = 'right'
            if event.key == pygame.K_z:
                if direction == 'down':
                    direction = 'down'
                else:
                    direction = 'up'
            if event.key == pygame.K_s:
                if direction == 'up':
                    direction = 'up'
                else:
                    direction = 'down'
              
    
    #print(direction)
    if direction == 'left':
        snake_head[0] -= 10
    if direction == 'right':
        snake_head[0] += 10
    if direction == 'up':
        snake_head[1] -= 10
    if direction == 'down':
        snake_head[1] += 10
        
    # snake touche le bord = perdue    
    if snake_head[0]<0 or snake_head[0]>640:
        gameover()
    if snake_head[1]<0 or snake_head[1]>455:
        gameover()
    # snake touche son corps = perdue
    for x in snake_body:
        if snake_head == x:
            gameover()
    # si snake mange le fuit = augmentation de la taille du serpent
    if snake_head[0] == fruit[0] and snake_head[1] == fruit[1]:      
        snake_body.insert(0, list(snake_head))
        background = pygame.image.load(background_image).convert()#raffraichie le background
        fruit = [random.randrange(0,640,10), random.randrange(0,450,10)]#nouvelle position du fruit
        snake_speed += 1# incrémente la vitesse de 1 après chaque fruit manger
        score += 10# incrémente le score de 10 après chaque fruit manger
    # sinon rien
    else:
        snake_body.insert(0, list(snake_head))#ajoute la nouvelle position du snake en première element de snake_body
        del snake_body[-1]#supprime le dernier élement de snake_body
         
    #affichage text sur image
    font = pygame.font.Font('freesansbold.ttf', 40)
    font1 = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('Game Over', True, red, black)
    text1 = font1.render('Score: '+ str(score), True, red)
    textRect = text.get_rect()
    textRect1 = text.get_rect()
    textRect.center = (325, 200)

    # print("fruit")
    # print(fruit)
    # print("body")
    # print(list(snake_body))
    # print("head")
    # print(snake_head)
    # print("speed")
    # print(snake_speed)
    
    background = pygame.image.load(background_image).convert()#raffraichie le background
    
    pygame.draw.rect(background, red, pygame.Rect(fruit[0], fruit[1], 10, 10))#dessine le fruit
    for i in snake_body:
        pygame.draw.rect(background, black, pygame.Rect(i[0], i[1], 10, 10))#dessine le snake
       
    
            
    # Frame Per Second /temps de rafraichissement de l'image du jeu
    fps.tick(snake_speed)
        
    pygame.display.update()

    screen.blit(background, (0,0))#La méthode background.blit() dessine l’image avec des coordonnées initiales.
    
gameover()# réfère a la fonction quitter du programme

