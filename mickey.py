import pygame
import datetime
import math

def init():
    icon = pygame.image.load("C://Users//Батыр//Desktop//PP2_2025//week7/images//mickey.png")
    pygame.display.set_icon(icon)

pygame.init()
init()

screen = pygame.display.set_mode((900, 800))

mickey = pygame.image.load("C://Users//Батыр//Desktop//PP2_2025//week7/images//mickey_norm.png")
minute_hand = pygame.image.load("C://Users//Батыр//Desktop//PP2_2025//week7/images//minute.png")
second_hand = pygame.image.load("C://Users//Батыр//Desktop//PP2_2025//week7/images//second.png")

mickey = pygame.transform.scale(mickey, (900, 800))
minute_hand = pygame.transform.scale(minute_hand, (800, 800))
second_hand = pygame.transform.scale(second_hand, (800, 800))

x = 450
y = 400

clock = pygame.time.Clock()

cnt = 0
while True:
    if cnt % 100 == 0:
        print(cnt)

    now = datetime.datetime.now()
    minute = now.minute
    second = now.second
    print(f"Time: {minute}:{second}")

    minute_angle = (-minute - 7) * 6
    second_angle = (-second + 8) * 6

    minute_rotated = pygame.transform.rotate(minute_hand, minute_angle)
    second_rotated = pygame.transform.rotate(second_hand, second_angle)

    minute_rect = minute_rotated.get_rect(center=(x, y))
    second_rect = second_rotated.get_rect(center=(x, y))
    
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit(0)
                
    screen.blit(mickey, (0, 0))
    screen.blit(minute_rotated, minute_rect)
    screen.blit(second_rotated, second_rect)
    
    pygame.display.update()
    clock.tick(60)
    cnt += 1