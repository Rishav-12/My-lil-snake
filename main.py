# PLease read the README for instructions
import pygame
import random
from math import sqrt
import os
pygame.init()

screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Snakes")
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

if not os.path.exists("highScore.txt"):
	with open("highScore.txt", "w") as file:
		file.write("0")

with open("highScore.txt", "r") as file:
		hiscore = int(file.read())

running = True
gameover = False

while running:
	if gameover:
		game_over()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				with open("highScore.txt", "w") as file:
					file.write(str(hiscore))
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

		if score_value >= 100:
			init_vel = 6
		if score_value >= 150:
			init_vel = 7
		if score_value >= 200:
			init_vel = 8
		if score_value >= 250:
			init_vel = 9
		if score_value >= 300:
			init_vel = 10
		if score_value >= 330:
			init_vel = 11
		if score_value >= 360:
			init_vel = 12
		if score_value >= 390:
			init_vel = 13
		if score_value >= 420:
			init_vel = 14
		if score_value >= 450:
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

		if score_value > hiscore:
			hiscore = score_value

		score_hiscore = font.render(f"Score: {score_value}  High Score: {hiscore}", True, black)
		screen.blit(score_hiscore, (5, 5))
		plot_snake()
		pygame.draw.rect(screen, red, [foodX, foodY, food_size, food_size])

	pygame.display.update()
