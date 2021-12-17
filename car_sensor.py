import pygame
from math import sin, cos, radians

class Sensor():
	def __init__(self, angle):
		self.image = pygame.Surface([5,5])
		self.image.fill((255,0,0))
		self.rect = self.image.get_rect()
		self.angle = angle
		self.space = 10
		self.jump_num = 100

	def update(self):
		center = self.rect.center
		self.rect.centerx += self.space*cos(radians(self.angle))
		self.rect.centery += self.space*sin(radians(self.angle))


