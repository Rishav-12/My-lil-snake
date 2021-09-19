# Please read the README for instructions
import pygame
import random
import os

#--Setup--
pygame.init()
S_WIDTH, S_HEIGHT = 480, 480
screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
pygame.display.set_caption("Snakes")
font = pygame.font.Font("MICROSS.TTF", 30)
over_font = pygame.font.Font("MICROSS.TTF", 60)
clock = pygame.time.Clock()

#--Global variables--
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)

#--Game-specific variables--
snakeX = 150
snakeY = 150
snk_size = 15
init_vel = 15
velX = 0
velY = 0

food_size = 15
score_value = 0
direction = ""

def plot_snake():
	for i, coord in enumerate(snk_list):
		if i == len(snk_list) - 1:
			pygame.draw.rect(screen, green, [coord[0], coord[1], snk_size, snk_size])
		else:
			pygame.draw.rect(screen, black, [coord[0], coord[1], snk_size, snk_size])

def get_food_coords():
	foodX = random.randint(15, S_WIDTH-1)
	foodX = foodX - (foodX % 15)

	foodY = random.randint(15, S_HEIGHT-1)
	foodY = foodY - (foodY % 15)

	return foodX, foodY

def is_food_eaten(x1, y1, x2, y2):
	if x1 == x2 and y1 == y2:
		return True

def game_over():
	velX = 0
	velY = 0
	over_text = over_font.render(f"Game Over", True, red)
	screen.blit(over_text, (90, 190))

foodX, foodY = get_food_coords()
snk_list = []
snk_len = 1

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
		clock.tick(10)

		head = []
		head.append(snakeX)
		head.append(snakeY)
		snk_list.append(head)

		if len(snk_list) > snk_len:
			del snk_list[0]

		if is_food_eaten(snakeX, snakeY, foodX, foodY):
			score_value += 10
			foodX, foodY = get_food_coords()
			snk_len += 1

		# Check collision with walls
		if snakeX < 0 or snakeX > S_WIDTH or snakeY < 0 or snakeY > S_HEIGHT:
			gameover = True

		# Check if the snake runs into itself
		if head in snk_list[:-1]:
			gameover = True

		if score_value > hiscore:
			hiscore = score_value

		score_hiscore = font.render(f"Score: {score_value}  High Score: {hiscore}", True, black)
		screen.blit(score_hiscore, (5, 5))
		plot_snake()
		pygame.draw.rect(screen, red, [foodX, foodY, food_size, food_size])

	pygame.display.update()
