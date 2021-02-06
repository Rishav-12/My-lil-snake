import pygame
import random
from math import sqrt
pygame.init()

screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Beetle Game")
font = pygame.font.Font("MICROSS.TTF", 30)
over_font = pygame.font.Font("MICROSS.TTF", 60)

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

snakeX = 250
snakeY = 200
snk_size = 15
init_vel = 5
velX = 0
velY = 0

snk_list = []
snk_len = 1

foodX = random.randint(0, 560)
foodY = random.randint(0, 460)
food_size = 15
score_value = 0
direction = ""
clock = pygame.time.Clock()

def plot_snake():
	for coord in snk_list:
		pygame.draw.rect(screen, black, [coord[0], coord[1], snk_size, snk_size])

def iscollision(x1, y1, x2, y2):
	dist = sqrt((x2 - x1)**2 + (y2 - y1)**2)
	if dist < 10:
		return True

def game_over():
	velX = 0
	velY = 0
	over_text = over_font.render(f"Game Over", True, red)
	screen.blit(over_text, (150, 210))

running = True
gameover = False

while running:
	if gameover:
		game_over()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
	else:
		screen.fill(white)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT and direction != "right":
					velX = -init_vel
					velY = 0
					direction = "left"
				if event.key == pygame.K_RIGHT and direction != "left":
					velX = init_vel
					velY = 0
					direction = "right"
				if event.key == pygame.K_UP and direction != "down":
					velY = -init_vel
					velX = 0
					direction = "up"
				if event.key == pygame.K_DOWN and direction != "up":
					velY = init_vel
					velX = 0
					direction = "down"

		snakeX += velX
		snakeY += velY
		clock.tick(30)

		head = []
		head.append(snakeX)
		head.append(snakeY)
		snk_list.append(head)

		if len(snk_list) > snk_len:
			del snk_list[0]

		if score_value >= 120:
			init_vel = 8
		if score_value >= 200:
			init_vel = 10
		if score_value >= 280:
			init_vel = 12
		if score_value >= 350:
			init_vel = 15

		if iscollision(snakeX, snakeY, foodX, foodY):
			score_value += 10
			foodX = random.randint(0, 560)
			foodY = random.randint(0, 460)
			snk_len += 5
		
		if snakeX < 0 or snakeX > 600 or snakeY < 0 or snakeY > 500:
			gameover = True

		if head in snk_list[:-1]:
			gameover = True

		score = font.render(f"Score: {score_value}", True, black)
		screen.blit(score, (5, 5))
		plot_snake()
		pygame.draw.rect(screen, red, [foodX, foodY, food_size, food_size])

	pygame.display.update()