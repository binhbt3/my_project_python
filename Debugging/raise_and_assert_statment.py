"""
*****
*   *
*   *
*****

"""

def boxPrint(symbol,width, height):
	if len(symbol) != 1:
		# Create a traceback to display error to user
		raise Exception ('"symbol" needs to a string of length 1.')
	
	if height < 2 or width < 2:
		raise Exception (" height and width must be greater or equal to 2")
	print(symbol*width)
	for i in range(0, height-2):
		print(symbol + " "*(height -2) + symbol )
	print(symbol*width)

boxPrint("-", 3, 3)
boxPrint("*", 1, 3)