import random
from scipy.stats import nbinom
import utils.parameters as parameters

def play(strategy, p1_moves, p2_moves):
	return strategy.play(p1_moves, p2_moves, parameters.T, parameters.R, parameters.P, parameters.S, parameters.delta)

#Returns the payoff of player 1, given both moves.
#Is symmetric.
def payoff(p1_move, p2_move):
	if p1_move:
		if p2_move:
			return parameters.R
		else:
			return parameters.S
	else:
		if p2_move:
			return parameters.T
		else:
			return parameters.P

def roll_game_length():
	#NegativeBinomial(r, p) is the number of failures before r successes.
	#So 1 + NegativeBinomial(1, 1 - delta) is the number of games.
	return 1 + nbinom.rvs(1, 1 - parameters.delta)

#Takes two strategies, and runs a game.
#Returns the total payoff for both strategies.
#If normalise = True, results are divided by the number of iterations, to control for variable game length.
def game(strategy1, strategy2, normalise = True, return_moves = False):
	game_length = roll_game_length()
	p1_moves = []
	p2_moves = []
	p1_payoff = 0
	p2_payoff = 0
	for _ in range(game_length):
		p1_move = play(strategy1, p1_moves, p2_moves)
		p2_move = play(strategy2, p2_moves, p1_moves)
		
		p1_moves.append(p1_move)
		p2_moves.append(p2_move)
		p1_payoff += payoff(p1_move, p2_move)
		p2_payoff += payoff(p2_move, p1_move)
	
	if normalise:
		p1_payoff /= game_length
		p2_payoff /= game_length
	
	if return_moves:
		return p1_payoff, p2_payoff, p1_moves, p2_moves
	else:
		return p1_payoff, p2_payoff
