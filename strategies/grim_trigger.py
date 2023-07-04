name = "Grim Trigger"
owner = "Textbook"

def play(p1_moves, p2_moves, T, R, P, S, delta):
	#If all moves have been cooperates, keep cooperating.
	#Else, defect.
	return all(p1_moves) and all(p2_moves)
