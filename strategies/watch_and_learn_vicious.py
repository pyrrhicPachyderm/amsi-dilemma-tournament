import random

name = "Watch and Learn, Vicious"
owner = "Nick"

def play(p1_moves, p2_moves, *args, **kwargs):
	lurk = 2

	if len(p2_moves) < lurk:
		return True
	if len(p2_moves) == lurk:
		return False # Hello, probe.

	# Progressive characterisation: Match your opponent.
	ambient_trust = sum(p2_moves[-lurk:])/lurk
	# Self-limiting growth, since it can't recognise itself.
	return random.random() <= ambient_trust - 0.2
