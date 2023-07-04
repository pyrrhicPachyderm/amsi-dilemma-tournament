import random
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

#Takes two strategies, and runs a game.
#Returns the total payoff for both strategies.
#Results are divided by the number of iterations, to control for variable game length.
def game(strategy1, strategy2):
	num_iter = 0
	p1_moves = []
	p2_moves = []
	p1_payoff = 0
	p2_payoff = 0
	while True:
		p1_move = play(strategy1, p1_moves, p2_moves)
		p2_move = play(strategy2, p1_moves, p2_moves)
		
		p1_moves.append(p1_move)
		p2_moves.append(p2_move)
		p1_payoff += payoff(p1_move, p2_move)
		p2_payoff += payoff(p2_move, p1_move)
		num_iter += 1
		
		if random.random() >= parameters.delta:
			break
	
	p1_payoff /= num_iter
	p2_payoff /= num_iter
	
	return p1_payoff, p2_payoff
