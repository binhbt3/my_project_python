#assert False, "This is the error message"



market_2nd = {'ns':'green', 'ew':'red'}
def switchLights(intersection):
	for key in intersection.keys():
		if intersection[key] == 'green':
			intersection[key] = 'yellow'
		elif intersection[key] == 'yellow':
			intersection[key] = 'red'
		elif intersection[key] == 'red':
			intersection[key] = 'green'

print(market_2nd)
switchLights(market_2nd)

print(market_2nd)
