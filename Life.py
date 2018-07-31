from random import randint
import time
import numpy


def dead_state(width, height):
	board = []

	for x in range(height):
		row = []
		for x in range(width):
			row.append(0)
		board.append(row)

	return board

def random_state(width, height):
	state = dead_state(width, height)

	for x in range(height):
		for y in range(width):
			state[x][y] = randint(0, 1)

	return state

def render(state):
	print(" ", end="")
	for cell in state[0]:
		print("-", end="")
	print()	


	for row in state:
		print("|", end="")
		for cell in row:
			if(cell == 1):
				print ("0", end="")
			else:
				print(" ", end="")

		print("|")
	print(" ", end="")
	for cell in state[0]:
		print("-", end="")
	print()

def next_board_state(state):
	live_count = 0
	new_state = dead_state(len(state[0]), len(state))

	

	for row in range(len(state)):
		for column in range(len(state[row])):
			live_count = 0


			#Check if cell is in top row
			if((row == 0)):
				#Cell in top right
				if(column == 0):
					live_count = live_count + state[row][column+1] + state[row+1][column+1] + state[row+1][column]
				#Cell in top left
				elif(column == (len(state[row]) - 1)):
					live_count = live_count + state[row+1][column] + state[row+1][column-1] + state[row][column-1]
				#Cell just in top row
				else:
					live_count = live_count + state[row][column+1] + state[row+1][column+1] + state[row+1][column] + state[row+1][column-1] + state[row][column-1]
			#Check if cell is in bottom row
			elif(row == (len(state) - 1)):
				#Cell in bottom left
				if(column == 0):
					live_count = live_count + state[row-1][column] + state[row][column+1] + state[row][column+1]
				#Cell in bottom right
				elif(column == (len(state[row]) - 1)):
					live_count = live_count + state[row-1][column] + state[row][column-1] + state[row-1][column-1]
				#Cell only in bottom row
				else:
					live_count = live_count + state[row][column-1] + state[row-1][column-1] + state[row-1][column] + state[row][column+1] + state[row][column+1]
			#If cell is on left side
			elif(column == 0):
				live_count = live_count + state[row-1][column] + state[row][column+1] + state[row-1][column+1] + state[row+1][column+1] + state[row+1][column]
			#Cell is on right side
			elif(column == (len(state[row]) - 1)):
				live_count = live_count + state[row-1][column] + state[row-1][column-1] + state[row][column-1] + state[row+1][column-1] + state[row+1][column]
			#Cell is not on boundary
			else:
				live_count = live_count + state[row-1][column-1] + state[row-1][column] + state[row-1][column+1] + state[row][column+1] + state[row+1][column+1] + state[row+1][column] + state[row+1][column-1] + state[row][column-1]

			
			#Reproduction	
			if(live_count == 3 and state[row][column] == 0):
				new_state[row][column] = 1
			#Underpopulation
			elif(live_count == 0 or live_count == 1):
				new_state[row][column] = 0
			#Ideal condition	
			elif((live_count == 2 or live_count == 3) and state[row][column] == 1):
				new_state[row][column] = 1
			#Overpopulation
			elif(live_count > 3):
				new_state[row][column] = 0

	return new_state

def load_board_state(file):
	theFile = open(file, 'r')
	state = []
	row = []

	for cell in theFile.read():
		if cell == '\n':
			state.append(row)
			row = []
			continue
		row.append(int(cell))

	state.append(row)

	return state



state = random_state(50, 30)
render(state)

while(True):
	state = next_board_state(state)
	render(state)
	time.sleep(0.25)















	






