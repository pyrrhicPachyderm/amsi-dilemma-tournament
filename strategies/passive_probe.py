import random

name = "Passive Probe"
owner = "Nick"

def play(p1_moves, p2_moves, *args, **kwargs):
	#Nice
	if len(p1_moves) == sum(p1_moves):
		return True
		
	responses = zip([True] + list(p1_moves), p2_moves)
	
	if any([p1_move and not p2_move for p1_move, p2_move in responses]):
		return False
	
	if any([not p1_move and p2_move for p1_move, p2_move in responses]):
		return False
	
	return True
