import pygame
import sys
import random
pygame.init()
screen_width = 1290
screen_height = 737
running=True

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Basics")
background_color = ('black')
play_button=pygame.Rect(545,268.5,200,50)
exit_button=pygame.Rect(545,268.5+80,200,50)

def ping_pong():
    ball_speed = 4  # common

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Pygame basics")

    running = True

    background_color = pygame.Color("black")

    paddle_width, paddle_height = 150, 13

    paddle_speed = 6

    score = 0

    paddle = pygame.Rect(645, 710, paddle_width, paddle_height)

    ball_radius = 30
    ball = pygame.Rect(250, 200, ball_radius, ball_radius)
    ball_x = random.choice([-4, 4])
    ball_y = ball_speed

    font = pygame.font.Font(pygame.font.match_font('Arial', bold=True), 20)

    while running:

        pygame.time.delay(20)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # move the ball

        ball.x += ball_x
        ball.y += ball_y

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and paddle.left > 0:
            paddle.x -= paddle_speed

        if keys[pygame.K_RIGHT] and paddle.right < screen_width:
            paddle.x += paddle_speed
        # check for collision

        if ball.colliderect(paddle):  # returns true if the ball is in collision, else it returns false
            ball_y = -ball_y  # go up
            score += 1

        if ball.y <= 0:
            ball_y = - ball_y
            ball_x = random.choice([-4, 4])

        if ball.left <= 0 or ball.right >= screen_width:
            ball_x = -ball_x

        if ball.y >= screen_height:
            ball.x = screen_width // 2
            ball.y = screen_height - 737 + 20
            ball_x = random.choice([-4, 4])
            score = 0

        screen.fill(background_color)  # to update the display screen

        hello = font.render(f'Score:{score}', True, 'white')
        screen.blit(hello, (screen_width - 120, 10))

        # pygame.draw.circle(screen,'white',(50,50),ball_radius)

        pygame.draw.rect(screen, 'white', paddle)

        pygame.draw.ellipse(screen, 'white', ball)
        pygame.display.flip()

    return

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type==pygame.MOUSEBUTTONDOWN:
            if exit_button.collidepoint(event.pos):
                running=False
            if play_button.collidepoint(event.pos):
                print("play button was clicked")
                ping_pong()


    screen.fill(background_color)

    pygame.draw.rect(screen,'green',play_button,border_radius=20)
    pygame.draw.rect(screen,'red',exit_button,border_radius=20)
    font=pygame.font.Font(None,36)

    play_text=font.render("Play",True,'black')
    exit_text=font.render("Exit",True,'black')

    screen.blit(play_text,(play_button.x+75,play_button.y+10))
    screen.blit(exit_text, (exit_button.x+75, exit_button.y+10))

    pygame.display.flip()
