
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')

while True:
	sys_font = pygame.font.SysFont("None", 19)
	rendered = sys_font.render('Hello World', 0, (255, 100, 100))
	screen.blit(rendered, (100, 100))
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()




