import pygame

# Initialization of the Game
pygame.init()
width = 1500
height = 900
screen = pygame.display.set_mode((width, height))  # Width by Height

# Window Stuff
pygame.display.set_caption('Pong')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# Player Stuff
player_img = pygame.image.load('player.png')
player_X = 10
player_Y_default = height / 2 - 100
player_Y_dif = 0

# Ball Stuff
ball_img = pygame.image.load('ball.png')
ball_X = width / 2 - 15
ball_Y = height / 2 - 15
ball_dir_X = -3
ball_dir_Y = 3

# CPU Stuff
cpu_img = pygame.image.load('player.png')
cpu_X = width - 10 - 27
cpu_Y = height / 2 - 100


def player(y_val):
    screen.blit(player_img, (player_X, y_val))


def ball():
    screen.blit(ball_img, (ball_X, ball_Y))


def cpu():
    screen.blit(cpu_img, (cpu_X, cpu_Y))


def calc_cpu():
    global cpu_Y
    global ball_Y
    if cpu_Y + 100 - ball_Y - 15 > 0:
        cpu_Y -= 3
    elif cpu_Y + 100 - ball_Y - 15 < 0:
        cpu_Y += 3
    cpu_Y = min(cpu_Y, height - 10 - 200)
    cpu_Y = max(cpu_Y, 10)


def game_over(win):
    global ball_dir_X
    global ball_dir_Y
    global ball_X
    global ball_Y
    print(win)
    ball_X = width / 2 - 15
    ball_Y = height / 2 - 15
    ball_dir_X = -3
    ball_dir_Y = 3


