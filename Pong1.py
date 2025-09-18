import pygame

# Initialize Pygame
pygame.init()

# Game Variables
WIDTH, HEIGHT = 800, 600
BALL_SPEED_X, BALL_SPEED_Y = 4, 4
PADDLE_SPEED = 6

# Colors
WHITE = (255, 255, 255)
TEAL = (99, 200, 148)
MAROON = (198, 10, 101)
BLACK = (0, 0, 0)

# Screen Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong by @Rohan Kumar")

# Load Background Image
bg_image = pygame.image.load("forest_mountains_sunset_cool_weather_minimalism.gif") 
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))

# Paddle & Ball Setup
paddle_width, paddle_height = 10, 100
ball_size = 20

paddle_a = pygame.Rect(30, HEIGHT // 2 - 50, paddle_width, paddle_height)
paddle_b = pygame.Rect(WIDTH - 40, HEIGHT // 2 - 50, paddle_width, paddle_height)
ball = pygame.Rect(WIDTH // 2 - 10, HEIGHT // 2 - 10, ball_size, ball_size)

# Score
score_a, score_b = 0, 0
font = pygame.font.Font(None, 40)

# Load Sound
bounce_sound = pygame.mixer.Sound("Bounce.wav")

# Game Loop
running = True
clock = pygame.time.Clock()

while running:
    screen.blit(bg_image, (0, 0))  # Draw background

    # Event Handling
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move Paddles with Boundaries
    if keys[pygame.K_w] and paddle_a.top > 0:
        paddle_a.y -= PADDLE_SPEED
    if keys[pygame.K_s] and paddle_a.bottom < HEIGHT:
        paddle_a.y += PADDLE_SPEED
    if keys[pygame.K_UP] and paddle_b.top > 0:
        paddle_b.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and paddle_b.bottom < HEIGHT:
        paddle_b.y += PADDLE_SPEED

    # Move Ball
    ball.x += BALL_SPEED_X
    ball.y += BALL_SPEED_Y

    # Ball Collision with Walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        BALL_SPEED_Y *= -1
        bounce_sound.play()

    # Ball Collision with Paddles
    if ball.colliderect(paddle_a) and BALL_SPEED_X < 0:
        BALL_SPEED_X *= -1
        ball.x = paddle_a.right  # Prevents ball from getting stuck

    if ball.colliderect(paddle_b) and BALL_SPEED_X > 0:
        BALL_SPEED_X *= -1
        ball.x = paddle_b.left - ball_size  # Prevents ball from getting stuck

    # Score Update & Reset Ball
    if ball.left <= 0:
        score_b += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)
        BALL_SPEED_X = 4  # Reset speed
        BALL_SPEED_Y = 4
    if ball.right >= WIDTH:
        score_a += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)
        BALL_SPEED_X = -4  # Reset speed
        BALL_SPEED_Y = 4

    # Draw Everything
    pygame.draw.rect(screen, TEAL, paddle_a)
    pygame.draw.rect(screen, TEAL, paddle_b)
    pygame.draw.ellipse(screen, MAROON, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    # Score Display
    score_text = font.render(f"Player A: {score_a}   Player B: {score_b}", True, BLACK)
    screen.blit(score_text, (WIDTH // 2 - 100, 20))

    # Update Display
    pygame.display.flip()
    clock.tick(60)  # 60 FPS

pygame.quit()
