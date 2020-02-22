# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    bullet.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fguzman <fguzman@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/21 14:25:54 by fguzman           #+#    #+#              #
#    Updated: 2020/02/21 14:26:17 by fguzman          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# this file contains the class for our bullets the ship uses to destroy aliens. 

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y
        
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)