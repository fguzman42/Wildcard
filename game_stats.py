# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    game_stats.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fguzman <fguzman@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/21 14:12:47 by fguzman           #+#    #+#              #
#    Updated: 2020/02/21 14:24:38 by fguzman          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# This file contains the classes and methods used for the scoreboard, life left, and levels.

class  GameStats:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1