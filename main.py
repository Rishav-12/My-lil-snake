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

class Snake():
	"""
	defines the snake
	"""
	def __init__(self):
		self.x = 150
		self.y = 150
		self.size = 15
		self.init_vel = 15
		self.velx = 0
		self.vely = 0
		self.list = []
		self.len = 1
		self.head = []

	def draw(self):
		for i, coord in enumerate(self.list):
			if i == len(self.list) - 1:
				pygame.draw.rect(screen, green, [coord[0], coord[1], self.size, self.size])
			else:
				pygame.draw.rect(screen, black, [coord[0], coord[1], self.size, self.size])

	def update(self):
		self.x += self.velx
		self.y += self.vely
		self.head.append(self.x)
		self.head.append(self.y)
		self.list.append(self.head)

		if len(self.list) > self.len:
			del self.list[0]


#--Game-specific variables--
food_size = 15
score_value = 0
direction = ""


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

if not os.path.exists("highScore.txt"):
	with open("highScore.txt", "w") as file:
		file.write("0")

with open("highScore.txt", "r") as file:
	hiscore = int(file.read())

running = True
gameover = False

snake = Snake()

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
					snake.velx = -snake.init_vel
					snake.vely = 0
					direction = "left"
				if event.key == pygame.K_RIGHT and direction != "left":
					snake.velx = snake.init_vel
					snake.vely = 0
					direction = "right"
				if event.key == pygame.K_UP and direction != "down":
					snake.vely = -snake.init_vel
					snake.velx = 0
					direction = "up"
				if event.key == pygame.K_DOWN and direction != "up":
					snake.vely = snake.init_vel
					snake.velx = 0
					direction = "down"

		snake.update()
		clock.tick(10)

		# Check collision with walls
		if snake.x < 0 or snake.x > S_WIDTH or snake.y < 0 or snake.y > S_HEIGHT:
			gameover = True

		# Check if the snake runs into itself
		if snake.head in snake.list[:-1]:
			gameover = True

		if is_food_eaten(snake.x, snake.y, foodX, foodY):
			score_value += 10
			foodX, foodY = get_food_coords()
			snake.len += 1

		if score_value > hiscore:
			hiscore = score_value

		score_hiscore = font.render(f"Score: {score_value}  High Score: {hiscore}", True, black)
		screen.blit(score_hiscore, (5, 5))
		snake.draw()
		pygame.draw.rect(screen, red, [foodX, foodY, food_size, food_size])

	pygame.display.update()
