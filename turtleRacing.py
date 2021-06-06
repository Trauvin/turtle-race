import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'cyan', 'blue', 'yellow', 'brown', 'black', 'orange', 'purple', 'pink', 'green']


def get_number_of_racers():
	racers = 0
	while True:
		racers = input("Digite o número de corredores (2 - 10): ")
		if racers.isdigit():
			racers = int(racers)
		else:
			print("Entrada não é válida... Tente novamente.")
			continue

		if 2 <= racers <=10:
			return racers
		else:
			print("Número não está entre 2-10... Tente novamente.")

def race(colors):
	turtles = create_turtles(colors)

	while True:
		for racer in turtles:
			distance = random.randrange(1, 20)
			racer.forward(distance)

			x, y = racer.pos()
			if y >= HEIGHT // 2 - 10:
				return colors[turtles.index(racer)]

def create_turtles(colors):
	turtles = []
	spacingx = WIDTH // (len(colors) + 1)
	for i, color in enumerate(colors):
		racer = turtle.Turtle()
		racer.color(color)
		racer.shape('turtle')
		racer.left(90)
		racer.penup()
		# o valor de x mudará a cada execução do laço, y é constante
		# divide a largura por 2 para obter a parte negativa de x (-200)
		# e alinhar as tartarugas da esquerda para direita
		print(-WIDTH//2 + (i + 1) * spacingx)
		racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
		racer.pendown()
		turtles.append(racer)

	return turtles

def init_turtle():
	screen = turtle.Screen()
	screen.setup(WIDTH, HEIGHT)
	screen.title("Corrida de Tartaruga")

racers = get_number_of_racers()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers] # faz um match entre o número de participantes e as cores
winner = race(colors)
print("A vencedora é a tartaruga ", winner)