#Takes two lists of equal length, and returns a list with each element of x repeated the corresponding number of times.
def rep(x, times):
	result = []
	for i in range(len(x)):
		result.extend([x[i]] * times[i])
	return result
