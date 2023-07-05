name = "Delta Chance of Cooperating"
owner = "James"

import random

def play(p1_moves, p2_moves, T, R, P, S, delta):
	if random.random()>delta:
		return False
	else:
		return True
