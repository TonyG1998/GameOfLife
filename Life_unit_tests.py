from Life import next_board_state

#Test 1, dead board state remain dead
init_state1 = [
	[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]
]

expected_next_state = [
	[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]
]

actual_next_state = next_board_state(init_state1)

if expected_next_state == actual_next_state:
	print ("Passed 1")
else:
	print ("Failed 1")

#test 2, 3 neighbors

init_state2 = [
	[0, 0, 1],
	[0, 1, 1],
	[0, 0, 0]
]
expected_next_state = [
	[0, 1, 1],
	[0, 1, 1],
	[0, 0, 0]
]

actual_next_state2 = next_board_state(init_state2)

if(actual_next_state2 == expected_next_state):
	print("Passed test 2")
else:
	print("Failed test 2")
	print("calculated state" + actual_next_state2)
	print("expected_next_state" + expected_next_state)


#Test for overpopulation

init_state3 = [
	[0, 0, 1],
	[0, 0, 0],
	[1, 0, 0]
]

expected_next_state3 = [
	[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]
]

actual_next_state3 = next_board_state(init_state3)

if(actual_next_state3 == expected_next_state3):
	print("Test 3 passed")
else:
	print("Test 3 failed")
	print("Caculated state: " + str(actual_next_state3))
	print("Expected next state" + str(expected_next_state3))
