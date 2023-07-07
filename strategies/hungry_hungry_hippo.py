name = "Hungry Hungry Hippo"
owner = "Madhav"

def play(p1_moves, p2_moves, T, R, P, S, delta):
	# Testing phase: D C C
	if len(p2_moves) == 0:
		return False
	elif len(p2_moves) == 1:
		return True
	elif len(p2_moves) == 2:
		return True
	# Response phase: Diagnose opponent as one of the following.
	# Rude: Turn 1 defect, turn 3 defect
	# Weak: No defects
	# Nice: Turn 2 D, turn 3 C
	# Angy: Turn 3 D
	
	# Then perform the following response strategies:
	# Rude || Weak || Angy: Always defect. This simplifies to turn 3 D or all C.
	# Nice: Always C.
	elif(all(p2_moves) or not p2_moves[2]):
		return False
	else:
		return True
	
