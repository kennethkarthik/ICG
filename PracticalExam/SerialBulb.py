import pygame

black = (0, 0, 0)
white = (255, 255, 255)
blue = (73, 188, 244)
red = (235, 32, 47)
green = (126, 199, 81)
yellow = (249, 216, 32)

def main():
	screen.fill(black)

	pygame.draw.line(screen, white, (0, 350), (1000, 350),5)

	pygame.draw.line(screen, white, (120, 350), (120, 380), 5)
	pygame.draw.circle(screen, green, (120,446),56,0)
	pygame.draw.rect(screen, white, (85, 380, 70, 25), 0)

	pygame.draw.line(screen, white, (120+180, 350), (120+180, 380), 5)
	pygame.draw.circle(screen, red, (120+180,446),56,0)
	pygame.draw.rect(screen, white, (85+180, 380, 70, 25), 0)

	pygame.draw.line(screen, white, (120+180+180, 350), (120+180+180, 380), 5)
	pygame.draw.circle(screen, blue, (120+180+180,446),56,0)
	pygame.draw.rect(screen, white, (85+180+180, 380, 70, 25), 0)

	pygame.draw.line(screen, white, (120+180+180+180, 350), (120+180+180+180, 380), 5)
	pygame.draw.circle(screen, yellow, (120+180+180+180,446),56,0)
	pygame.draw.rect(screen, white, (85+180+180+180, 380, 70, 25), 0)

	pygame.draw.line(screen, white, (120+180+180+180+180, 350), (120+180+180+180+180, 380), 5)
	pygame.draw.circle(screen, green, (120+180+180+180+180,446),56,0)
	pygame.draw.rect(screen, white, (85+180+180+180+180, 380, 70, 25), 0)
	

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		pygame.display.update()


if __name__ == "__main__":

	pygame.init()
	size = [1000, 700]
	screen = pygame.display.set_mode(size)

	main()
	pygame.quit()