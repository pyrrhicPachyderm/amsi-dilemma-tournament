name = "Probe"
owner = "Christopher"

def play(p1_moves, p2_moves, T, R, P, S, delta):
	probe = 1 #Zero-indexed turn number on which to nastily defect.
	#On the probe turn, defect.
	if len(p2_moves) == probe:
		return False
	#If we recognise ourselves, cooperate.
	if p1_moves == p2_moves:
		return True
	#Build a list of pairs, of our moves and their responses *their move on the following turn).
	#Treat us as having cooperated before the game.
	#We don't yet have their response to our most recent move.
	responses = list(zip([True] + p1_moves[:-1], p2_moves))
	#If they've ever defected without provokation, screw 'em.
	if any([p1_move and not p2_move for p1_move, p2_move in responses]):
		return False
	#If they've ever cooperated even in the face of provokation, sucker 'em.
	if any([not p1_move and p2_move for p1_move, p2_move in responses]):
		return False
	#Else, cooperate.
	return True
