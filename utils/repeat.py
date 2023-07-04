from math import floor
from operator import itemgetter

#Takes two lists of equal length, and returns a list with each element of x repeated the corresponding number of times.
def rep(x, times):
	result = []
	for val, n in zip(x, times):
		result.extend([val] * n)
	return result

#Takes a list of floating point numbers, and rounds the list to integers while preserving the sum.
def safe_round(xs):
	total = round(sum(xs))
	#First, we round everything down.
	results = [floor(x) for x in xs]
	#Then, we round up the numbers with the largest fractional parts until the sum is correct.
	residuals = [x%1 for x in xs]
	residuals = sorted(enumerate(residuals), key = itemgetter(1), reverse = True) #Sort descending by values.
	difference = total - sum(results)
	for i in range(difference):
		results[residuals[i][0]] += 1
	
	return results

#Takes a total count and a list of proportions.
#Returns a list of indices with the number of repetitions of each index as close to the proportions as possible.
def proportion_rep(n, proportions):
	times = [n * p for p in proportions]
	times = safe_round(times)
	return rep(list(range(len(times))), times)
