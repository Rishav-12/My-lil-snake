import pygame
import random
from math import sqrt
pygame.init()

screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Beetle Game")
font = pygame.font.Font(None, 30)
over_font = pygame.font.Font(None, 60)

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
snakeX = 250
snakeY = 200
snk_len = 15
snk_width = 15
init_vel = 5
velX = 0
velY = 0
foodX = random.randint(0, 560)
foodY = random.randint(0, 460)
food_size = 15
score_value = 0
direction = ""
clock = pygame.time.Clock()

def iscollision(x1, y1, x2, y2):
	dist = sqrt((x2 - x1)**2 + (y2 - y1)**2)
	if dist < 15:
		return True

def game_over():
	velX = 0
	velY = 0
	over_text = over_font.render(f"Game Over", True, red)
	screen.blit(over_text, (180, 210))

running = True
gameover = False

while running:
	screen.fill(white)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN and not gameover:
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
	
	if snakeX <= 0 or snakeX >= 565 or snakeY <= 0 or snakeY >= 485:
		gameover = True
		game_over()

	score = font.render(f"Score: {score_value}", True, black)
	screen.blit(score, (5, 5))
	pygame.draw.rect(screen, black, [snakeX, snakeY, snk_len, snk_width])
	pygame.draw.rect(screen, red, [foodX, foodY, food_size, food_size])

	pygame.display.update()