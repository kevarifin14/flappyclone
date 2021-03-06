import pygame, sys, random, pyganim
from pygame.locals import *
from objects import Bird, Pipe, Top, Bottom

pygame.init()
pygame.display.set_caption('Flappy Bird')

#images
bird_img0 = pygame.image.load('flappy.gif')
bird_img1 = pygame.transform.rotate(bird_img0, 5)
bird_img2 = pygame.transform.rotate(bird_img0, 10)
bird_img3 = pygame.transform.rotate(bird_img0, 15)

#animation
animBird = pyganim.PygAnimation([(bird_img0,0.2),(bird_img1,0.2),(bird_img2,0.2),(bird_img3,0.2)])
animBird.play()

#colors
black = (0,0,0)
white = (255,255,255)
green = (0, 200, 0)
bright_green = (0, 255, 0)

#text
largeText = pygame.font.Font('freesansbold.ttf', 50)
smallText = pygame.font.Font('freesansbold.ttf', 20)

def setup():
	"""Initialize game variable"""
	global score,pipes, bird, top, bottom, top2, bottom2
		
	# objects
	position = random.randint(-275,-50)
	bird = Bird()
	top = Top(350, position)
	bottom = Bottom(350, position+440)
	position2 = random.randint(-275,-50)
	top2 = Top(350, position)
	bottom2 = Bottom(350, position+440)

	#groups
	pipes = pygame.sprite.Group()
	pipes.add(top, bottom, top2, bottom2)
	score = 0

def text_objects(text, font):
	"""Creates text objects"""
	textSurface = font.render(text, True, black)
	return textSurface, textSurface.get_rect()

def button(action,msg,x,y,w,h,i,a):
	"""
	Takes in button action and message along with dimension
	to create an interative button
	"""
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()

	if x+w > mouse[0] > x and y+h > mouse[1] > y:
		pygame.draw.rect(surface, a, (x,y,w,h))
		if click[0] == 1:
			if action == "start":
				game_loop()
			elif action == "reset":
				setup()
				game_loop()
	else:
		pygame.draw.rect(surface, i, (x,y,w,h))

	startSurf, startRect = text_objects(msg, smallText)
	startRect.center = ((x+w/2), (y+h/2))
	surface.blit(startSurf, startRect)

def game_intro():
	"""Flappy bird menu screen"""
	intro = True

	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		TextSurf, TextRect = text_objects("Flappy Bird", largeText)
		TextRect.center = ((350/2),(450/2))
		surface.blit(TextSurf, TextRect)

		button("start","Start",50,365,100,40,green,bright_green)

		pygame.display.update()

def game_end():

	stop = True

	while stop:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		button("reset", "Reset", 125, 205, 100,40,green, bright_green)

		pygame.display.update()

def cycle_pipes(top, bottom):
	"""
	Checks if pipes have reached the end of the screen
	and if so it moves them back to the beginning position
	"""
	global score
	if top.x == -53 and bottom.x == -53:
		position = random.randint(-275, -50)
		top.reset(y=position)
		bottom.reset(y=position+440)
		score += 1

def refresh_display():
	surface.blit(background, (0,0))
	pipes.draw(surface)		
	bird.draw(surface)

	scoreSurf, scoreRect = text_objects(str(score), smallText)
	scoreRect.center = ((175), 10)
	surface.blit(scoreSurf, scoreRect)


def game_loop():
	mainloop = True
	pause = True
	score = 1
	while mainloop:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN and bird.alive:
				if event.key == K_SPACE:
					bird.up()
					pygame.display.update()

		#reset pipes
		cycle_pipes(top, bottom)
		cycle_pipes(top2, bottom2)

		#check if bird is still flappin'
		bird.check_fly(game_end)

		#move birdy if it's alive
		if bird.alive:
			top.move()
			bottom.move()
			if top.x<(350/2-53/2) and bottom.x<(350/2-53/2) and pause:
				pause = False
			if not pause:
				top2.move()
				bottom2.move()
			bird.down()

		#check if bird hit a pipe
		collision = checkCollision(bird, top, bottom) or checkCollision(bird, top2, bottom2)
		#collision = False
		bird.die(surface,collision,game_end,mainloop)



		#redraw background and objects
		refresh_display()

		pygame.display.update()

def checkCollision(obj1, obj2, obj3):
	return pygame.sprite.collide_rect(obj1, obj2) or pygame.sprite.collide_rect(obj1, obj3)

#music
#mario = pygame.mixer.music.load('supermario.mp3')
#pygame.mixer.music.play(-1, 0.0)


background = pygame.image.load('background.png')
background_size = background.get_size()
background_rect = background.get_rect()

surface = pygame.display.set_mode(background_size)
surface.blit(background, (0,0))


setup()
game_intro()

