import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 800
HEIGHT = 600
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 90
BALL_SIZE = 15
PADDLE_SPEED = 5
BALL_SPEED = 7

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Create game objects
player = pygame.Rect(50, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
opponent = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH//2 - BALL_SIZE//2, HEIGHT//2 - BALL_SIZE//2, BALL_SIZE, BALL_SIZE)

# Ball movement
ball_speed_x = BALL_SPEED * random.choice((1, -1))
ball_speed_y = BALL_SPEED * random.choice((1, -1))

# Score
player_score = 0
opponent_score = 0
font = pygame.font.Font(None, 74)

def move_paddle(paddle, up=True):
    if up and paddle.top > 0:
        paddle.y -= PADDLE_SPEED
    if not up and paddle.bottom < HEIGHT:
        paddle.y += PADDLE_SPEED

def move_ball(ball):
    global ball_speed_x, ball_speed_y, player_score, opponent_score
    
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with top and bottom
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    # Ball collision with paddles
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

    # Score points
    if ball.left <= 0:
        opponent_score += 1
        ball_reset()
    if ball.right >= WIDTH:
        player_score += 1
        ball_reset()

def ball_reset():
    global ball_speed_x, ball_speed_y
    ball.center = (WIDTH//2, HEIGHT//2)
    ball_speed_y = BALL_SPEED * random.choice((1, -1))
    ball_speed_x = BALL_SPEED * random.choice((1, -1))

def opponent_ai():
    if opponent.top < ball.y:
        opponent.y += PADDLE_SPEED
    if opponent.bottom > ball.y:
        opponent.y -= PADDLE_SPEED

# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        move_paddle(player, up=True)
    if keys[pygame.K_DOWN]:
        move_paddle(player, up=False)

    # Move the ball and AI
    move_ball(ball)
    opponent_ai()

    # Drawing
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player)
    pygame.draw.rect(screen, WHITE, opponent)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT))

    # Display score
    player_text = font.render(str(player_score), False, WHITE)
    opponent_text = font.render(str(opponent_score), False, WHITE)
    screen.blit(player_text, (WIDTH//4, 20))
    screen.blit(opponent_text, (3*WIDTH//4, 20))

    pygame.display.flip()
    clock.tick(60)