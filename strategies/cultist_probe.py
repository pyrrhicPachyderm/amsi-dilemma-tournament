name = "Cultist Probe"
owner = "Nick"

def play(p1_moves, p2_moves, T, R, P, S, delta):
	
	# Play cultist if cultist.
	if cultist(p2_moves) is not None:
		return cultist(p2_moves)
		
	# Modification: The handshake contains a probe already.

	#If we recognise ourselves, cooperate.
	if p1_moves == p2_moves:
		return True
	
	
	responses = list(zip([True] + p1_moves[:-1], p2_moves))
	#If they've ever defected without provocation, AND the handshake failed...
	# Knives out.
	if any([p1_move and not p2_move for p1_move, p2_move in responses]):
		return False
		
	# If they're gullbile, sluuuurp. But forgive a calibration-move or two.
	if sum([not p1_move and p2_move for p1_move, p2_move in responses]) > 3:
		return False
	#Else, cooperate.
	return True

# Return: handshake move or None
def cultist(p2_moves):
	secret_handshake = [False, False, True]
	n = len(secret_handshake)
	idx = len(p2_moves)

	if idx == 0:
		# first move is first handshake move
		return secret_handshake[idx]

	elif 0 < idx < n:

		# check the partner has done the handshake correctly so far
		if all([a == b for a, b in zip(p2_moves, secret_handshake)]):

			# do the handshake
			return secret_handshake[idx]
		else:
			# if they've made a wrong move, normal strategy
			return None

	else:

		# after that, check for the handshake and verify that all moves after were cooperate
		if all([a == b for a, b in zip(p2_moves, secret_handshake)]) and all(p2_moves[n:]):

			# cooperate with fellow cultist
			return True

		else:

			# defect against all others
			return None
