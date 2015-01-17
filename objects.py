import pygame
import random

class Bird(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		"""Construct your birdy!"""
		self.image = pygame.image.load('flappy.gif')
		self.rect = self.image.get_rect()
		self.img_up = pygame.transform.rotate(self.image, 20)
		self.img_down = pygame.transform.rotate(self.image, 290)
		#initial position
		self.x = 10
		self.y = 225
		self.rect = (self.x, self.y, 50, 50)

	def move(self):
		"""More Bird with arrow keys"""
		key = pygame.key.get_pressed()
		if key[pygame.K_SPACE]:
			self.image = self.img_up
			if self.y < 10:
				self.y = self.y
				self.rect.y = self.rect.y
			else:
				self.y -= 2
				self.rect.y -= 2
		else:
			self.y += 0.5
			self.image = self.img_down
		self.rect = self.image.get_rect()
		
	def draw(self, surface, collision):
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
		self.rect = pygame.Rect(self.x, self.y, 124, 579)	

	def move(self):
		"""Moves pipe across screen"""
		self.x -= 1
		self.rect.x -=1

	def draw(self, surface):
		"""Draw pipe on surface"""
		surface.blit(self.image, (self.x, self.y))

	def reset(self, x=350):
		self.x = x
		self.y = random.randint(-100,0)


