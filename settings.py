# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    settings.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fguzman <fguzman@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/21 14:13:02 by fguzman           #+#    #+#              #
#    Updated: 2020/02/21 14:24:41 by fguzman          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #



# This class is the settings that initialize the variables for the rest of my 
# classes used for rendering, scoreboard, highscore, ship settings, alien settings, etc.


class Settings:
	
	def __init__(self):
		self.screen_width = 1200
		self.screen_height =  1200
		self.bg_color = (255, 105, 180)
		self.ship_limit = 3
		self.bullet_width = 15
		self.bullet_height = 30
		self.bullet_color = (51, 30, 65)
		self.bullets_allowed = 1000
		self.fleet_drop_speed = 25
		self.speedup_scale = 1.1
		self.score_scale = 1.5
		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		self.ship_speed = 30
		self.bullet_speed = 50
		self.alien_speed = 40
		self.fleet_direction = 1
		self.alien_points = 50

	def increase_speed(self):
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale
		self.alien_points = int(self.alien_points * self.score_scale)