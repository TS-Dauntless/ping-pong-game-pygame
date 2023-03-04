import pygame
import random

# initializing pygame
pygame.init()

# creating the window
window = pygame.display.set_mode((800, 600))

# Background Music
pygame.mixer.music.load("aud/bg.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

# Creating logo
logo = pygame.transform.scale(pygame.image.load("img/ping pong logo.png"), (64, 64))
pygame.display.set_icon(logo)

# Placing Caption
pygame.display.set_caption("Ping Pong")

# Background image
background = pygame.image.load("img/background.jpeg")
background = pygame.transform.scale(background, (800, 600))

# Player A
player_a_img = pygame.transform.scale(pygame.image.load("img/bar.png"), (32, 128))
player_a_x_cor = 0
player_a_y_cor = 234
player_a_y_cor_change = 0
player_a_score = 0

# Player B
player_b_img = pygame.transform.scale(pygame.image.load("img/bar.png"), (32, 128))
player_b_x_cor = 768
player_b_y_cor = 234
player_b_y_cor_change = 0
player_b_score = 0

# Ball
ball_img = pygame.transform.scale(pygame.image.load("img/Ball.png"), (50, 50))
ball_x_cor = 350
ball_y_cor = 250
ball_x_cor_change = random.choice((0.5, -0.5, 0.4, -0.4))
ball_y_cor_change = random.choice((0.5, -0.5, 0.4, -0.4))


# Function to Show the score
def show_score():
    global player_a_score, player_b_score
    window.blit(pygame.font.Font("freesansbold.ttf", 40).render(f"Player A : {player_a_score}", True, (255, 255, 255)),
                (10, 10))
    window.blit(pygame.font.Font("freesansbold.ttf", 40).render(f"Player B : {player_b_score}", True, (255, 255, 255)),
                (410, 10))


# Game Main Loop
running = True

while running:
    # Backgrounds
    window.fill((255, 255, 255))
    window.blit(background, (0, 0))

    # Getting events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_b_y_cor_change += -0.5
            if event.key == pygame.K_DOWN:
                player_b_y_cor_change += 0.5
            if event.key == pygame.K_w:
                player_a_y_cor_change += -0.5
            if event.key == pygame.K_s:
                player_a_y_cor_change += 0.5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_b_y_cor_change += 0.5
            if event.key == pygame.K_DOWN:
                player_b_y_cor_change += -0.5
            if event.key == pygame.K_w:
                player_a_y_cor_change += 0.5
            if event.key == pygame.K_s:
                player_a_y_cor_change += -0.5

    # Displaying Player A
    window.blit(player_a_img, (player_a_x_cor, player_a_y_cor))

    # Adding movement to player A
    player_a_y_cor += player_a_y_cor_change

    # Applying border for player A
    if player_a_y_cor <= 0:
        player_a_y_cor = 0
    elif player_a_y_cor + 128 >= 600:
        player_a_y_cor = 600 - 128

    # Displaying player B
    window.blit(player_b_img, (player_b_x_cor, player_b_y_cor))

    # Adding movement to player B
    player_b_y_cor += player_b_y_cor_change

    # Applying border for player B
    if player_b_y_cor <= 0:
        player_b_y_cor = 0
    elif player_b_y_cor + 128 >= 600:
        player_b_y_cor = 600 - 128

    # Displaying Ball
    window.blit(ball_img, (ball_x_cor, ball_y_cor))

    # Adding movement to Ball
    ball_x_cor += ball_x_cor_change
    ball_y_cor += ball_y_cor_change

    # Applying border to ball
    if ball_y_cor <= -5:
        ball_y_cor = -5
        ball_y_cor_change *= -1
        pygame.mixer.Sound("aud/wall.wav").play()  # Wall hit sound

    elif ball_y_cor >= 555:
        ball_y_cor = 555
        ball_y_cor_change *= -1
        pygame.mixer.Sound("aud/wall.wav").play()  # Wall hit Sound

    # Ball hits Player
    if (0 <= ball_x_cor <= 32) and (ball_y_cor + 45 >= player_a_y_cor and ball_y_cor - 5 <= player_a_y_cor + 128):
        ball_x_cor = 33
        ball_x_cor_change *= -1
        pygame.mixer.Sound("aud/ball hit paddle.wav").play()  # Sound when ball hits player

    elif (768 <= ball_x_cor + 50 <= 800) and (ball_y_cor + 45 >= player_b_y_cor and ball_y_cor - 5 <= player_b_y_cor + 128):
        ball_x_cor = 717
        ball_x_cor_change *= -1
        pygame.mixer.Sound("aud/ball hit paddle.wav").play()  # Sound when ball hits player

    # Ball hits wall to over game
    # When player missed Ball
    if ball_x_cor < 0:
        player_b_score += 1
        ball_x_cor = 350
        ball_y_cor = 250
        ball_x_cor_change = random.choice((0.3, -0.3, 0.4, -0.4))
        ball_y_cor_change = random.choice((0.3, -0.3, 0.4, -0.4))
        pygame.mixer.Sound("aud/ball missed.wav").play()  # Sound when ball missed by player

    elif ball_x_cor > 750:
        player_a_score += 1
        ball_x_cor = 350
        ball_y_cor = 250
        ball_x_cor_change = random.choice((0.3, -0.3, 0.4, -0.4))
        ball_y_cor_change = random.choice((0.3, -0.3, 0.4, -0.4))
        pygame.mixer.Sound("aud/ball missed.wav").play()  # Sound when ball missed by player

    # Displaying Score
    show_score()
    # To update always
    pygame.display.update()
