import sys
import pygame
from setting import Settings
from ship import Ship

def run_game():
	pygame.init()
	demo = Settings()
	
	screen = pygame.display.set_mode((demo.screen_width,demo.screen_height))
	ship = Ship(screen)
	pygame.display.set_caption("Alien Invasion")
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		screen.fill(demo.bg_color)
		ship.blitme()
		pygame.display.flip()

run_game()