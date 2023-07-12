name = "Two Eyes for an Eye"
owner = "Nick"

def play(p1_moves, p2_moves, T, R, P, S, delta):
	if len(p2_moves) == 1:
		return False
	if len(p2_moves) == 2:
		return False
	
	p1_defects = len(p1_moves) - sum(p1_moves)
	p2_defects = len(p2_moves) - sum(p2_moves)
	
	return p1_defects < 2*p2_defects
