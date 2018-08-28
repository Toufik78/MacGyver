#!/usr/bin/python3

# -*- coding: Utf-8 -*


import pygame

from pygame.locals import *

from classes import *

from constants import *

pygame.init()

# Opening the Pygame window (square: width = height)

window = pygame.display.set_mode((windows_size, windows_size))
background = pygame.image.load(image_background).convert()
window.blit(background, (0,0))

#Loading  of the character

#perso = pygame.image.load(MacGyver).convert_alpha()

#position_perso = perso.get_rect()

#window.blit(perso, position_perso)

# Title

pygame.display.set_caption(window_title)

# BOUCLE PRINCIPALE
#Initialization of the program loop
prog = 1
game = 1

while prog:

    # Initialization of the lvl
    lvl = Map()
    lvl.create()
    # Initilization of the lvl design
    lvl.display(window)
    background = pygame.image.load(image_background).convert()

    # Initialization of the character
    mcGyver = Character(mcGyver_right, mcGyver_left,mcGyver_up, mcGyver_down, lvl)


    # Rafraichissement
    pygame.display.flip()


    # Game loop
    while game:

        # Limitation of the number of loop per second
        pygame.time.Clock().tick(30)
        # Rafraichissement
        pygame.display.flip()

        # Detection of events
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                prog = 0
                game = 0

                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        mcGyver.move('right')
                    elif event.key == K_LEFT:
                        mcGyver.move('left')
                    elif event.key == K_UP:
                        mcGyver.move('up')
                    elif event.key == K_DOWN:
                        mcGyver.move('down')

    # Rafraichissement

    # Affichages aux nouvelles positions

    window.blit(background, (0, 0))
    pygame.display.flip()
