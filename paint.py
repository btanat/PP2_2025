import pygame
import sys

pygame.init()

# --- Setup ---
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Paint App")

# --- Colors ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

current_color = BLACK   # default color
brush_size = 10
tool = "brush"          # can be "brush", "rect", "circle", "eraser"

screen.fill(WHITE)
drawing = False
start_pos = None

font = pygame.font.SysFont("Arial", 20)

def draw_text(text, x, y):
    txt = font.render(text, True, BLACK)
    screen.blit(txt, (x, y))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Mouse pressed → start drawing
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos

            # Right-click = erase
            if event.button == 3:
                tool = "eraser"

        # Mouse released → stop drawing
        if event.type == pygame.MOUSEBUTTONUP:
            if tool == "rect":
                end_pos = event.pos
                rect = pygame.Rect(start_pos, (end_pos[0]-start_pos[0], end_pos[1]-start_pos[1]))
                pygame.draw.rect(screen, current_color, rect, 2)
            elif tool == "circle":
                end_pos = event.pos
                radius = int(((end_pos[0]-start_pos[0])**2 + (end_pos[1]-start_pos[1])**2)**0.5)
                pygame.draw.circle(screen, current_color, start_pos, radius, 2)
            drawing = False

        # Keyboard control
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                tool = "brush"
            if event.key == pygame.K_r:
                tool = "rect"
            if event.key == pygame.K_c:
                tool = "circle"
            if event.key == pygame.K_e:
                tool = "eraser"

            # color change
            if event.key == pygame.K_1:
                current_color = BLACK
            if event.key == pygame.K_2:
                current_color = RED
            if event.key == pygame.K_3:
                current_color = GREEN
            if event.key == pygame.K_4:
                current_color = BLUE

    # When mouse moves and drawing = True
    if drawing and tool == "brush":
        pygame.draw.circle(screen, current_color, pygame.mouse.get_pos(), brush_size)
    if drawing and tool == "eraser":
        pygame.draw.circle(screen, WHITE, pygame.mouse.get_pos(), brush_size)

    # UI text
    pygame.draw.rect(screen, WHITE, (0, 0, WIDTH, 30))
    draw_text(f"Tool: {tool.upper()} | Color: {current_color} | Keys: [B]rush [R]ect [C]ircle [E]raser | Colors: 1=Black 2=Red 3=Green 4=Blue", 10, 5)

    pygame.display.update()
