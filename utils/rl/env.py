import math
import random
import numpy as np
import gymnasium as gym

import utils.parameters as parameters
from utils.game import roll_game_length, play, payoff
from utils.load_strategies import load_strategies
from utils.rl.observe import observation_space_size, get_observation

strategies = load_strategies()

class DilemmaEnv(gym.Env):
	def __init__(self, config = None):
		config = config or {}
		
		#The action space will have two states: 0 is Defect, 1 is Cooperate.
		#The observation space has three states: the above two, plus 2 is unobserved.
		#The observation space must be of a fixed size, so we just make it *huge*.
		#Ideally, we should probably give it both the first N observations and the most recent M observations.
		#Instead, we give it just the first N observations, and make N too big to ever overrun.
		self.action_space = gym.spaces.Discrete(2) #Just two states.
		self.observation_space = gym.spaces.MultiDiscrete([3] * (2 * observation_space_size))
		
		#TODO: Set up an ecosystem of different strategies.
		
		self.reset(seed = config.get("seed", None))
	
	def draw_opponent(self, opponent_id = None, opponent_name = None):
		if opponent_id:
			return strategies[opponent]
		if opponent_name:
			return next(strategy for strategy in strategies.values() if strategy.name == opponent_name)
		
		#Draw a random opponent.
		#TODO: Allow this to be weighted.
		return random.choice(list(strategies.values()))
	
	def reset(self, opponent_id = None, opponent_name = None, seed = None, options = None):
		super().reset(seed = seed)
		
		self.opponent = self.draw_opponent(opponent_id = opponent_id, opponent_name = opponent_name)
		self.game_length = roll_game_length()
		self.game_num = 0
		self.p1_moves = []
		self.p2_moves = []
		
		observation = get_observation(self.p1_moves, self.p2_moves)
		info = {}
		
		return observation, info
	
	def step(self, action):
		p1_move = bool(action)
		p2_move = play(self.opponent, self.p2_moves, self.p1_moves)
		
		self.p1_moves.append(p1_move)
		self.p2_moves.append(p2_move)
		self.game_num += 1
		
		observation = get_observation(self.p1_moves, self.p2_moves)
		reward = payoff(p1_move, p2_move) / self.game_length
		terminated = self.game_num >= self.game_length
		truncated = False
		info = {}
		
		return observation, reward, terminated, truncated, info
