import pygame, os, datetime, sys
from player import Player
from menu import Start_menu
from data import image_start, screen

WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
clock = pygame.time.Clock()
pygame.init()

# konkretyzacja obiektu
player = Player('hero_1', WIDTH, HEIGHT)
current_level = Start_menu(player, image_start, 'Start_menu')
player.level = current_level

# pętla menu
while player.window_open:
    
    # pętla zdarzeń 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            player.window_open = False
        elif event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            player.screen_width, player.screen_height = event.w, event.h
            current_level.resize(screen, event.w, event.h)

        player.get_events(event)
        player.level.get_events(event)

    # rysowanie i aktualizacja obiektów
    player.level.draw(screen)
    player.draw(screen)
    player.level.update()
    player.update()

    # aktualizacja okna pygame
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
