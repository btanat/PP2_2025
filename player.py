import pygame
import os
import random

_songs = [
    "songs/Dr. Dre - The Next Episode.mp3",
    "songs/Eminem - Lose Yourself.mp3",
    "songs/Eminem - Superman.mp3",
    "songs/Kelis - Milkshake.mp3",
    "songs/krasiva.mp3",
    "songs/party_up.mp3",
    "songs/Rihanna Feat. Eminem - Love The Way You Lie.mp3"
]

def play_next_song():
    global _songs
    _songs = _songs[1:] + [_songs[0]]
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()  
    print(f"Now playing: {_songs[0]}")

def play_previous_song():
    global _songs
    pygame.mixer.music.load(_songs[-1])
    pygame.mixer.music.play()  
    print(f"Now playing: {_songs[-1]}")



def init():
    icon = pygame.image.load("images/icon.png")
    pygame.display.set_icon(icon)

pygame.init()
pygame.mixer.init()
init()

screen = pygame.display.set_mode((500, 500))

play_next_song()

events = pygame.event.get()
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit(0)
            if event.key == pygame.K_RIGHT:
                play_next_song()
            if event.key == pygame.K_LEFT:
                play_previous_song()
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                    print("Music paused")
                else:
                    pygame.mixer.music.unpause()
                    print("Music resumed")
                    
                
                  