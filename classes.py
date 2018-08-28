#! /usr/bin/env python3
# coding: utf-8

import pygame
from pygame.locals import *
from constants import *
import random

# Class that generate the level
class Map:

    def __init__(self):

        # The map's file
        self.file = lvl_design
        # The map in the form of list
        self.structure = 0

    # Generate a lvl from the file
    def create(self):

        # Open the lvl file
        with open(self.file, 'r') as file:
            # Create a list of list
            structure_file = []

            for lign in file:
                lign_lvl = []

                # Each caracter will be a case of the grid
                for caracter in lign:
                    if caracter != "\n":
                        lign_lvl.append(caracter)

                structure_file.append(lign_lvl)

            self.structure = structure_file

    # Generate the lvl design
    def display(self, window):

        # Different sprite of the lvl design
        wall = pygame.image.load(image_wall).convert()
        start = pygame.image.load(image_start).convert()
        end = pygame.image.load(image_arrival).convert()

        lign_number = 0
        for lign in self.structure:

            case_number = 0
            for sprite in lign:
                # Add the corresponding sprite at the good place
                x = case_number * size_sprite
                y = lign_number * size_sprite
                if sprite == 'm':
                    window.blit(wall, (x, y))
                elif sprite == 'd':
                    window.blit(start, (x, y))
                elif sprite == 'a':
                    window.blit(end, (x, y))
                case_number += 1
            lign_number += 1


# Class that generate the character
class Character:

    def __init__(self, right, left, up, down,lvl):

        # Character's sprite
        self.right = pygame.image.load(right).convert_alpha()
        self.left = pygame.image.load(left).convert_alpha()
        self.up = pygame.image.load(up).convert_alpha()
        self.down = pygame.image.load(down).convert_alpha()

        # Initialization of the position on the grid
        self.x = 0
        self.y = 0

        # Initialization of the position on the design
        self.sprite_x = 0
        self.sprite_y = 0


        # Initialization of the direction
        self.direction = self.right

        # Character's deplacement
        def move(self, direction):

            if direction == 'right':
                # Test if the character will not go out of the screen
                if self.x < (nb_sprite - 1):
                    # Test if the destination is not a wall
                    if self.lvl.structure[self.y][self.x + 1] != 'm':
                        # Incrementing self.x by 1
                        self.x += 1
                        # Update the position on the interface
                        self.sprite_x = self.x * size_sprite
                # Update the direction on the interface
                self.direction = self.right

            if direction == 'left':
                if self.x > 0:
                    if self.lvl.structure[self.y][self.x - 1] != 'm':
                        self.x -= 1
                        self.sprite_x = self.x * size_sprite
                self.direction = self.left

            if direction == 'up':
                if self.y > 0:
                    if self.lvl.structure[self.y - 1][self.x] != 'm':
                        self.y -= 1
                        self.sprite_y = self.y * size_sprite
                self.direction = self.up

            if direction == 'down':
                if self.y < (nb_sprite - 1):
                    if self.lvl.structure[self.y + 1][self.x] != 'm':
                        self.y += 1
                        self.sprite_y = self.y * size_sprite
                self.direction = self.down




