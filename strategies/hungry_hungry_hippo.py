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
	# Selfhelp edge case
	elif p1_moves == p2_moves:
		return True
	# Immediate response phase: Diagnose opponent as one of the following.
	# Rude: Turn 1 defect, turn 3 defect
	# Weak: No defects
	# Nice: Turn 2 D, turn 3 C
	# Angy: Turn 3 D
	
	# Then perform the following response strategies:
	# Rude || Weak || Angy: Always defect.
	# Nice: Always C.
	elif len(p2_moves <= 10):
		if(all(p2_moves) or not p2_moves[2]):
			return False
		else:
			return True
	
	# Extended response phase: Continually diagnose opponent.
	# Punished: Ds followed by Ds
	# Forgiven: Ds followed by Cs
	# Rudes:    Cs followed by Ds
	# Coops:    Cs followed by Cs
	else:
		Punished = 0
		Forgiven = 0
		Rude = 0
		Coop = 0
		for i in range(1,len(p1_moves)):
			if p1_moves[i-1]:
				if p2_moves[i]:
					Coop += 1
				else: 
					Rude += 1
			else:
				if p2_moves[i]:
					Forgiven += 1
				else:
					Punished += 1
		if Rude > Coop:
			return False
		elif Punished > Forgiven:
			return True
		else:
			return False
