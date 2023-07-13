import math

import utils.parameters as parameters

#Given the desired chance of overrunning the observation space, returns the required size of the observation space.
def calculate_size(overrun_chance):
	return math.ceil(math.log(overrun_chance, parameters.delta))

def get_observation_size(n, m):
	return 2 * (n + m)

#Simply uses the first n moves and the last m moves as the observation.
#n or m may be zero.
def get_observation(p1_moves, p2_moves, n, m):
	#Convert p1_moves and p2_moves to 0 (Defect) and 1 (Cooperate)
	p1_moves = [int(move) for move in p1_moves]
	p2_moves = [int(move) for move in p2_moves]
	#Populate the observation vector.
	size = get_observation_size(n, m)
	observation = [2] * size
	for i in range(min(len(p1_moves), n)):
		observation[i] = p1_moves[i]
		observation[i+n] = p2_moves[i]
	for i in range(min(len(p1_moves), m)):
		observation[size-m-i-1] = p1_moves[-i-1]
		observation[size-i-1] = p2_moves[-i-1]
	return observation
