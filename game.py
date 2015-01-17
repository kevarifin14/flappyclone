import pygame, sys
import random
from pygame.locals import *
from objects import Bird, Pipe, Top, Bottom


pygame.init()
pygame.display.set_caption('Flappy Bird')

#music
#mario = pygame.mixer.music.load('supermario.mp3')
#pygame.mixer.music.play(-1, 0.0)

#clock
clock = pygame.time.Clock()
time_pipe1 = 0


background = pygame.image.load('background.png')
background_size = background.get_size()
background_rect = background.get_rect()

surface = pygame.display.set_mode(background_size)
surface.blit(background, (0,0))

#groups
pipes = pygame.sprite.Group()

#initialize objects

position = random.randint(-275,-50)
bird = Bird()
top = Top(350, position)
bottom = Bottom(350, position+410)

pipes.add(top, bottom)

def checkCollision(obj1, obj2, obj3):
	return pygame.sprite.collide_rect(obj1, obj2) or pygame.sprite.collide_rect(obj1, obj3)

#game loop
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN and bird.alive:
			if event.key == K_SPACE:
				bird.up()



	dt = clock.tick()
	time_pipe1 += dt

	if time_pipe1 > 3500 and bird.alive:
		position = random.randint(-275, -50)
		top.reset(y=position)
		bottom.reset(y=position+410)
		time_pipe1 = 0

	
	bird.check_fly()

	if bird.alive:
		top.move()
		bird.down()
		bottom.move()


	collision = checkCollision(bird, top, bottom)
	bird.die(collision)

	surface.blit(background, (0,0))

	bird.draw(surface)
	pipes.draw(surface)

	pygame.display.update()
