import pygame
from pygame.math import Vector2
from pygame.locals import K_LEFT, K_RIGHT, K_UP, K_DOWN, K_SPACE
from math import sin, cos, radians
from rna import Network
from car_sensor import Sensor
from globals import *

class Car(pygame.sprite.Sprite):
	def __init__(self, pos=(150,500), parents_weights=list()):
		super().__init__()
		self.image = pygame.transform.smoothscale(pygame.image.load('img/car.png').convert_alpha(), (2400/60, 1190/60))
		self.original_image = self.image
		self.rect = self.image.get_rect()
		self.mask = pygame.mask.from_surface(self.image)
		screen = pygame.display.get_surface()
		self.screen = screen.get_rect()
		self.position = Vector2(pos)
		self.direction = Vector2(1, 0)
		self.speed = 0
		self.angle_speed = 0
		self.angle = 0

		self.brain = Network([10, 2, 2, 4])
		self.sensors = [Sensor(90)]

	def update(self): # updating values
		if self.angle_speed != 0:
			# Rotate the direction vector and then the image.
			self.direction.rotate_ip(self.angle_speed)
			self.angle += self.angle_speed
			self.image = pygame.transform.rotate(self.original_image, -self.angle)
			self.rect = self.image.get_rect(center=self.rect.center)
		# Update the position vector and the rect.
		self.position += self.direction * self.speed
		self.rect.center = self.position

		for sensor in self.sensors:
			sensor.angle = self.angle
			sensor.update()

	def move(self, li):
		self.angle_speed = 0
		if li[K_LEFT]:
			self.angle_speed = -5
		elif li[K_RIGHT]:
			self.angle_speed = 5
		elif li[K_UP]:
			self.speed += 1
		elif li[K_DOWN]:
			self.speed -= 1
