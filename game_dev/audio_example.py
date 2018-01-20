
import pygame, sys
from pygame.locals import *
import numpy
import time

WAV_FILE = 'song.wav'

pygame.init()
pygame.display.set_caption('audio example')
screen = pygame.display.set_mode((400, 400))

audio = pygame.mixer.Sound(WAV_FILE)
audio.play(-1)

while True:
	sys_font = pygame.font.SysFont("None", 19)
	rendered = sys_font.render(WAV_FILE, 0, (255, 100, 100))
	screen.blit(rendered, (100, 100))

	for event in pygame.event.get():
		if event.type == QUIT:
			audio.stop()
			pygame.quit()
			sys.exit()

	pygame.display.update()


