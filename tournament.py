#!/usr/bin/env python3

import numpy
import matplotlib.pyplot as plt
from utils.load_strategies import load_strategies
from utils.game import game
from utils.repeat import proportion_rep
import utils.parameters as parameters

strategies = list(load_strategies().values())

N = parameters.N_per * len(strategies)

proportions = [1 / len(strategies)] * len(strategies)
population = proportion_rep(N, proportions)

results = numpy.array(proportions)

#Runs all the games for a generation, returning a list of the total payoff per strategy.
def run_generation(population):
	payoffs = [0] * len(strategies)
	for i1, s1 in enumerate(population):
		for i2, s2 in enumerate(population):
			if i1 == i2:
				continue #Each individual doesn't interact wwith itself.
			payoff1, payoff2 = game(strategies[s1], strategies[s2])
			payoffs[s1] += payoff1
			payoffs[s2] += payoff2
	
	return payoffs

#Run the evolution!
generations = range(parameters.num_gen+1)
for gen in generations[1:]:
	print(f"Generation {gen}")
	
	payoffs = run_generation(population)
	proportions = [payoff / sum(payoffs) for payoff in payoffs]
	population = proportion_rep(N, proportions)
	
	results = numpy.vstack((results, numpy.array(proportions)))

#Save the results to a csv.
numpy.savetxt("results.csv",
	numpy.column_stack((numpy.array(generations), results)),
	fmt = ["%d"] + ["%.10f"] * len(strategies),
	delimiter = ",",
	header = ",".join(["\"generation\""] + [f"\"{strategy.name}\"" for strategy in strategies]),
	comments = "",
)

#Show a plot of the results.
for i in range(results.shape[1]):
	plt.plot(generations, results[:,i], label = strategies[i].name)

plt.xlabel("Generation")
plt.ylabel("Proportion of population")
plt.xlim(min(generations), max(generations))
plt.ylim(0, 1)
plt.legend()

plt.show()
