#!/usr/bin/env python3

import sys
from utils.load_strategies import load_strategies
from utils.game import game

strategies = load_strategies()

if len(sys.argv) != 3:
	print(f"Usage: {sys.argv[0]} <strategy1> <strategy2>", file = sys.stderr)
	sys.exit()
if sys.argv[1] not in strategies:
	print(f"{sys.argv[1]} not found", file = sys.stderr)
	sys.exit()
if sys.argv[2] not in strategies:
	print(f"{sys.argv[2]} not found", file = sys.stderr)
	sys.exit()

strategy1 = strategies[sys.argv[1]]
strategy2 = strategies[sys.argv[2]]

p1_payoff, p2_payoff, p1_moves, p2_moves = game(strategy1, strategy2, normalise = False, return_moves = True)

strategy_strings = ["Defect", "Cooperate"]
pad_width = max(len(strategy_strings[True]), len(strategy_strings[False]), len(strategy1.name), len(strategy2.name), len(str(p1_payoff)), len(str(p2_payoff)))

print(f"{strategy1.name.rjust(pad_width)} {strategy2.name.rjust(pad_width)}")
for p1_move, p2_move in zip(p1_moves, p2_moves):
	print(f"{strategy_strings[p1_move].rjust(pad_width)} {strategy_strings[p2_move].rjust(pad_width)}")
print(f"{str(p1_payoff).rjust(pad_width)} {str(p2_payoff).rjust(pad_width)}")
