import pygame

# Définition des constantes
BLOC_SIZE = 30
GRID_WIDTH = 10
GRID_HEIGHT = 20
SCREEN_WIDTH = GRID_WIDTH * BLOC_SIZE
SCREEN_HEIGHT = GRID_HEIGHT * BLOC_SIZE

# Initialisation de Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Définition de la forme des pièces de Tetris
shapes = [
    [[1, 1, 1],
     [0, 1, 0]],
    [[0, 2, 2],
     [2, 2, 0]],
    [[3, 3, 0],
     [0, 3, 3]],
    [[4, 0, 0],
     [4, 4, 4]],
    [[0, 0, 5],
     [5, 5, 5]],
    [[6, 6, 6, 6]],
    [[7, 7],
     [7, 7]]
]

# Fonction pour dessiner les pièces de Tetris
def draw_piece(piece, x, y):
    for i in range(len(piece)):
        for j in range(len(piece[i])):
            if piece[i][j] != 0:
                pygame.draw.rect(screen, (255, 255, 255), (x+j*BLOC_SIZE, y+i*BLOC_SIZE, BLOC_SIZE, BLOC_SIZE), 0)

# Boucle principale du jeu
running = True
while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Dessin du fond de l'écran
    screen.fill((0, 0, 0))
    
    # Dessin d'une pièce de Tetris
    draw_piece(shapes[0], 60, 60)
    
    # Mise à jour de l'écran
    pygame.display.flip()

# Fermeture de Pygame
pygame.quit()

while True:
    record = get_record()
    dx, rotate = 0, False
    sc.blit(bg, (0, 0))
    sc.blit(game_sc, (20, 20))
    game_sc.blit(game_bg, (0, 0))
    # delay for full lines
    for i in range(lines):
        pygame.time.wait(200)
    # control
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_LEFT:
                dx = -1
            if event.key == pygame.K_RIGHT:
                dx = 1
            if event.key == pygame.K_UP:
                rotate = True
            if event.key == pygame.K_DOWN:
                anim_count, anim_speed = anim_limit, 1
    # move and rotate
    if dx or rotate:
        old_figure = deepcopy(figure)
        for i in range(len(figure)):
            figure[i].x += dx
            if rotate:
                figure[i] = (figure[i][1] * -1, figure[i][0])
        if not all(check_borders() for i in range(len(figure))):
            figure = old_figure
    # check full lines
    for i in range(H - 1, -1, -1):
        if all(field[i]):
            lines += 1
            score += scores[len(figure)]
            for j in range(i, 0, -1):
                field[j] = field[j - 1]
            field[0] = [0 for _ in range(W)]
    # move figure down
    anim_count += anim_speed
    if anim_count >= anim_limit:
        anim_count = 0
        figure_rect.y += 1
        for i in range(len(figure)):
            figure[i].y += 1
        if not all(check_borders() for i in range(len(figure))):
            for i in range(len(figure)):
def draw_figure(figure, color):
    for i in range(4):
        figure_rect.x, figure_rect.y = figure[i].x * TILE + 1, figure[i].y * TILE + 1
        pygame.draw.rect(game_sc, color, figure_rect)


def draw_next_figure(next_figure, next_color):
    for i in range(4):
        figure_rect.x, figure_rect.y = (next_figure[i].x + W + 3) * TILE + 1, (next_figure[i].y + 2) * TILE + 1
        pygame.draw.rect(game_sc, next_color, figure_rect)


def draw_field(color):
    for i in range(H):
        for j in range(W):
            if field[i][j]:
                pygame.draw.rect(game_sc, color, pygame.Rect(j * TILE + 1, i * TILE + 1, TILE - 2, TILE - 2))


def new_figure():
    global figure, next_figure, color, next_color, anim_count, anim_limit
    figure = next_figure
    color = next_color
    next_figure = deepcopy(choice(figures))
    next_color = get_color()
    anim_count, anim_limit = 0, randrange(500, 2000)
    if not check_borders():
        return False
    return True


def move_figure(dx):
    global figure
    figure = [pygame.Rect(x.x + dx, x.y, 1, 1) for x in figure]
    if not check_borders():
        figure = [pygame.Rect(x.x - dx, x.y, 1, 1) for x in figure]
        return False
    return True


def rotate_figure():
    global figure
    if len(figure) == 4:
        x1, y1, x2, y2 = figure[0].x, figure[0].y, figure[1].x, figure[1].y
        if x1 == x2:
            if y1 > y2:
                dx, dy = figure[0].x - figure[2].x, figure[0].y - figure[2].y
            else:
                dx, dy = figure[0].x - figure[3].x,

