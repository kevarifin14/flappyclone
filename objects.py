import pygame, sys, random, pyganim


background = pygame.image.load('background.png')


class Bird(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		"""Construct your birdy!"""
		self.img = pygame.image.load('flappy.gif')

		bird_img0 = pygame.image.load('flappy.gif')
		bird_img1 = pygame.transform.rotate(bird_img0, 5)
		bird_img2 = pygame.transform.rotate(bird_img0, 10)
		bird_img3 = pygame.transform.rotate(bird_img0, 15)
		self.image = pyganim.PygAnimation([(bird_img0,0.2)])

		die1 = self.img
		die2 = pygame.transform.rotate(die1, 350)
		die3 = pygame.transform.rotate(die1, 340)
		die4 = pygame.transform.rotate(die1, 330)
		die5 = pygame.transform.rotate(die1, 320)
		die6 = pygame.transform.rotate(die1, 310)
		die7 = pygame.transform.rotate(die1, 300)
		die8 = pygame.transform.rotate(die1, 290)
		die9 = pygame.transform.rotate(die1, 280)
		die10 = pygame.transform.rotate(die1, 270)
		self.animDie = pyganim.PygAnimation([(die1,0.15),(die2,0.15),(die3,0.15),(die4,0.15),(die5,0.15),(die6,0.15),(die7,0.15),(die8,0.15),(die9,0.15),(die10,0.15	)],loop=False)

		fly1 = self.img


		self.image.play()
		#self.img_normal = self.image
		#self.img_up = pygame.transform.rotate(self.image, 20)
		#self.img_down = pygame.transform.rotate(self.image, 290)
		#self.img_dead = pygame.transform.rotate(self.image, 270)
		self.alive = True
		#initial position
		self.x = 10
		self.y = 225
		#self.rect = pygame.Rect(self.x, self.y, 10, 10)
		self.rect = self.img.get_rect()
		self.rect.x = self.x
		self.rect.y = self.y
		self.rect.width -= 10
		self.rect.height -= 10

	def die(self, surface,collision, menu, mainloop):
		if collision:
			self.image = self.animDie
			self.image.play()
			self.alive = False
			#self.image = self.img_dead
			if self.y <= 410:
				self.y += 1.75
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
		self.image.blit(surface, (self.x, self.y))


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

