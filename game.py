import pygame, sys
import random
from pygame.locals import *
from objects import Bird, Pipe


pygame.init()
pygame.display.set_caption('Flappy Bird')

#music
mario = pygame.mixer.music.load('supermario.mp3')
pygame.mixer.music.play(-1, 0.0)

#clock
clock = pygame.time.Clock()
time_pipe1 = 0
time_pipe2 = 0


background = pygame.image.load('background.png')
background_size = background.get_size()
background_rect = background.get_rect()

surface = pygame.display.set_mode(background_size)
surface.blit(background, (0,0))

#groups
pipegroup = pygame.sprite.Group()

#initialize objects

bird = Bird()
pipe1 = Pipe(350, random.randint(-150, 0))
pipe2 = Pipe(550, random.randint(-150, 0))

def checkCollision(obj1, obj2):
	return obj1.rect.colliderect(obj2.rect)

#game loop
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	dt = clock.tick()
	time_pipe1 += dt
	time_pipe2 += dt

	if time_pipe1 > 3500:
		pipe1.reset()
		time_pipe1 = 0

	if time_pipe2 > 4800:
		pipe2.reset(525)
		time_pipe2 = 0

	bird.move()
	pipe1.move()
	pipe2.move()

	collision = checkCollision(bird, pipe1)

	if collision:
		print('crash')


	surface.blit(background, (0,0))

	bird.draw(surface, collision)
	pipe1.draw(surface)
	pipe2.draw(surface)

	pygame.display.update()
