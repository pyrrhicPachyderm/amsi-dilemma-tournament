import random

name = "Watch and Learn"
owner = "Nick"

def play(p1_moves, p2_moves, *args, **kwargs):
	# Progressive characterisation: Match your opponent.
	return random.randint(0,len(p2_moves)) <= sum(p2_moves)
	
	# Side note: probably rather unstable performance when facing early-determining strategies.
