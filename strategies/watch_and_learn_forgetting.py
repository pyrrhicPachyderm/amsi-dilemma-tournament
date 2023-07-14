import random

name = "Watch and Learn, Forgetting"
owner = "Nick"

def play(p1_moves, p2_moves, *args, **kwargs):
	if sum(p2_moves) == len(p2_moves):
		# Cooperative until betrayed.
		return True
		
	memory_length = min(15, len(p2_moves))

	# Progressive characterisation: Match your opponent.
	ambient_trust = sum(p2_moves[-memory_length:])/memory_length
	return random.random() <= ambient_trust
