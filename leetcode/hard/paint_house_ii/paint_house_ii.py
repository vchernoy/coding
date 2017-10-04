


def paint(costs):
	n = len(costs)
	if n == 0:
		return 0

	k = len(costs[0])
	if k == 0:
		return 0

	F = []
	for i in xrange(n+1):
		F.append([0] * k)

	for i in xrange(1, n+1):
		for x in xrange(k):
			vals = []
			for y in xrange(k):
				if y != x:
					vals.append(costs[i-1][y] + F[i-1][y])

			F[i][x] = min(vals)

	return min(F[n][0], costs[n-1][0] + F[n-1][0])



costs = [[1,2],[5,2],[1,3]]
print paint(costs)

costs = [[1,2],[1,10],[1,3]]
print paint(costs)

costs = [[10,2]]
print paint(costs)


