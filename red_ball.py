import pygame

def init():
    icon = pygame.image.load("images/icon.png")
    pygame.display.set_icon(icon)

pygame.init()
init()

screen = pygame.display.set_mode((800, 600))

x = 400
y = 300

clock = pygame.time.Clock()

while True:
    screen.fill((255, 255, 255))
    
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 25)

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit(0)
            elif event.key == pygame.K_UP and y >= 40:
                y -= 20
            elif event.key == pygame.K_DOWN and y <= 560:
                y += 20
            elif event.key == pygame.K_LEFT and x >= 40:
                x -= 20
            elif event.key == pygame.K_RIGHT and x <= 760:
                x += 20
            

    clock.tick(60)
    pygame.display.update()