import pygame
from pygame.locals import K_LEFT, K_RIGHT, K_UP, K_DOWN, K_SPACE
from math import sin, cos, radians
from ai import AI
from car_sensor import Sensor
from globals import *

class Car(pygame.sprite.Sprite):
	def __init__(self, parents_weights=list()):
		super().__init__()
		self.og_image = pygame.transform.smoothscale(pygame.image.load('img/car.png').convert_alpha(), (2400/40, 1190/40))
		self.image = self.og_image
		self.rect = self.image.get_rect()
		self.mask = pygame.mask.from_surface(self.image)
		screen = pygame.display.get_surface()
		self.screen = screen.get_rect()
		self.rect.x, self.rect.y = 200, self.screen.centery-100
		self.angle = 0
		self.change_angle = 0
		self.v = 0.2

		self.score = INITIAL_SCORE
		self.brain = AI(10, 2, 5, 4)
		self.sensors = [Sensor(90)]

	def update(self): # updating values
		self.rect.x += self.v * sin(radians(self.angle+90))
		self.rect.y += self.v * cos(radians(self.angle+90))

		for sensor in self.sensors:
			sensor.angle = self.angle
			sensor.update()

	def rot(self): # rotating sprite
		self.image = pygame.transform.rotate(self.og_image, self.angle)
		self.angle += self.change_angle
		self.angle = self.angle % 360
		self.rect = self.image.get_rect(center=self.rect.center)

	def accelerate(self): # accelerate the car
		self.v += 1  if self.v < 10 else 0

	def brake(self): # brake the car
		self.v -= 1 if self.v > 0 else 0

	def move(self, li):
		"""========================= Player movements"""
		self.change_angle = 0
		if li[K_LEFT]:
			self.change_angle = 10
		elif li[K_RIGHT]:
			self.change_angle = -10
		elif li[K_UP]:
			self.accelerate()
		elif li[K_DOWN]:
			self.brake()
		self.rot()
		"""============================ """
		if li == 'left': self.change_angle = 10
		if li == "right": self.change_angle = -10
		if li == "accelerate": self.accelerate()
		if li == "brake": self.brake()
		self.rot()
