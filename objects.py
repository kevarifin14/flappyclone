import pygame
import random
import time


class Bird(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		"""Construct your birdy!"""
		self.image = pygame.image.load('flappy.gif')
		self.img_normal = self.image
		self.img_up = pygame.transform.rotate(self.image, 20)
		self.img_down = pygame.transform.rotate(self.image, 290)
		self.img_dead = pygame.transform.rotate(self.image, 270)
		self.alive = True
		#initial position
		self.x = 10
		self.y = 225
		#self.rect = pygame.Rect(self.x, self.y, 10, 10)
		self.rect = self.image.get_rect()
		self.rect.x = self.x
		self.rect.y = self.y
		self.rect.width -= 10
		self.rect.height -= 10

	def die(self, collision, menu, mainloop):
		if collision:
			self.alive = False
			self.image = self.img_dead
			if self.y <= 410:
				self.y += 1.5
			else:
				mainloop = False
				menu()

	def check_fly(self, menu):
		if self.y > 410:
			self.alive = False
			menu()

	def up(self):
		"""More Bird with space bar"""
		self.y -= 50
		self.rect.y -= 50
	
	def down(self):
		self.y += 1
		self.rect.y += 1
		#self.image = self.img_down
		
	def draw(self, surface):
		"""Draw bird""" 
		surface.blit(self.image, (self.x, self.y))


class Pipe(pygame.sprite.Sprite):
	
	def __init__(self, x_coord, y_coord):
		pygame.sprite.Sprite.__init__(self)
		"""Constructs pipe obstruction"""
		self.image = pygame.image.load('pipes.png')
		self.x = x_coord
		self.x_original = x_coord
		self.y = y_coord
		self.y_original = y_coord
		#self.rect = pygame.Rect((self.x, self.y), (30, 40))	
		#self.rect = pygame.Rect(self.x+10, self.y, 45, 200)
		#define the rectangle
		self.rect = self.image.get_rect()

	def move(self):
		"""Moves pipe across screen"""
		self.x -= 1
		self.rect.x -= 1

	def draw(self, surface):
		"""Draw pipe on surface"""
		surface.blit(self.image, (self.x, self.y))

	def reset(self, x=350, y=0):
		self.x = x
		self.y = y
		self.rect.x = self.x
		self.rect.y = self.y


class Top(Pipe):
	"""Top half of the pipe obstacle"""
	def __init__(self, x__coord, y__coord):
		Pipe.__init__(self, x__coord, y__coord)
		#change the image
		self.image = pygame.image.load('top.png')
		self.rect = self.image.get_rect()
		self.rect.x = self.x
		self.rect.y = self.y
		self.rect.height = 310	

class Bottom(Pipe):
	"""Bottom half of the pipe obstacle"""
	def __init__(self, x__coord, y__coord):
		Pipe.__init__(self, x__coord, y__coord)
		#change the image
		self.image = pygame.image.load('bottom.png')
		self.rect = pygame.Rect(self.x, self.y, 45, 300)
		self.rect.width -= 20

