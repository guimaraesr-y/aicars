import pygame, sys, os, random
from car import *
from globals import *

class Game:
	def __init__(self, parents_weights=list()):
		os.environ['SDL_VIDEO_CENTERED'] = '1'
		pygame.init()
		self.info = pygame.display.Info()
		self.screen_width, self.screen_height = self.info.current_w-50, self.info.current_h-100
		self.screen = pygame.display.set_mode([self.screen_width, self.screen_height], pygame.RESIZABLE)

		self.clock = pygame.time.Clock()
		self.running = True
		self.bg = Background(self)

		self.cars = pygame.sprite.Group()
		self.all_sprites = pygame.sprite.Group(self.bg)
		self.dead_cars = pygame.sprite.Group()


		if CURRENT_GEN == 0:
			for i in range(CARS_BY_GEN):
				self.cars.add(Car())
		else:
			for i in range(CARS_BY_GEN):
				self.cars.add(Car(parents_weights))

	def detect_collision(self, g, g_target):
		for car in pygame.sprite.spritecollide(g, g_target, True, collided=lambda spr1, spr2: pygame.sprite.collide_mask(spr1, spr2)):
			self.dead_cars.add(car)

	def run(self):
		while self.running:
			presses = pygame.key.get_pressed()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						self.running = False

			for x in self.cars:
				x.move(presses)

			self.screen.fill(BLACK) 

			self.all_sprites.draw(self.screen)
			self.all_sprites.update()

			self.cars.draw(self.screen)
			self.cars.update()

			self.clock.tick(FPS)
			pygame.display.flip()

class Background(pygame.sprite.Sprite):
	def __init__(self, game):
		super().__init__()
		self.image = pygame.transform.smoothscale(pygame.image.load('img/background.png').convert_alpha(), (game.screen_width, game.screen_height))
		pygame.Surface.set_colorkey(self.image, (0,0,0))
		self.rect = self.image.get_rect()
		self.screen = game.screen.get_rect()
		self.rect.center = self.screen.center
		self.mask = pygame.mask.from_surface(self.image)
		self.game = game

	def update(self):
		game.detect_collision(self.game.bg, self.game.cars) # colisão do carro com as paredes da pista

if __name__=='__main__':
	game = Game()
	game.run()
