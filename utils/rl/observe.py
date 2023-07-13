import math

import utils.parameters as parameters

overrun_chance = 1e-40
observation_space_size = math.ceil(math.log(overrun_chance, parameters.delta))

def get_observation(p1_moves, p2_moves):
	observation = [2] * (2 * observation_space_size)
	for i,move in enumerate(p1_moves):
		observation[i] = int(move)
	for i,move in enumerate(p1_moves):
		observation[i + observation_space_size] = int(move)
	return observation
