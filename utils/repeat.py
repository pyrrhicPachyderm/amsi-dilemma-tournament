#Takes two lists of equal length, and returns a list with each element of x repeated the corresponding number of times.
def rep(x, times):
	result = []
	for val, n in zip(x, times):
		result.extend([val] * n)
	return result
