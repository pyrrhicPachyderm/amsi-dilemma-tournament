name = "Nice Hippo"
owner = "Madhav"

def play(p1_moves, p2_moves, T, R, P, S, delta):
	# Selfhelp edge case
	if p1_moves == p2_moves:
		return True
	# Testing phase: C
	elif len(p2_moves) == 0:
		return True
	# Immediate response phase: Only defect if opponent defects.
	elif len(p2_moves <= 10):
		if(p2_moves[-1]):
			return True
		else:
			return False
	
	# Extended response phase: Continual diagnosis.
	# Punished: Ds followed by Ds
	# Forgiven: Ds followed by Cs
	# Rudes:    Cs followed by Ds
	# Coops:    Cs followed by Cs
	else:
		Trigger = not all(p2_moves) # If enabled, we can start capitalising.
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
		elif Trigger:
			return False
		else:
			return True
			
				
				
					
		
			
	