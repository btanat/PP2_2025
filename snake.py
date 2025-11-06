import pygame
import sys
import random

pygame.init()

# window and cell size
WIDTH = 600
HEIGHT = 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# snake setup
snake = [[100, 100], [80, 100], [60, 100]]
direction = "RIGHT"

# random food position
food = [random.randrange(0, WIDTH // CELL_SIZE) * CELL_SIZE,
        random.randrange(0, HEIGHT // CELL_SIZE) * CELL_SIZE]

score = 0
level = 1
speed = 10

font = pygame.font.SysFont("Arial", 20)
clock = pygame.time.Clock()

# draw the snake
def draw_snake(snake):
    for block in snake:
        pygame.draw.rect(screen, GREEN, (block[0], block[1], CELL_SIZE, CELL_SIZE))

# draw the food
def draw_food(food):
    pygame.draw.rect(screen, RED, (food[0], food[1], CELL_SIZE, CELL_SIZE))

# show score and level
def show_info(score, level):
    text = font.render(f"Score: {score}   Level: {level}", True, WHITE)
    screen.blit(text, (10, 10))

# main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # movement control
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != "DOWN":
        direction = "UP"
    if keys[pygame.K_DOWN] and direction != "UP":
        direction = "DOWN"
    if keys[pygame.K_LEFT] and direction != "RIGHT":
        direction = "LEFT"
    if keys[pygame.K_RIGHT] and direction != "LEFT":
        direction = "RIGHT"

    # move snake head
    head = list(snake[0])
    if direction == "UP":
        head[1] -= CELL_SIZE
    if direction == "DOWN":
        head[1] += CELL_SIZE
    if direction == "LEFT":
        head[0] -= CELL_SIZE
    if direction == "RIGHT":
        head[0] += CELL_SIZE

    # add new head
    snake.insert(0, head)

    # check if snake eats food
    if head == food:
        score += 1
        # level up every 3 points
        if score % 3 == 0:
            level += 1
            speed += 2
        # new random food
        food = [random.randrange(0, WIDTH // CELL_SIZE) * CELL_SIZE,
                random.randrange(0, HEIGHT // CELL_SIZE) * CELL_SIZE]
    else:
        snake.pop()  # remove tail if not eating

    # check wall collision
    if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
        pygame.quit()
        sys.exit()

    # check self collision
    if head in snake[1:]:
        pygame.quit()
        sys.exit()

    # draw everything
    screen.fill(BLACK)
    draw_snake(snake)
    draw_food(food)
    show_info(score, level)

    pygame.display.update()
    clock.tick(speed)
