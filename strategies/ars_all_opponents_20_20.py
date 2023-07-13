name = "ARS All Opponents 20 20"
owner = "Christopher"

import os
from sb3_contrib import ARS
import utils.rl.observe as observe

agent = ARS.load(os.path.join("rl", "agents", "ARS_all_opponents_20_20"))

def play(p1_moves, p2_moves, T, R, P, S, delta):
	action, _ = agent.predict(observe.get_observation(p1_moves, p2_moves, n = 20, m = 20))
	return action
