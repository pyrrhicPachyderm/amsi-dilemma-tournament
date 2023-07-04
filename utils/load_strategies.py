import os
import sys
import importlib

strategies_dir = "strategies"

def invalid_strategy(filename, message):
	print(f"File {filename} does not contain a valid strategy: {message}.", file = sys.stderr)

def load_strategies():
	strategies = []
	for filename in os.listdir(strategies_dir):
		if not os.path.isfile(os.path.join(strategies_dir, filename)):
			continue
		
		strategy = importlib.import_module(strategies_dir + "." + os.path.splitext(filename)[0])
		
		if not hasattr(strategy, "name"):
			invalid_strategy(filename, "no strategy name (\"name\" variable)")
			continue
		if not isinstance(strategy.name, str):
			invalid_strategy(filename, "strategy name is not a valid string")
			continue
		if not hasattr(strategy, "owner"):
			invalid_strategy(filename, "no owner (\"owner\" variable)")
			continue
		if not isinstance(strategy.owner, str):
			invalid_strategy(filename, "owner is not a valid string")
			continue
		if not hasattr(strategy, "play"):
			invalid_strategy(filename, "no \"play\" function")
		if not callable(strategy.play):
			invalid_strategy(filename, "\"play\" is not a function")
		#TODO: Check "play" has the correct signature
		
		strategies.append(strategy)
	return strategies
