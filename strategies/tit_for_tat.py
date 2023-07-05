name = "Tit for Tat"
owner = "Textbook"

def play(p1_moves, p2_moves, T, R, P, S, delta):
	if len(p2_moves) == 0:
		#Initial, cooperate.
		return True
	else:
		#Else, copy the opponents last move.
		return p2_moves[-1]
