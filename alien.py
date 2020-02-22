# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    alien.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fguzman <fguzman@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/21 14:24:54 by fguzman           #+#    #+#              #
#    Updated: 2020/02/21 14:25:36 by fguzman          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# This file contains the class for the alien. The methods determine the alien speed and position

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load('sprites/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
    

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
       
    def update(self):
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x