import logging
logging.basicConfig(level =  logging.DEBUG, format = '%(asctime)s - %(levelname)s -%(message)s')


logging.debug('Start of program')

def factorial(n):
        logging.debug('Start of factorial (%s)' %(n))
        total = 1
        for i in range(n + 1):
                total *=i
                logging.debug("i is %s, total is %s" %(i, total))
	logging.debug('Return value is %s' %(total))
	return total

print(factorial(4))
