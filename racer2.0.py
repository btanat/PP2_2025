# Imports
import pygame, sys
from pygame.locals import *
import random, time
 
# Initializing pygame
pygame.init()
 
# Frame rate
FPS = 60
FramePerSec = pygame.time.Clock()
 
# Colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
# Screen settings
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5           # Base enemy speed
SCORE = 0           # How many enemies passed
COINS = 0           # Total collected coins
 
# Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
 
background = pygame.image.load("PygameTutorial//AnimatedStreet.png")
 
# Window
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
 
 
# ---------------------------- ENEMY CLASS ----------------------------
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("PygameTutorial//Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
 
    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)

        # Respawn enemy when it goes off screen
        if self.rect.top > 600:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
 
 
# ---------------------------- PLAYER CLASS ----------------------------
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("PygameTutorial//Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)

        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
 
 
# ---------------------------- COIN CLASS ----------------------------
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Randomly choose coin type
        coin_type = random.choice(["bronze", "silver", "gold"])

        # Assign value & image based on type
        if coin_type == "bronze":
            self.value = 1
            img = "PygameTutorial//CoinBronze.jpg"
        elif coin_type == "silver":
            self.value = 3
            img = "PygameTutorial//CoinSilver.jpg"
        else:
            self.value = 5
            img = "PygameTutorial//CoinGold.png"

        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (45, 45))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
 
    def move(self):
        self.rect.move_ip(0, SPEED // 2)

        # Respawn above screen
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
 
 
# ---------------------------- SPRITE SETUP ----------------------------
P1 = Player()
E1 = Enemy()
C1 = Coin()
 
enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, C1)
 
# Speed increase event every second
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
 
 
# ---------------------------- GAME LOOP ----------------------------
while True:
    for event in pygame.event.get():
        # Gradually increase speed
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
    # Draw background
    DISPLAYSURF.blit(background, (0,0))

    # Score & coins display
    scores = font_small.render("Score: " + str(SCORE), True, BLACK)
    coins_text = font_small.render("Coins: " + str(COINS), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    DISPLAYSURF.blit(coins_text, (300,10))
 
    # ----------------- COIN COLLECTION LOGIC -----------------
    collected = pygame.sprite.spritecollide(P1, coins, False)
    for coin in collected:
        COINS += coin.value
        pygame.mixer.Sound('PygameTutorial//coin.mp3').play()

        # Increase speed every 10 coins
        if COINS % 10 == 0:
            SPEED += 1

        # Respawn coin
        coin.rect.top = 0
        coin.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
 
    # Move all sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
 
    # ----------------- COLLISION WITH ENEMY -----------------
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('PygameTutorial//crash.wav').play()
        time.sleep(0.5)
                    
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30,250))
        pygame.display.update()

        for entity in all_sprites:
            entity.kill()

        time.sleep(2)
        pygame.quit()
        sys.exit()
         
    pygame.display.update()
    FramePerSec.tick(FPS)
