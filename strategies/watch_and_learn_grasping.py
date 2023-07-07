import random

name = "Watch and Learn, Grasping"
owner = "Nick"

def play(p1_moves, p2_moves, *args, **kwargs):
	if sum(p2_moves) == len(p2_moves):
		# Cooperative until betrayed.
		return True

	# Progressive characterisation: Match your opponent.
	ambient_trust = sum(p2_moves)/len(p2_moves)
	return random.random() <= ambient_trust - 0.02
